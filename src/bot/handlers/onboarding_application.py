import asyncio

from pydantic import BaseModel, validator, ValidationError
from datetime import datetime
from ..utils import send_email


from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

from bot.constants import onboarding_text
from bot.constants.query_patterns import INFO_PREFIX
from bot.constants.state import (
                                BEGINNER_ONBOARDING,
)

from bot.handlers.command_application import stop_callback
from bot.keyboards.onboarding_keyboards import (
    adaptation_markup,
    beginner_employment_markup,
    beginner_markup,
    checklist_markup,
    director_confirm_markup,
    director_markup,
    director_question_markup,
    director_tasks_markup,
    first_day_markup,
    mentor_markup,
    mentor_tasks_markup,
    work_plan_markup,
    feedback_keyboard_markup,
    calendar_keyboard_markup,
    thanks_markup,
)

async def mentor_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Наставник/Бадди.'''
    query = update.callback_query
    await query.answer()
    await query.message.edit_text(
        onboarding_text.MENTOR,
        reply_markup=mentor_markup,
    )


async def mentor_tasks_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Задачи Наставника/Бадди.'''
    await update.callback_query.message.reply_text(
        onboarding_text.MENTOR_TASKS,
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=mentor_tasks_markup,
    )


async def beginner_start_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Новичок.'''
    await update.callback_query.message.reply_text(
        onboarding_text.BEGINNER_START_MESSAGE_ONE
    )
    await update.callback_query.message.reply_text(
        onboarding_text.BEGINNER_START_MESSAGE_TWO,
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=beginner_markup,
    )
    return BEGINNER_ONBOARDING


class DateModel(BaseModel):
    employment_date: datetime

    @validator('employment_date')
    def date_must_be_past_or_present(cls, v):
        if v.date() > datetime.today().date():
            raise ValueError('Дата должна быть прошлой или сегодняшней. Будущие даты вводить нельзя.')
        return v

async def send_delayed_message(bot, delay, chat_id, message, reply_markup=None):
    await asyncio.sleep(delay)
    await bot.send_message(chat_id, message, reply_markup=reply_markup)

async def beginner_employment_date_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    '''
    Функция для сохранения даты трудоустройства новичка, так же возможно
    здесь реализовать отправку отложенных сообщений
    '''

    employment_date = update.message.text
    try:
        # Проверка корректности введенной даты
        datetime.strptime(employment_date, '%d-%m-%Y')
    except ValueError:
        await update.message.reply_text('Некорректная дата. Пожалуйста, введите дату в формате ДД-ММ-ГГГГ.')
        return

    try:
        DateModel(employment_date=datetime.strptime(employment_date, '%d-%m-%Y'))
    except ValidationError as e:
        error_message = e.errors()[0]['msg']
        user_friendly_error_message = error_message.replace('Value error, ', '')
        await update.message.reply_text(user_friendly_error_message)
        return
    
    if employment_date:
        # Отправку отложенных сообщений и проверку
        bot = context.bot
        asyncio.create_task(send_delayed_message(
            bot, 25, update.message.chat_id, 
            onboarding_text.BEGINNER_AFTER_25_DAY_MESSAGE,
            reply_markup=feedback_keyboard_markup,
        ))
        asyncio.create_task(send_delayed_message(
            bot, 40, update.message.chat_id, 
            onboarding_text.BEGINNER_AFTER_40_DAY_MESSAGE,
        ))
        asyncio.create_task(send_delayed_message(
            bot, 85, update.message.chat_id, 
            onboarding_text.BEGINNER_AFTER_85_DAY_MESSAGE,
        ))

    await update.message.reply_text(
        onboarding_text.BEGINNER_EMPLOYMENT_MESSAGE_ONE
    )
    await update.message.reply_text(
        onboarding_text.BEGINNER_EMPLOYMENT_MESSAGE_TWO,
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=beginner_employment_markup,
    )
    return ConversationHandler.END

async def beginner_great_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    send_email('Feedback', 'Все отлично!')
    await update.callback_query.answer()

async def beginner_so_so_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    send_email('Feedback', '50/50')
    await update.callback_query.answer()

async def beginner_help_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    send_email('Feedback', 'Не все гладко, help')
    await update.callback_query.answer()

beginner_callback = ConversationHandler(
    entry_points=[
        CallbackQueryHandler(
            beginner_start_callback, pattern=f'{INFO_PREFIX}beginner'
        )
    ],
    states={
        BEGINNER_ONBOARDING: [
            MessageHandler(filters.TEXT, beginner_employment_date_callback),
        ],
    },
    fallbacks=[CommandHandler('stop', stop_callback)],
)


async def feedback_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопок обратной связи.'''
    # Запоминаем нажатую кнопку
    button_data = update.callback_query.data
    context.user_data['last_button'] = button_data

    # Отправляем значение кнопки на почту
    send_email('Feedback button pressed', f'Button {button_data} was pressed')

    # Отправляем сообщения
    await update.callback_query.message.reply_text(
        onboarding_text.BEGINNER_DEFERRED_MESSAGES_VARIANTS,
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=calendar_keyboard_markup,
    )


