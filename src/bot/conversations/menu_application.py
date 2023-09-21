from telegram import Update
from telegram.ext import ContextTypes

from bot.constants.text import (
    MENU_CONTACT_LIST_INPUT_FIO, MENU_CONTACT_LIST_LOAD_CONTACT_LIST
)

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




