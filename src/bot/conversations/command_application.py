from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

from bot.constants.info.text import HELP
from bot.constants.text import STOP_MESSAGE


async def help(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
) -> None:
    await update.message.reply_text(HELP)
    
async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Команда остановки бота"""
    await update.message.reply_text(STOP_MESSAGE)
    return ConversationHandler.END
