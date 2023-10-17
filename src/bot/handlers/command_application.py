from bot.constants.text import HELP_MESSAGE, STOP_MESSAGE

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
)


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Команда запроса помощи"""
    await update.message.reply_text(HELP_MESSAGE)
    return ConversationHandler.END


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Команда остановки бота"""
    await update.message.reply_text(STOP_MESSAGE)
    return ConversationHandler.END


def register_handlers(app: Application):
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('stop', stop))
