from telegram import Update
from telegram.ext import ContextTypes

from bot.constants.info.text import GREETING


async def greeting(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Base handler to greet the user"""
    await update.message.reply_text(GREETING)
