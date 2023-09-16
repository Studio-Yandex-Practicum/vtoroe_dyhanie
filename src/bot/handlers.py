from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from bot.constants.info.text import GREETING
from bot.constants.text import REG_FORM_MESSAGE


async def greeting(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Base handler to greet the user"""
    await update.message.reply_text(GREETING)


async def reg_form_callback(
        update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Send text and links to user with registration and forms message."""
    await update.message.reply_text(
        REG_FORM_MESSAGE,
        parse_mode=ParseMode.MARKDOWN_V2,
        disable_web_page_preview=True
    )
