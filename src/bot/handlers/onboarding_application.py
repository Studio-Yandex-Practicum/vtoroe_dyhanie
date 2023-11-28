import asyncio
from datetime import datetime

from pydantic import ValidationError
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

from ..utils.generic import check_date_format
from ..utils.send_email import send_email
from bot.constants import onboarding_text
from bot.constants.query_patterns import INFO_PREFIX
from bot.constants.schemas import DateModel
from bot.constants.state import BEGINNER_ONBOARDING
from bot.handlers.command_application import stop_callback
from bot.keyboards.onboarding_keyboards import (
    adaptation_markup,
    beginner_employment_markup,
    beginner_markup,
    calendar_keyboard_markup,
    checklist_markup,
    director_confirm_markup,
    director_markup,
    director_question_markup,
    director_tasks_markup,
    feedback_keyboard_markup,
    first_day_markup,
    mentor_markup,
    mentor_tasks_markup,
    thanks_markup,
    work_plan_markup,
)
from bot.utils.admin_api import get_django_json


async def mentor_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Наставник/Бадди.'''
    query = update.callback_query
    await query.answer()
    message_data = await get_django_json(
        'http://127.0.0.1:8000/onboarding_text/8/'
    )
    await query.message.edit_text(
        message_data.get('MENTOR', ''),
        reply_markup=await mentor_markup(),
    )


async def mentor_tasks_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Задачи Наставника/Бадди.'''
    message_data = await get_django_json(
        'http://127.0.0.1:8000/onboarding_text/9/'
    )
    await update.callback_query.message.reply_text(
        message_data.get('MENTOR_TASKS', ''),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=await mentor_tasks_markup(),
    )