async def calendar_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопок calendar_keyboard_markup.'''
    # Получаем данные обратного вызова
    callback_data = update.callback_query.data

    # Отправляем соответствующее сообщение в зависимости от данных обратного вызова
    if callback_data == 'calendar_yes':
        await update.callback_query.message.reply_text(
            onboarding_text.BEGINNER_DEFERRED_MESSAGES_VARIANTS_YES,
            parse_mode=ParseMode.MARKDOWN_V2,
            reply_markup=thanks_markup,
        )
    elif callback_data == 'calendar_no':
        await update.callback_query.message.reply_text(
            onboarding_text.BEGINNER_DEFERRED_MESSAGES_VARIANTS_NO,
            parse_mode=ParseMode.MARKDOWN_V2,
            reply_markup=thanks_markup,
        )


async def beginner_first_day_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Первый день.'''
    await update.callback_query.message.reply_text(
        onboarding_text.BEGINNER_FIRST_DAY_MESSAGE_ONE
    )
    await update.callback_query.message.reply_text(
        onboarding_text.BEGINNER_FIRST_DAY_MESSAGE_TWO,
        parse_mode=ParseMode.MARKDOWN_V2,
        disable_web_page_preview=True,
    )
    await update.callback_query.message.reply_text(
        onboarding_text.BEGINNER_FIRST_DAY_MESSAGE_THREE,
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=first_day_markup,
    )


async def beginner_adaptation_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Этапы адаптации.'''
    await update.callback_query.message.reply_text(
        onboarding_text.BEGINNER_STAGES_ADAPTATION_MESSAGE_ONE,
        parse_mode=ParseMode.MARKDOWN_V2,
        disable_web_page_preview=True,
    )
    await update.callback_query.message.reply_text(
        onboarding_text.BEGINNER_STAGES_ADAPTATION_MESSAGE_TWO
    )
    await update.callback_query.message.reply_text(
        onboarding_text.BEGINNER_STAGES_ADAPTATION_MESSAGE_THREE
    )
    await update.callback_query.message.reply_text(
        onboarding_text.BEGINNER_STAGES_ADAPTATION_MESSAGE_FOUR,
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=adaptation_markup,
    )


async def beginner_work_plan_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки План работы на испытательный срок.'''
    await update.callback_query.message.reply_text(
        onboarding_text.BEGINNER_WORK_PLAN_MESSAGE_ONE,
        parse_mode=ParseMode.MARKDOWN_V2,
        disable_web_page_preview=True,
        reply_markup=work_plan_markup,
    )


async def beginner_checklist_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Чек-лист нового сотрудника.'''
    await update.callback_query.message.reply_text(
        onboarding_text.BEGINNER_CHECK_LIST_MESSAGE_ONE,
        parse_mode=ParseMode.MARKDOWN_V2,
        disable_web_page_preview=True,
        reply_markup=checklist_markup,
    )


async def beginner_back_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Возврата в меню Новичок.'''
    await update.callback_query.message.edit_text(
        'Выберете действие:',
        reply_markup=beginner_employment_markup,
    )


async def director_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Руководитель.'''
    query = update.callback_query
    await query.answer()
    await query.message.edit_text(
        onboarding_text.DIRECTOR.get('msg_1'),
        parse_mode='HTML',
        disable_web_page_preview=True,
        reply_markup=director_markup,
    )


async def tasks_director_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Задачи Руководителя.'''
    await update.callback_query.message.reply_text(
        onboarding_text.DIRECTOR_TASKS,
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=director_tasks_markup,
    )


