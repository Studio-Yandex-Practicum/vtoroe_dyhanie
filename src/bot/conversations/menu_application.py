from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from bot.constants.text import FEEDBACK_MESSAGE


async def feedback_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Отправляет сообщение при нажатии кнопки Обратная связь"""
    await update.message.reply_text(
        FEEDBACK_MESSAGE,
        parse_mode=ParseMode.MARKDOWN_V2,
        disable_web_page_preview=True
    )
