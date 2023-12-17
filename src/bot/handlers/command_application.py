from pydantic import ValidationError
from telegram import ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

from bot.constants.schemas import QuestionModel
from bot.constants.state import GET_USER_QUESTION
from bot.constants.text import BACK_TO_MENU, STOP_MESSAGE
from bot.keyboards.keyboards import main_menu_markup
from bot.utils.send_email import send_email


async def help_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> int:
    '''Команда запроса помощи.'''
    await update.message.reply_text('Введите ваш вопрос:')
    return GET_USER_QUESTION


async def process_commands(
    update: Update, context: ContextTypes.DEFAULT_TYPE, command: str
) -> None:
    '''Функция проверяет, если команда пользователя находится в словаре
    command_handlers, то вызывает соответствующую функцию-обработчик.'''
    command_handlers = {
        'menu': menu_callback,
        'stop': stop_callback,
    }
    if command in command_handlers:
        await command_handlers[command](update, context)


async def get_user_question_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> int:
    '''Функция обрабатывает сообщение с вопросом от пользователя.'''
    user_id = update.effective_user.username
    user_question = update.message.text
    if update.message.text.startswith('/'):
        command = update.message.text[1:]
        await process_commands(update, context, command)
        return ConversationHandler.END
    try:
        QuestionModel(question=user_question)
    except ValidationError as e:
        error_message = '\n'.join([error['msg'] for error in e.errors()])
        error_message = error_message.replace('Value error,', '')
        await update.message.reply_text(error_message.strip())
        return GET_USER_QUESTION
    subject = 'Обращение в поддержку телеграм бота'
    body_text = f'Никнейм в телеграм: {user_id}\nВопрос: {user_question}'
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
