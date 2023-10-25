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
    beginner_employment_markup,
    beginner_markup,
    mentor_markup,
    mentor_tasks_markup,
)


async def mentor_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Наставник/Бадди.'''

    await update.callback_query.message.reply_text(
        onboarding_text.MENTOR,
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=mentor_markup,
    )


async def mentor_tasks_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Задачи Наставника/Бадди.'''

    await update.callback_query.message.reply_text(
        onboarding_text.TASKS_FOR_MENTOR,
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=mentor_tasks_markup,
    )


async def beginner_start_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Новичок'''

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


def register_handlers(app: Application) -> None:
    app.add_handler(beginner_callback)

    registrator = {
        f'{INFO_PREFIX}mentor_or_buddy': mentor_callback,
        f'{INFO_PREFIX}menor_tasks': mentor_tasks_callback,
    }
    for pattern, handler in registrator.items():
        app.add_handler(CallbackQueryHandler(handler, pattern=pattern))
