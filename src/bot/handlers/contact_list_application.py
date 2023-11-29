from telegram import Update
from telegram.ext import (
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

from bot.constants.state import FIND_CONTACT, FIND_CONTACT_AGAIN
from bot.handlers.command_application import stop_callback
from bot.keyboards.contact_list_keyboards import (
    contact_list_download_markup,
    contact_list_exit_markup,
)
from bot.keyboards.keyboards import main_menu_markup
from bot.utils.admin_api import get_django_json, get_django_json_sync
from bot.utils.keyword_search import find_contacts


async def contact_list_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> int:
    '''Обрабатывает кнопку "Список контактов" из главного меню.'''
    message_data = await get_django_json(
        'http://127.0.0.1:8000/contact_list_text/1:2/'
    )
    await update.message.reply_text(
        message_data.get("MENU_CONTACT_LIST_INPUT_FIO", "")
    )
    await update.message.reply_text(
        message_data.get("MENU_CONTACT_LIST_LOAD_CONTACT_LIST", ""),
        reply_markup=await contact_list_download_markup(),
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
    message_data = await get_django_json(
        'http://127.0.0.1:8000/contact_list_text/6/'
    )
    await update.message.reply_text(
        text=message_data.get('SEARCH_AGAIN_OR_EXIT', ''),
        reply_markup=await contact_list_exit_markup(),
    )
    return FIND_CONTACT_AGAIN


async def main_menu_pressed_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    '''Обрабатывает нажатие кнопки выхода после очередного поиска.'''
    await update.callback_query.message.delete()
    message_data = await get_django_json('http://127.0.0.1:8000/text/10/')
    await update.callback_query.message.reply_text(
        text=message_data.get('BACK_TO_MENU', ''),
        reply_markup=await main_menu_markup(),
    )
    return ConversationHandler.END


contact_list_conv_handler = ConversationHandler(
    entry_points=[
        MessageHandler(
            filters.Text(
                get_django_json_sync('http://127.0.0.1:8000/button/9/').get(
                    'MENU_CONTACT_LIST', ""
                )
            ),
            contact_list_callback,
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
