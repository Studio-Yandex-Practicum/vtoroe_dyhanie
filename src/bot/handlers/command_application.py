from telegram import ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
)

from bot.constants.text import HELP_MESSAGE, STOP_MESSAGE


async def help_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> int:
    '''Команда запроса помощи'''

    await update.message.reply_text(HELP_MESSAGE)
    return ConversationHandler.END


async def stop_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    '''
    Функция заканчивающая работу бота.
    После её работы, бот будет принимать только команду /start.
    '''

    await update.message.reply_text(
        STOP_MESSAGE, reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


def register_handlers(app: Application) -> None:
    app.add_handler(CommandHandler('help', help_callback))
    app.add_handler(CommandHandler('stop', stop_callback))
