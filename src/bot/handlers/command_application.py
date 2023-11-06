from telegram import ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

from bot.constants.text import BACK_TO_MENU, STOP_MESSAGE
from bot.keyboards.keyboards import main_menu_markup
from bot.utils import send_email


GET_USER_QUESTION = 1


async def help_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> int:
    '''Команда запроса помощи.'''
    await update.message.reply_text('Введите ваш вопрос:')
    return GET_USER_QUESTION


async def get_user_question_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> int:
    '''Функция обрабатывает сообщение с вопросом от пользователя.'''
    user_id = update.effective_user.username
    user_question = update.message.text
    subject = 'Вопрос от пользователя'
    body_text = f'Пользователь: {user_id}\nЗадает вопрос: {user_question}'
    send_email(subject, body_text)
    await update.message.reply_text(
        'Ваш вопрос отправлен. Мы свяжемся с вами в ближайшее время.'
    )
    return ConversationHandler.END


async def menu_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Команда перехода в главное меню.'''
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
    '''Регистрация обработчиков.'''
    help_handler = ConversationHandler(
        entry_points=[CommandHandler('help', help_callback)],
        states={
            GET_USER_QUESTION: [
                MessageHandler(filters.ALL, get_user_question_callback)
            ]
        },
        fallbacks=[CommandHandler('stop', stop_callback)],
    )
    app.add_handler(help_handler)
    app.add_handler(CommandHandler('menu', menu_callback))
    app.add_handler(CommandHandler('stop', stop_callback))
