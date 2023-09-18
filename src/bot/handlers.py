from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters

from bot.constants.info.text import GREETING
from bot.conversations.menu_application import knowledge_base


async def greeting(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Base handler to greet the user"""
    await update.message.reply_text(GREETING)


knowledge_base_handler = MessageHandler(
    filters.Text(["База знаний"]),
    knowledge_base
)
