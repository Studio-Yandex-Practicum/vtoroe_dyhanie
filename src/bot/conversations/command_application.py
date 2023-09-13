from telegram import Update
from telegram.ext import ConversationHandler, ContextTypes

from bot.constants.text.py import STOP_MESSAGE


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Команда остановки бота"""
    await update.message.reply_text(STOP_MESSAGE)
    return ConversationHandler.END
