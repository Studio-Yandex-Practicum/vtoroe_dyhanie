from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
)

from bot.constants.text import HELP_MESSAGE, STOP_MESSAGE


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Команда запроса помощи"""
    await update.message.reply_text(HELP_MESSAGE)


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Команда остановки бота"""
    await update.message.reply_text(STOP_MESSAGE)
    return ConversationHandler.END


def register_handlers(app: Application):
    app.add_handler(CommandHandler('start', help))
    app.add_handler(CommandHandler('stop', stop))
