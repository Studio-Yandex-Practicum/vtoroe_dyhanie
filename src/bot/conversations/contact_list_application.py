from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

from bot.constants.state import (
    MAIN_MENU,
)
from bot.keyboards import main_menu_markup


async def find_contact_by_fio(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    """Стартует поиск контакта по заданному тексту
    и возвращает контакт (телефон, имя...)"""
# тут нужно будет написать что-то, что получит на вход текст
# query.data из query = update.callback_query и пойдет в базу искать контакты
# а на выходе вернет контакт
# и пропишет результат в строчку ниже

#    await query.answer()
    await update.message.reply_text(
        text='Контакты нужного человека', reply_markup=main_menu_markup
    )
    return MAIN_MENU
