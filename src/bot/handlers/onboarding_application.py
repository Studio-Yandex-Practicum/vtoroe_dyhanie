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
from bot.utils import get_django_json


async def mentor_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Наставник/Бадди.'''
    query = update.callback_query
    await query.answer()
    message_data = await get_django_json(
        'http://127.0.0.1:8000/onboarding_text/8/')
    await query.message.edit_text(
        message_data.get('MENTOR', ''),
        reply_markup=await mentor_markup(),
    )


async def mentor_tasks_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Задачи Наставника/Бадди.'''
    message_data = await get_django_json(
        'http://127.0.0.1:8000/onboarding_text/9/')
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
        'http://127.0.0.1:8000/onboarding_text/10:11/')
    await update.callback_query.message.reply_text(
        message_data.get('BEGINNER_START_MESSAGE_ONE', '')
    )
    await update.callback_query.message.reply_text(
        message_data.get('BEGINNER_START_MESSAGE_TWO', ''),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=await beginner_markup(),
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
    message_data = await get_django_json(
        'http://127.0.0.1:8000/onboarding_text/12:13/')
    await update.message.reply_text(
        message_data.get('BEGINNER_EMPLOYMENT_MESSAGE_ONE', '')
    )
    await update.message.reply_text(
        message_data.get('BEGINNER_EMPLOYMENT_MESSAGE_TWO', ''),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=await beginner_employment_markup(),
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
    message_data = await get_django_json(
        'http://127.0.0.1:8000/onboarding_text/15:17/')
    message_link = await get_django_json(
        'http://127.0.0.1:8000/onboarding_text/6/')
    link = message_link.get('PROBATION_PLAN_LINK', '')
    message_one = message_data.get(
        'BEGINNER_FIRST_DAY_MESSAGE_ONE', '')
    message_two = message_data.get(
        'BEGINNER_FIRST_DAY_MESSAGE_TWO', '').format(
            PROBATION_PLAN_LINK=link)
    message_three = message_data.get(
        'BEGINNER_FIRST_DAY_MESSAGE_THREE', '')
    await update.callback_query.message.reply_text(
        message_one
    )
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
        'http://127.0.0.1:8000/onboarding_text/18:21/')
    message_link = await get_django_json(
        'http://127.0.0.1:8000/onboarding_text/5/')
    link = message_link.get('TASK_PLAN_LINK', '')
    await update.callback_query.message.reply_text(
        message_data.get(
            'BEGINNER_STAGES_ADAPTATION_MESSAGE_ONE', ''
        ).format(TASK_PLAN_LINK=link),
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
        'http://127.0.0.1:8000/onboarding_text/22/')
    message_link = await get_django_json(
        'http://127.0.0.1:8000/onboarding_text/4/')
    link = message_link.get('WORK_PLAN_LINK', '')
    await update.callback_query.message.reply_text(
        message_data.get(
            'BEGINNER_WORK_PLAN_MESSAGE_ONE', ''
        ).format(WORK_PLAN_LINK=link),
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True,
        reply_markup=await work_plan_markup(),
    )


async def beginner_checklist_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Чек-лист нового сотрудника.'''
    message_data = await get_django_json(
        'http://127.0.0.1:8000/onboarding_text/23/')
    link_data = await get_django_json(
        'http://127.0.0.1:8000/onboarding_text/3/')
    link = link_data.get('CHECK_LIST_LINK', '')
    message = message_data.get(
        'BEGINNER_CHECK_LIST_MESSAGE_ONE', '').format(
            CHECK_LIST_LINK=link)
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
        'http://127.0.0.1:8000/onboarding_text/24/')
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
        'http://127.0.0.1:8000/onboarding_text/25/')
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
        'http://127.0.0.1:8000/onboarding_text/27/')
    message_data_link = await get_django_json(
        'http://127.0.0.1:8000/onboarding_text/2/')
    link = message_data_link.get('START_MEETING_LINK', '')
    message = message_data.get(
        'MEETINGS_MESSAGE_FOR_DIRECTOR', '').format(START_MEETING_LINK=link)
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
        'http://127.0.0.1:8000/onboarding_text/26/')
    await update.callback_query.message.reply_text(
        message_data.get('DATA_MESSAGE_FOR_NEW_WORKER', '')
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
    message_data = await get_django_json(
        'http://127.0.0.1:8000/onboarding_text/27/')
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
        'beginner': beginner_back_callback,
    }
    for pattern, handler in registrator.items():
        app.add_handler(CallbackQueryHandler(handler, pattern=pattern))
