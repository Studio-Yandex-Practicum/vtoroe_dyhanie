from telegram import ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
)

from bot.constants.text import BACK_TO_MENU, HELP_MESSAGE, STOP_MESSAGE
from bot.keyboards.keyboards import main_menu_markup


async def help_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Команда запроса помощи'''

    await update.message.reply_text(HELP_MESSAGE)


async def menu_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Команда перехода в главное меню'''

    await update.message.reply_text(
        BACK_TO_MENU, reply_markup=main_menu_markup
    )


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
    app.add_handler(CommandHandler('menu', menu_callback))
    app.add_handler(CommandHandler('stop', stop_callback))
