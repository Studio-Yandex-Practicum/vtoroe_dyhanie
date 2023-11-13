from telegram import Update
from telegram.ext import (
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

from bot.constants import contact_list_text
from bot.constants.button import MENU_CONTACT_LIST
from bot.constants.state import CONTACT_LIST
from bot.handlers.command_application import stop_callback
from bot.keyboards.basic_info_keyboards import contact_list_markup
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
        reply_markup=contact_list_markup,
    )
    return CONTACT_LIST


async def find_contact_by_fio(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    '''Стартует поиск контакта по заданному тексту
    и возвращает контакт (телефон, имя...).'''
    user_text = update.message.text
    answer = await find_contacts(user_text)
    await update.message.reply_text(text=answer, reply_markup=main_menu_markup)
    return ConversationHandler.END


contact_list_conv_handler = ConversationHandler(
    entry_points=[
        MessageHandler(
            filters.Text([MENU_CONTACT_LIST]), contact_list_callback
        )
    ],
    states={
        CONTACT_LIST: [
            MessageHandler(filters.TEXT, find_contact_by_fio),
        ]
    },
    fallbacks=[CommandHandler('stop', stop_callback)],
)
