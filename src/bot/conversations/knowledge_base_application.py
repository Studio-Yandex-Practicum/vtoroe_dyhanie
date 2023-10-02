from telegram import Update
from telegram.ext import ContextTypes

from bot.constants.callback import MAIN_MENU_BUTTON
from bot.constants.state import MAIN_MENU, KNOWLEDGE_BASE


async def knowledge_base_callback(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
) -> int:
    """
    Функция возвращающая в Главное меню.
    """
    query = update.callback_query
    await query.answer()

    if query.data == MAIN_MENU_BUTTON:
        await query.message.reply_text('Возвращаемся в главное меню...')
        return MAIN_MENU

    return KNOWLEDGE_BASE
