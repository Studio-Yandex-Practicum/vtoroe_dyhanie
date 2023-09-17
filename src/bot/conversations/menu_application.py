from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, ContextTypes

from bot.constants.button import (
    MENU_ABOUT_FOND, MENU_ONBOARDING, MENU_GENERAL_INFO,
    MENU_GENERAL_RULES, MENU_KNOWLEDGE_BASE, MENU_FEEDBACK,
    MENU_REGLAMENTS_AND_FORMS, MENU_FAQ, MENU_CONTACT_LIST,
    NUMBER_OF_COLUMNS,
)
from bot.constants.text import (
    MENU_CONTACT_LIST_INPUT_FIO, MENU_CONTACT_LIST_LOAD_CONTACT_LIST
)
from bot.utils import build_menu

BUTTONS = [
    InlineKeyboardButton(MENU_ABOUT_FOND, callback_data=MENU_ABOUT_FOND),
    InlineKeyboardButton(MENU_ONBOARDING, callback_data=MENU_ONBOARDING),
    InlineKeyboardButton(MENU_GENERAL_INFO, callback_data=MENU_GENERAL_INFO),
    InlineKeyboardButton(MENU_GENERAL_RULES, callback_data=MENU_GENERAL_RULES),
    InlineKeyboardButton(MENU_KNOWLEDGE_BASE, callback_data=MENU_KNOWLEDGE_BASE),
    InlineKeyboardButton(MENU_FEEDBACK, callback_data=MENU_FEEDBACK),
    InlineKeyboardButton(MENU_REGLAMENTS_AND_FORMS, callback_data=MENU_REGLAMENTS_AND_FORMS),
    InlineKeyboardButton(MENU_FAQ, callback_data=MENU_FAQ)
]
FOOTER_BUTTONS = InlineKeyboardButton(MENU_CONTACT_LIST, callback_data=MENU_CONTACT_LIST)

# Тут должен быть обработчик с запуском меню, а может быть и в другом месте
# типа bot.handlers или bot.conversation.command_application
# с проверкой секретного слова, пока тут заглушка в виде 
# команды start, из которой происходит отрисовка меню
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
# сборка клавиатуры из кнопок `InlineKeyboardButton`
    reply_markup = InlineKeyboardMarkup(
        build_menu(
            buttons=BUTTONS,
            n_cols=NUMBER_OF_COLUMNS,
            footer_buttons=FOOTER_BUTTONS
        )
    )
    await update.message.reply_text('Пожалуйста, выберите:', reply_markup=reply_markup)

async def menu_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    variant = query.data

    await query.answer()

    if variant == MENU_CONTACT_LIST:
        await query.message.reply_text(
            MENU_CONTACT_LIST_INPUT_FIO
        )
        await query.message.reply_text(
            MENU_CONTACT_LIST_LOAD_CONTACT_LIST
        )
    else:
        await query.message.reply_text(
            'Что-то еще...'
        )
