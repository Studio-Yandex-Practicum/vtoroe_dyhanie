from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from bot.constants.text import REG_FORM_MESSAGE


async def reg_form_callback(
        update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Отправляет сообщение и ссылки на регламенты и формы"""
    await update.message.reply_text(
        REG_FORM_MESSAGE,
        parse_mode=ParseMode.MARKDOWN_V2,
        disable_web_page_preview=True
    )
