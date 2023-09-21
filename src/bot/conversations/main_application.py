from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

from bot.constants.state import CHECK, MENU
from bot.constants.text import (
    START_MESSAGE,
    FAILED_THE_TEST,
    PASSED_THE_TEST,
    STICKER_ID,
)
from bot.keyboards import main_menu_markup
from bot.core.settings import settings


async def greeting_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    """Базовая функция начинающая диалог с юзером и открывающий доступ к conv_handler."""
    await update.message.reply_text(START_MESSAGE)
    return CHECK


async def check_the_secret_word_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    """Функция проверяющая доступ к боту по секретному слову."""
    text = update.message.text
    if text.lower() != settings.secret_word.lower():
        await update.message.reply_text(FAILED_THE_TEST)
        return CHECK
    await update.message.reply_sticker(STICKER_ID)
    await update.message.reply_text(PASSED_THE_TEST, reply_markup=main_menu_markup)
    # Впоследствии вызов функции done заменить на возвращение значения следующего шага.
#    return await done_callback(update, context)
    return MENU
async def done_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    """Функция заканчивающая работу бота. После её работы, бот будет принимать только команду /start."""
    await update.message.reply_text("Возвращайтесь, буду рад пообщаться!")
    return ConversationHandler.END