async def beginner_start_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Новичок.'''
    message_data = await get_django_json(
        'http://127.0.0.1:8000/onboarding_text/10:11/'
    )
    await update.callback_query.message.reply_text(
        message_data.get('BEGINNER_START_MESSAGE_ONE', '')
    )
    await update.callback_query.message.reply_text(
        message_data.get('BEGINNER_START_MESSAGE_TWO', ''),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=await beginner_markup(),
    )
    return BEGINNER_ONBOARDING


async def send_delayed_message(
    bot, delay, chat_id, message, reply_markup=None
):
    await asyncio.sleep(delay)
    await bot.send_message(
        chat_id,
        message,
        reply_markup=reply_markup,
    )


async def beginner_employment_date_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    '''
    Функция для сохранения даты трудоустройства новичка, так же возможно
    здесь реализовать отправку отложенных сообщений
    '''

    employment_date = update.message.text
    if not check_date_format(employment_date):
        await update.message.reply_text(
            'Некорректная дата. Пожалуйста, введите дату в формате ДД-ММ-ГГГГ.'
        )
        return None

    try:
        employment_date = datetime.strptime(employment_date, '%d-%m-%Y')
        DateModel(employment_date=employment_date)
    except ValidationError as e:
        error_message = e.errors()[0]['msg']
        user_friendly_error_message = error_message.replace(
            'Value error, ', ''
        )
        await update.message.reply_text(user_friendly_error_message)
        return None

    if employment_date:
        # Отправку отложенных сообщений и проверку
        bot = context.bot
        asyncio.create_task(
            send_delayed_message(
                bot,
                25 * 86400,
                update.message.chat_id,
                onboarding_text.BEGINNER_AFTER_25_DAY_MESSAGE,
                reply_markup=feedback_keyboard_markup,
            )
        )
        asyncio.create_task(
            send_delayed_message(
                bot,
                40 * 86400,
                update.message.chat_id,
                onboarding_text.BEGINNER_AFTER_40_DAY_MESSAGE,
            )
        )
        asyncio.create_task(
            send_delayed_message(
                bot,
                85 * 86400,
                update.message.chat_id,
                onboarding_text.BEGINNER_AFTER_85_DAY_MESSAGE,
            )
        )

    message_data = await get_django_json(
        'http://127.0.0.1:8000/onboarding_text/12:13/'
    )
    await update.message.reply_text(
        message_data.get('BEGINNER_EMPLOYMENT_MESSAGE_ONE', '')
    )
    await update.message.reply_text(
        message_data.get('BEGINNER_EMPLOYMENT_MESSAGE_TWO', ''),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=await beginner_employment_markup(),
    )
    return ConversationHandler.END


async def beginner_great_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    send_email('Feedback', 'Все отлично!')
    await update.callback_query.answer()


async def beginner_so_so_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    send_email('Feedback', '50/50')
    await update.callback_query.answer()


async def beginner_help_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
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

    # Отправляем соответствующее сообщение
    # в зависимости от данных обратного вызова
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
    message_data = await get_django_json(
        'http://127.0.0.1:8000/onboarding_text/15:17/'
    )
    message_link = await get_django_json(
        'http://127.0.0.1:8000/onboarding_text/6/'
    )
    link = message_link.get('PROBATION_PLAN_LINK', '')
    message_one = message_data.get('BEGINNER_FIRST_DAY_MESSAGE_ONE', '')
    message_two = message_data.get(
        'BEGINNER_FIRST_DAY_MESSAGE_TWO', ''
    ).format(PROBATION_PLAN_LINK=link)
    message_three = message_data.get('BEGINNER_FIRST_DAY_MESSAGE_THREE', '')
    await update.callback_query.message.reply_text(message_one)
    await update.callback_query.message.reply_text(
        message_two,
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True,
    )
    await update.callback_query.message.reply_text(
        message_three,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=await first_day_markup(),
    )


async def beginner_adaptation_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Этапы адаптации.'''
    message_data = await get_django_json(
        'http://127.0.0.1:8000/onboarding_text/18:21/'
    )
    message_link = await get_django_json(
        'http://127.0.0.1:8000/onboarding_text/5/'
    )
    link = message_link.get('TASK_PLAN_LINK', '')
    await update.callback_query.message.reply_text(
        message_data.get('BEGINNER_STAGES_ADAPTATION_MESSAGE_ONE', '').format(
            TASK_PLAN_LINK=link
        ),
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True,
    )
    await update.callback_query.message.reply_text(
        message_data.get('BEGINNER_STAGES_ADAPTATION_MESSAGE_TWO', '')
    )
    await update.callback_query.message.reply_text(
        message_data.get('BEGINNER_STAGES_ADAPTATION_MESSAGE_THREE', '')
    )
    await update.callback_query.message.reply_text(
        message_data.get('BEGINNER_STAGES_ADAPTATION_MESSAGE_FOUR', ''),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=await adaptation_markup(),
    )


async def beginner_work_plan_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки План работы на испытательный срок.'''
    message_data = await get_django_json(
        'http://127.0.0.1:8000/onboarding_text/22/'
    )
    message_link = await get_django_json(
        'http://127.0.0.1:8000/onboarding_text/4/'
    )
    link = message_link.get('WORK_PLAN_LINK', '')
    await update.callback_query.message.reply_text(
        message_data.get('BEGINNER_WORK_PLAN_MESSAGE_ONE', '').format(
            WORK_PLAN_LINK=link
        ),
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True,
        reply_markup=await work_plan_markup(),
    )


async def beginner_checklist_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Чек-лист нового сотрудника.'''
    message_data = await get_django_json(
        'http://127.0.0.1:8000/onboarding_text/23/'
    )
    link_data = await get_django_json(
        'http://127.0.0.1:8000/onboarding_text/3/'
    )
    link = link_data.get('CHECK_LIST_LINK', '')
    message = message_data.get('BEGINNER_CHECK_LIST_MESSAGE_ONE', '').format(
        CHECK_LIST_LINK=link
    )
    await update.callback_query.message.reply_text(
        message,
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True,
        reply_markup=await checklist_markup(),
    )


async def beginner_back_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Возврата в меню Новичок.'''
    await update.callback_query.message.edit_text(
        'Выберете действие:',
        reply_markup=await beginner_employment_markup(),
    )


async def director_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Руководитель.'''
    query = update.callback_query
    await query.answer()
    message_data = await get_django_json(
        'http://127.0.0.1:8000/onboarding_text/24/'
    )
    await query.message.edit_text(
        message_data.get('DIRECTOR_msg_1', ''),
        parse_mode='HTML',
        disable_web_page_preview=True,
        reply_markup=await director_markup(),
    )


