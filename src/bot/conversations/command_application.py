from telegram import Update
from telegram.ext import ConversationHandler


STOP_MESSAGE = "Бот остановлен."


async def stop(update: Update, context):
    """Команда остановки бота"""
    await update.message.reply_text(STOP_MESSAGE)
    return ConversationHandler.END
