from telegram import ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
)

from bot.keyboards.keyboards import main_menu_markup
from bot.utils import get_django_json


async def help_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Команда запроса помощи.'''
    messages = await get_django_json(
        'http://127.0.0.1:8000/text/2/')
    message_data = messages.get('HELP_MESSAGE', '')
    await update.message.reply_text(message_data)


async def menu_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Команда перехода в главное меню.'''
    messages = messages = await get_django_json(
        'http://127.0.0.1:8000/text/10/')
    message_data = messages.get('BACK_TO_MENU', '')
    await update.message.reply_text(
        message_data,
        reply_markup=await main_menu_markup()
    )


async def stop_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    '''
    Функция заканчивающая работу бота.
    После её работы, бот будет принимать только команду /start.
    '''
    messages = messages = await get_django_json(
        'http://127.0.0.1:8000/text/1/')
    message_data = messages.get('STOP_MESSAGE', '')
    await update.message.reply_text(
        message_data,
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


def register_handlers(app: Application) -> None:
    '''Регистрация обработчиков.'''
    app.add_handler(CommandHandler('help', help_callback))
    app.add_handler(CommandHandler('menu', menu_callback))
    app.add_handler(CommandHandler('stop', stop_callback))
