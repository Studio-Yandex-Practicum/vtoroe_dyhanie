from telegram import Update
from telegram.ext import ContextTypes

from bot.constants.text import KNOWLEDGE_BASE_MESSAGE


async def knowledge_base(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Отсылает сообщение с описанием базы знаний и ссылку на нее."""
    await update.message.reply_text(
        text=KNOWLEDGE_BASE_MESSAGE,
        parse_mode="Markdown",
        disable_web_page_preview=True,
    )
from telegram import CallbackQuery, Update
from telegram.ext import ContextTypes

from bot.constants.state import MAIN_MENU
from bot.constants.text import (
    BACK_TO_MAIN_MENU
)

from bot.keyboards import main_menu_markup


async def back_to_menu_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
) -> int:
    """Возвращает в главное меню."""
    query = update.callback_query
    await query.edit_message_reply_markup()
    return await handle_back_to_main_menu(query)


async def handle_back_to_main_menu(query: CallbackQuery) -> int:
    """Обработчик нажатия кнопки В главное меню"""
    await query.answer()
    await query.message.reply_text(
        BACK_TO_MAIN_MENU, reply_markup=main_menu_markup
    )
    return MAIN_MENU

