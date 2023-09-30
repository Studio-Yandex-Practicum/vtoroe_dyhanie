from telegram import (
    Update,
)
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
)
from bot.constants.button import MENU_CONTACT_LIST
from bot.constants.state import (
    CHECK,
    MAIN_MENU,
    BASIC_INFORMATION,
    FIO,
)
from bot.constants.basic_info_text import (
    BASIC_INFORMATION_MENU,
)
from bot.basic_info_keyboards import (
    basic_information_markup,
)
from bot.constants import main_text
from bot.keyboards import (
    main_menu_markup,
)

from bot.core.settings import settings
from bot.conversations.contact_list_application import (
    contact_list,
)

async def greeting_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    """Базовая функция начинающая диалог с юзером и открывающий доступ к conv_handler."""
    await update.message.reply_text(main_text.START_MESSAGE)
    return CHECK


async def check_the_secret_word_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    """Функция проверяющая доступ к боту по секретному слову."""
    text = update.message.text
    if text.lower() != settings.secret_word.lower():
        await update.message.reply_text(main_text.FAILED_THE_TEST)
        return CHECK
    await update.message.reply_sticker(main_text.STICKER_ID)
    await update.message.reply_text(
        main_text.PASSED_THE_TEST, reply_markup=main_menu_markup
    )
    return MAIN_MENU


async def main_menu_actions_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    """Функция реализующая разделение обработки команд из главного меню."""
    user_input = update.message.text

    if user_input == "Основная информация":
        await update.message.reply_text(
            BASIC_INFORMATION_MENU, reply_markup=basic_information_markup
        )
        return BASIC_INFORMATION
    elif user_input == MENU_CONTACT_LIST:
        await contact_list(update, context)
        return FIO
    # Добавить обработку других кнопок.

    return MAIN_MENU


async def done_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    """Функция заканчивающая работу бота. После её работы, бот будет принимать только команду /start."""
    await update.message.reply_text("Возвращайтесь, буду рад пообщаться!")
    return ConversationHandler.END
