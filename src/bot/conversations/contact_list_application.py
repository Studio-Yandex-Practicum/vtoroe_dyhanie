from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

from bot.constants.text import (
    MENU_CONTACT_LIST_INPUT_FIO, MENU_CONTACT_LIST_LOAD_CONTACT_LIST,
)


async def find_contact_by_fio(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """Стартует поиск контакта по заданному тексту
    и возвращает контакт (телефон, имя...)"""
    pass
# тут нужно будет написать что-то, что получит на вход текст
# update.message.text и пойдет в базу искать контакты
# а на выходе вернет контакт
# и пропишет результат в строчку ниже
#    await update.message.reply_text(update.message.text)


async def contact_list(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Отправляет сообщения с приглашением
    на ввод ФИО и ссылкой на базу контактов"""

    await update.message.reply_text(
        MENU_CONTACT_LIST_INPUT_FIO
    )
    await update.message.reply_text(
        MENU_CONTACT_LIST_LOAD_CONTACT_LIST
    )
