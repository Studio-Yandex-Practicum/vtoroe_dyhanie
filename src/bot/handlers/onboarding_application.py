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
from bot.constants.state import BEGINNER_ONBOARDING
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


async def beginner_employment_date_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    '''
    Функция для сохранения даты трудоустройства новичка, так же возможно
    здесь реализовать отправку отложенных сообщений
    '''

    employment_date = update.message.text
    if employment_date:
        # Здесь можно реализовать отправку отложенных сообщений и проверку
        # корректности введенной даты трудоустройства
        pass

    await update.message.reply_text(
        onboarding_text.BEGINNER_EMPLOYMENT_MESSAGE_ONE
    )
    await update.message.reply_text(
        onboarding_text.BEGINNER_EMPLOYMENT_MESSAGE_TWO,
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=beginner_employment_markup,
    )
    return ConversationHandler.END


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


async def director_employment_date_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    '''
    Функция для сохранения даты трудоустройства нового сотрудника.
    '''

    director_employment_date = update.message.text
    if director_employment_date:
        # Здесь можно реализовать отправку отложенных сообщений и проверку
        # корректности введенной даты трудоустройства
        pass
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
    }
    for pattern, handler in registrator.items():
        app.add_handler(CallbackQueryHandler(handler, pattern=pattern))