async def director_question_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Что за встречи?'''
    await update.callback_query.message.reply_text(
        onboarding_text.MEETINGS_MESSAGE_FOR_DIRECTOR,
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=director_question_markup,
    )


async def director_confirmation_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Супер, давай.'''
    await update.callback_query.message.reply_text(
        onboarding_text.DATA_MESSAGE_FOR_NEW_WORKER
    )
    return BEGINNER_ONBOARDING

async def calendar_yes_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    send_email('Calendar button pressed', 'Да все в календаре')
    await update.callback_query.answer()

async def calendar_no_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    send_email('Calendar button pressed', 'Еще не успел')
    await update.callback_query.answer()

async def director_employment_date_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    '''
    Функция для сохранения даты трудоустройства новичка, так же возможно
    здесь реализовать отправку отложенных сообщений
    '''

    employment_date = update.message.text
    try:
        # Проверка корректности введенной даты
        datetime.strptime(employment_date, '%d-%m-%Y')
    except ValueError:
        await update.message.reply_text('Некорректная дата. Пожалуйста, введите дату в формате ДД-ММ-ГГГГ.')
        return

    try:
        DateModel(employment_date=datetime.strptime(employment_date, '%d-%m-%Y'))
    except ValidationError as e:
        error_message = e.errors()[0]['msg']
        user_friendly_error_message = error_message.replace('Value error, ', '')
        await update.message.reply_text(user_friendly_error_message)
        return
    
    if employment_date:
        # Отправку отложенных сообщений и проверку
        bot = context.bot
        asyncio.create_task(send_delayed_message(
            bot, 25, update.message.chat_id, 
            onboarding_text.DIRECTOR_AFTER_25_DAY_MESSAGE,
            reply_markup=calendar_keyboard_markup,
        ))
        asyncio.create_task(send_delayed_message(
            bot, 40, update.message.chat_id, 
            onboarding_text.DIRECTOR_AFTER_40_DAY_MESSAGE,
        ))
        asyncio.create_task(send_delayed_message(
            bot, 85, update.message.chat_id, 
            onboarding_text.DIRECTOR_AFTER_85_DAY_MESSAGE,
        ))
        await update.message.reply_text(
        onboarding_text.REMINDER_MESSAGE_FOR_MEETINGS.get('msg_1'),
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=director_confirm_markup,
        )
    return ConversationHandler.END


director_beginner_callback = ConversationHandler(
    entry_points=[
        CallbackQueryHandler(
            director_confirmation_callback,
            pattern=f'{INFO_PREFIX}director_confirmation',
        )
    ],
    states={
        BEGINNER_ONBOARDING: [
            MessageHandler(filters.TEXT, director_employment_date_callback),
        ],
    },
    fallbacks=[CommandHandler('stop', stop_callback)],
)


def register_handlers(app: Application) -> None:
    app.add_handler(beginner_callback)
    app.add_handler(director_beginner_callback)

    # Добавьте ваши обработчики здесь
    app.add_handler(CallbackQueryHandler(beginner_great_callback, pattern='feedback_great'))
    app.add_handler(CallbackQueryHandler(beginner_so_so_callback, pattern='feedback_so_so'))
    app.add_handler(CallbackQueryHandler(beginner_help_callback, pattern='feedback_help'))
    app.add_handler(CallbackQueryHandler(calendar_yes_callback, pattern='calendar_yes'))
    app.add_handler(CallbackQueryHandler(calendar_no_callback, pattern='calendar_no'))

    registrator = {
        f'{INFO_PREFIX}first_day': beginner_first_day_callback,
        f'{INFO_PREFIX}adaptation': beginner_adaptation_callback,
        f'{INFO_PREFIX}work_plan': beginner_work_plan_callback,
        f'{INFO_PREFIX}checklist': beginner_checklist_callback,
        f'{INFO_PREFIX}director_question': director_question_callback,
        f'{INFO_PREFIX}director_tasks': tasks_director_callback,
        f'{INFO_PREFIX}director': director_callback,
        f'{INFO_PREFIX}mentor_or_buddy': mentor_callback,
        f'{INFO_PREFIX}menor_tasks': mentor_tasks_callback,
        'beginner_back': beginner_back_callback,
        'feedback': feedback_callback,
        'calendar': calendar_callback,
    }
    for pattern, handler in registrator.items():
        app.add_handler(CallbackQueryHandler(handler, pattern=pattern))
