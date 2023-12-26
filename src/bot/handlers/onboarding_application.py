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

from bot.utils.send_email import check_date_format, send_email
from bot.constants.query_patterns import INFO_PREFIX

from bot.constants.state import (
    BEGINNER_ONBOARDING,
    BEGINNER_ONBOARDING_25_DAYS,
    BEGINNER_ONBOARDING_40_DAYS,
)
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
from bot.utils.generic import check_date_format
from bot.utils.schemas import DateModel


async def mentor_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Наставник/Бадди.'''
    query = update.callback_query
    await query.answer()
    message_data = await get_django_json('onboarding_text/8/')
    await query.message.edit_text(
        message_data.get('MENTOR', ''),
        reply_markup=await mentor_markup(),
    )


async def mentor_tasks_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Задачи Наставника/Бадди.'''
    message_data = await get_django_json('onboarding_text/9/')
    await update.callback_query.message.reply_text(
        message_data.get('MENTOR_TASKS', ''),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=await mentor_tasks_markup(),
    )


async def beginner_start_callback(
        update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Новичок.'''
    message_data = await get_django_json('onboarding_text/10:11/')
    await update.callback_query.message.reply_text(
        message_data.get('BEGINNER_START_MESSAGE_ONE', '')
    )
    await update.callback_query.message.reply_text(
        message_data.get('BEGINNER_START_MESSAGE_TWO', ''),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=await beginner_markup(),
    )
    return BEGINNER_ONBOARDING


async def send_delayed_message(bot, delay, chat_id, text, reply_markup=None):
    await asyncio.sleep(delay)
    await bot.send_message(
        chat_id,
        text,
        reply_markup=reply_markup,
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True,
    )


async def send_beginner_feedback(update, bot):
    '''
    Отправка фидбэка новичка на корпоративную почту
    '''
    user_id = update.message.chat_id
    username = update.effective_user.username
    feedback = update.message.text
    text = (
        f'Никнейм пользователя в Telegram: {username}\n'
        f'Предложения:\n{feedback}'
    )
    subject = 'Фидбэк новичка'
    send_email(subject, text)
    await bot.send_message(
        user_id,
        (
            'Благодарим за обратную связь!\n'
            'Ваше предложение будет рассмотрено в ближайшее время'
        ),
    )


async def beginner_employment_feedback_after_25_days(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    '''
    Обработчик фидбэка по прошествию 25 дней
    '''
    bot = context.bot
    await send_beginner_feedback(update, bot)
    return BEGINNER_ONBOARDING_40_DAYS


async def beginner_employment_feedback_after_40_days(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    '''
    Обработчик фидбэка по прошествию 40 дней
    '''
    bot = context.bot
    await send_beginner_feedback(update, bot)
    return ConversationHandler.END


async def beginner_employment_date_callback(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE,
) -> int:
    '''
    Функция для получения даты трудоустройства новичка
    и отправка отложенных сообщений.
    '''
    employment_date = update.message.text
    current_date = datetime.now()

    if not check_date_format(employment_date):
        message_data = await get_django_json('onboarding_text/29/')
        await update.message.reply_text(
            text=message_data.get('WRONG_DATE_FORMAT', '')
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

    # Расчет количества дней после трудоустройства
    delta_days = (current_date - employment_date).days

    if employment_date:
        # Отправку отложенных сообщений и проверку
        bot = context.bot
        message_data = await get_django_json(
            'onboarding_text/30:33/'
        )
        link = message_data.get('ONBOARDING_LINK_FORM', '')
        if delta_days <= 25:
            asyncio.create_task(
                send_delayed_message(
                    bot,
                    (25 - delta_days) * 86400,
                    update.message.chat_id,
                    text=message_data.get('BEGINNER_AFTER_25_DAY_MESSAGE', ''),
                    reply_markup=feedback_keyboard_markup,
                )
            )
        elif 40 >= delta_days > 25:
            asyncio.create_task(
                send_delayed_message(
                    bot,
                    (40 - delta_days) * 86400,
                    update.message.chat_id,
                    text=message_data.get('BEGINNER_AFTER_40_DAY_MESSAGE', ''),
                )
            )
        elif 85 >= delta_days > 40:
            asyncio.create_task(
                send_delayed_message(
                    bot,
                    (85 - delta_days) * 86400,
                    update.message.chat_id,
                    text=message_data.get(
                        'BEGINNER_AFTER_85_DAY_MESSAGE', ''
                    ).format(ONBOARDING_LINK_FORM=link),
                )
            )

    message_data = await get_django_json('onboarding_text/12:13/')
    await update.message.reply_text(
        message_data.get('BEGINNER_EMPLOYMENT_MESSAGE_ONE', '')
    )
    await update.message.reply_text(
        message_data.get('BEGINNER_EMPLOYMENT_MESSAGE_TWO', ''),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=await beginner_employment_markup(),
    )
    return BEGINNER_ONBOARDING_25_DAYS


async def beginner_great_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    message_data = await get_django_json('onboarding_text/12:13/')
    send_email('Feedback', 'Все отлично!')
    message_data = await get_django_json('onboarding_text/34/')
    await update.callback_query.message.reply_text(
        message_data.get('BEGINNER_AFTER_85_DAY_MESSAGE', ''),
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=calendar_keyboard_markup,
    )


async def beginner_so_so_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    send_email('Feedback', '50/50')
    message_data = await get_django_json('onboarding_text/34/')
    await update.callback_query.message.reply_text(
        message_data.get('BEGINNER_AFTER_85_DAY_MESSAGE', ''),
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=calendar_keyboard_markup,
    )


async def beginner_help_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    send_email('Feedback', 'Не все гладко, help')
    message_data = await get_django_json('onboarding_text/34/')
    await update.callback_query.message.reply_text(
        message_data.get('BEGINNER_AFTER_85_DAY_MESSAGE', ''),
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=calendar_keyboard_markup,
    )


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
        BEGINNER_ONBOARDING_25_DAYS: [
            MessageHandler(
                filters.TEXT, beginner_employment_feedback_after_25_days
            ),
        ],
        BEGINNER_ONBOARDING_40_DAYS: [
            MessageHandler(
                filters.TEXT, beginner_employment_feedback_after_40_days
            ),
        ],
    },
    fallbacks=[CommandHandler('stop', stop_callback)],
)


async def feedback_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопок обратной связи.'''
    user_fullname = update.callback_query.from_user.full_name
    username = update.callback_query.from_user.username
    button_pressed = update.callback_query.data
    message_data = await get_django_json('onboarding_text/34:42/')
    send_email(
        (
            f"{message_data.get('BEGINNER_FEEDBACK_SUBJECT_USER', '')} "
            f"{user_fullname}({username}) "
            f"{message_data.get('BEGINNER_FEEDBACK_SUBJECT_ENDING', '')}"
        ),
        (
            f"{message_data.get('BEGINNER_FEEDBACK_BODY_START', '')} "
            f"{button_pressed}"
        ),
    )
    await update.callback_query.message.reply_text(
        message_data.get('BEGINNER_DEFERRED_MESSAGES_VARIANTS', ''),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=await calendar_keyboard_markup(),
    )


async def calendar_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопок calendar_keyboard_markup.'''
    user_fullname = update.callback_query.from_user.full_name
    username = update.callback_query.from_user.username
    button_pressed = update.callback_query.data
    message_data = await get_django_json('onboarding_text/35:45/')
    send_email(
        (
            f"{message_data.get('CALENDAR_SUBJECT_USER', '')} "
            f"{user_fullname}({username}) "
            f"{message_data.get('CALENDAR_SUBJECT_ENDING', '')}"
        ),
        (
            f"{message_data.get('CALENDAR_BODY_START', '')} "
            f"{button_pressed}"
        ),
    )
    if button_pressed == 'calendar_yes':
        await update.callback_query.message.reply_text(
            message_data.get('CALENDAR_DEFERRED_MESSAGES_VARIANTS_YES', ''),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=await thanks_markup(),
        )
    elif button_pressed == 'calendar_no':
        await update.callback_query.message.reply_text(
            message_data.get('CALENDAR_DEFERRED_MESSAGES_VARIANTS_NO', ''),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=thanks_markup,
        )


async def beginner_first_day_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Первый день.'''
    message_data = await get_django_json('onboarding_text/15:17/')
    message_link = await get_django_json('onboarding_text/6/')
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
    message_data = await get_django_json('onboarding_text/18:21/')
    message_link = await get_django_json('onboarding_text/5/')
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
    message_data = await get_django_json('onboarding_text/22/')
    message_link = await get_django_json('onboarding_text/4/')
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
    message_data = await get_django_json('onboarding_text/23/')
    link_data = await get_django_json('onboarding_text/3/')
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
    message_data = await get_django_json('onboarding_text/24/')
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
    message_data = await get_django_json('onboarding_text/25/')
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
    message_data = await get_django_json('onboarding_text/27/')
    message_data_link = await get_django_json('onboarding_text/2/')
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
    message_data = await get_django_json('onboarding_text/26/')
    await update.callback_query.message.reply_text(
        message_data.get('DATA_MESSAGE_FOR_NEW_WORKER', '')
    )
    return BEGINNER_ONBOARDING


async def calendar_yes_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    send_email('Calendar button pressed', 'Да все в календаре')
    await calendar_callback(update, context)


async def calendar_no_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    send_email('Calendar button pressed', 'Еще не успел')
    await calendar_callback(update, context)


async def director_employment_date_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    '''
    Функция для получения даты трудоустройства новичка
    и отправки отложенных сообщений
    '''
    employment_date = update.message.text
    current_date = datetime.now()

    if not check_date_format(employment_date):
        await update.message.reply_text(
            'Некорректная дата. Пожалуйста, введите дату в формате ДД.ММ.ГГГГ.'
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
    message_data = await get_django_json('onboarding_text/37:39/')

    # Расчет количества дней после трудоустройства
    delta_days = (current_date - employment_date).days

    if employment_date:
        bot = context.bot
        if delta_days <= 25:
            asyncio.create_task(
                send_delayed_message(
                    bot,
                    (25 - delta_days) * 86400,
                    update.message.chat_id,
                    message_data.get('DIRECTOR_AFTER_25_DAY_MESSAGE', ''),
                    reply_markup=calendar_keyboard_markup,
                )
            )
        elif 40 >= delta_days > 25:
            asyncio.create_task(
                send_delayed_message(
                    bot,
                    (40 - delta_days) * 86400,
                    update.message.chat_id,
                    message_data.get('DIRECTOR_AFTER_40_DAY_MESSAGE', ''),
                )
            )
        elif 85 >= delta_days > 40:
            asyncio.create_task(
                send_delayed_message(
                    bot,
                    (85 - delta_days) * 86400,
                    update.message.chat_id,
                    message_data.get('DIRECTOR_AFTER_85_DAY_MESSAGE', ''),
                )
            )
        message_data = await get_django_json('onboarding_text/28/')
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
