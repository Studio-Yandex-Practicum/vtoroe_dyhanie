from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from bot.constants.state import FEEDBACK, MENU
from bot.constants.text import FEEDBACK_MESSAGE
from bot.keyboards import back_button_markup, main_menu_markup


async def back_to_menu_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> int:
    """Возвращает в главное меню"""
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text='jj', reply_markup=main_menu_markup)
    return MENU


async def feedback_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Отправляет сообщение при нажатии кнопки Обратная связь."""
    await update.message.reply_text(
        FEEDBACK_MESSAGE,
        parse_mode=ParseMode.MARKDOWN_V2,
        disable_web_page_preview=True,
        reply_markup=back_button_markup
    )
    return FEEDBACK
