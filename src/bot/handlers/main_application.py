from telegram import BotCommandScopeChat, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

from bot.constants import button
from bot.constants.state import CHECK
from bot.core.settings import settings
from bot.handlers.command_application import stop_callback
from bot.keyboards.keyboards import main_menu_markup
from bot.utils.admin_api import get_django_json


async def greeting_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    '''
    Базовая функция начинающая диалог с юзером
    и открывающий доступ к check_secret_conv_handler.
    '''
    await context.bot.set_my_commands(
        [button.START_CMD, button.HELP_CMD],
        scope=BotCommandScopeChat(update.effective_chat.id),
    )
    message_data = await get_django_json('text/3:4/')
    await update.message.reply_text(
        text=message_data['START_MESSAGE_PART_ONE'],
        reply_markup={'remove_keyboard': True},
    )
    await update.message.reply_text(message_data['START_MESSAGE_PART_TWO'])
    return CHECK


async def check_the_secret_word_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    '''Функция проверяющая доступ к боту по секретному слову.'''
    message_data = await get_django_json('text/')
    word = update.message.text
    if word.lower() != settings.secret_word.lower():
        await update.message.reply_text(
            message_data.get('FAILED_THE_TEST', '')
        )
        return CHECK
    await context.bot.set_my_commands(
        [button.START_CMD, button.MENU_CMD, button.HELP_CMD, button.STOP_CMD],
        scope=BotCommandScopeChat(update.effective_chat.id),
    )
    await update.message.reply_sticker(message_data.get('STICKER_ID', ''))
    await update.message.reply_text(
        message_data.get('PASSED_THE_TEST', ''),
        reply_markup=await main_menu_markup(),
    )
    return ConversationHandler.END


check_secret_conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', greeting_callback)],
    states={
        CHECK: [
            MessageHandler(filters.TEXT, check_the_secret_word_callback),
        ],
    },
    fallbacks=[CommandHandler('stop', stop_callback)],
)


def register_handlers(app: Application) -> None:
    '''Регистрация обработчика.'''
    app.add_handler(check_secret_conv_handler)
