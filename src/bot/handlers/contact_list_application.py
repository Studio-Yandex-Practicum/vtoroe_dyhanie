from telegram import Update
from telegram.ext import (
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

from bot.constants import contact_list_text
from bot.constants.button import MENU_CONTACT_LIST
from bot.constants.keyword_serch import SEARCH_AGAIN_OR_EXIT
from bot.constants.state import FIND_CONTACT, FIND_CONTACT_AGAIN
from bot.constants.text import BACK_TO_MENU
from bot.handlers.command_application import stop_callback
from bot.keyboards.basic_info_keyboards import (
    contact_list_download_markup,
    contact_list_exit_markup,
)
from bot.keyboards.keyboards import main_menu_markup
from bot.utils.keyword_search import find_contacts


async def contact_list_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> int:
    '''Обрабатывает кнопку "Список контактов" из главного меню.'''
    await update.message.reply_text(
        contact_list_text.MENU_CONTACT_LIST_INPUT_FIO
    )
    await update.message.reply_text(
        contact_list_text.MENU_CONTACT_LIST_LOAD_CONTACT_LIST,
        reply_markup=contact_list_download_markup,
    )
    return FIND_CONTACT


async def find_contact_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    '''
    Проводит поиск контакта по
    заданному тексту и возвращает ответ.
    '''
    user_text = update.message.text
    answer = await find_contacts(user_text)
    await update.message.reply_text(text=answer)
    await update.message.reply_text(
        text=SEARCH_AGAIN_OR_EXIT,
        reply_markup=contact_list_exit_markup,
    )
    return FIND_CONTACT_AGAIN


async def main_menu_pressed_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    '''Обрабатывает нажатие кнопки выхода после очередного поиска.'''
    await update.callback_query.message.delete()
    await update.callback_query.message.reply_text(
        BACK_TO_MENU, reply_markup=main_menu_markup
    )
    return ConversationHandler.END


contact_list_conv_handler = ConversationHandler(
    entry_points=[
        MessageHandler(
            filters.Text([MENU_CONTACT_LIST]), contact_list_callback
        )
    ],
    states={
        FIND_CONTACT: [
            MessageHandler(filters.TEXT, find_contact_callback),
        ],
        FIND_CONTACT_AGAIN: [
            CallbackQueryHandler(
                main_menu_pressed_callback, pattern='exit_from_contact_search'
            ),
            MessageHandler(filters.TEXT, find_contact_callback),
        ],
    },
    fallbacks=[CommandHandler('stop', stop_callback)],
)
