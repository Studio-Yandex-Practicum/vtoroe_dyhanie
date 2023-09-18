from telegram import Update
from telegram.ext import ContextTypes, filters, MessageHandler

from bot.constants.info.text import GREETING
from bot.conversations.menu_application import reg_form_callback


async def greeting(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Base handler to greet the user"""
    await update.message.reply_text(GREETING)


reg_form_handler = MessageHandler(
    filters.Text(['Регламенты и формы']),
    reg_form_callback
)