async def tasks_director_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Задачи Руководителя.'''
    message_data = await get_django_json(
        'http://127.0.0.1:8000/onboarding_text/25/'
    )
    text = message_data.get('DIRECTOR_TASKS', '')
    await update.callback_query.message.reply_text(
        text,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=await director_tasks_markup(),
    )


async def director_question_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Что за встречи?'''
    message_data = await get_django_json(
        'http://127.0.0.1:8000/onboarding_text/27/'
    )
    message_data_link = await get_django_json(
        'http://127.0.0.1:8000/onboarding_text/2/'
    )
    link = message_data_link.get('START_MEETING_LINK', '')
    message = message_data.get('MEETINGS_MESSAGE_FOR_DIRECTOR', '').format(
        START_MEETING_LINK=link
    )
    await update.callback_query.message.reply_text(
        message,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=await director_question_markup(),
    )


async def director_confirmation_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Супер, давай.'''
    message_data = await get_django_json(
        'http://127.0.0.1:8000/onboarding_text/26/'
    )
    await update.callback_query.message.reply_text(
        message_data.get('DATA_MESSAGE_FOR_NEW_WORKER', '')
    )
    return BEGINNER_ONBOARDING


async def calendar_yes_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    send_email('Calendar button pressed', 'Да все в календаре')
    await update.callback_query.answer()


async def calendar_no_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    send_email('Calendar button pressed', 'Еще не успел')
    await update.callback_query.answer()


async def director_employment_date_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    '''
    Функция для сохранения даты трудоустройства новичка,
    так же возможно здесь реализовать
    отправку отложенных сообщений
    '''

    employment_date = update.message.text
    if not check_date_format(employment_date):
        await update.message.reply_text(
            'Некорректная дата. Пожалуйста, введите дату в формате ДД-ММ-ГГГГ.'
        )
        return None

    try:
        employment_date = datetime.strptime(employment_date, '%d-%m-%Y')
        DateModel(employment_date=employment_date)
    except ValidationError as e:
        error_message = e.errors()[0]['msg']
        user_friendly_error_message = error_message.replace(
            'Value error, ', ''
        )
        await update.message.reply_text(user_friendly_error_message)
        return None

    if employment_date:
        # Отправку отложенных сообщений и проверку
        bot = context.bot
        asyncio.create_task(
            send_delayed_message(
                bot,
                25 * 86400,
                update.message.chat_id,
                onboarding_text.DIRECTOR_AFTER_25_DAY_MESSAGE,
                reply_markup=calendar_keyboard_markup,
            )
        )
        asyncio.create_task(
            send_delayed_message(
                bot,
                40 * 86400,
                update.message.chat_id,
                onboarding_text.DIRECTOR_AFTER_40_DAY_MESSAGE,
            )
        )
        asyncio.create_task(
            send_delayed_message(
                bot,
                85 * 86400,
                update.message.chat_id,
                onboarding_text.DIRECTOR_AFTER_85_DAY_MESSAGE,
            )
        )
        message_data = await get_django_json(
            'http://127.0.0.1:8000/onboarding_text/27/'
        )
        await update.message.reply_text(
            message_data.get('REMINDER_MESSAGE_FOR_MEETINGS_msg_1', ''),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=await director_confirm_markup(),
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
    app.add_handler(
        CallbackQueryHandler(beginner_great_callback, pattern='feedback_great')
    )
    app.add_handler(
        CallbackQueryHandler(beginner_so_so_callback, pattern='feedback_so_so')
    )
    app.add_handler(
        CallbackQueryHandler(beginner_help_callback, pattern='feedback_help')
    )
    app.add_handler(
        CallbackQueryHandler(calendar_yes_callback, pattern='calendar_yes')
    )
    app.add_handler(
        CallbackQueryHandler(calendar_no_callback, pattern='calendar_no')
    )

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
