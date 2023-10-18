from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

from bot.constants import text
from bot.constants.state import CHECK
from bot.constants.text import START_MESSAGE_PART_ONE, START_MESSAGE_PART_TWO
from bot.core.settings import settings
from bot.keyboards.keyboards import main_menu_markup


async def greeting_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    """
    Базовая функция начинающая диалог с юзером
    и открывающий доступ к check_secret_conv_handler.
    """
    await update.message.reply_text(START_MESSAGE_PART_ONE)
    await update.message.reply_text(START_MESSAGE_PART_TWO)
    return CHECK


async def check_the_secret_word_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    """
    Функция проверяющая доступ к боту по секретному слову.
    """
    word = update.message.text
    if word.lower() != settings.secret_word.lower():
        await update.message.reply_text(text.FAILED_THE_TEST)
        return CHECK
    await update.message.reply_sticker(text.STICKER_ID)
    await update.message.reply_text(
        text.PASSED_THE_TEST, reply_markup=main_menu_markup
    )
    return ConversationHandler.END


async def done_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    """
    Функция заканчивающая работу бота.
    После её работы, бот будет принимать только команду /start.
    """
    await update.message.reply_text('Возвращайтесь, буду рад пообщаться!')
    return ConversationHandler.END


check_secret_conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', greeting_callback)],
    states={
        CHECK: [
            MessageHandler(filters.TEXT, check_the_secret_word_callback),
        ],
    },
    fallbacks=[MessageHandler(filters.Regex('^Done$'), done_callback)],
)


def register_handlers(app: Application) -> None:
    app.add_handler(check_secret_conv_handler)
