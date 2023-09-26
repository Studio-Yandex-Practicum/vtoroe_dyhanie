from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes, ConversationHandler

from bot.constants.state import (
    CHECK,
    FEEDBACK,
    MAIN_MENU
)
from bot.constants.text import (
    FAILED_THE_TEST,
    FEEDBACK_MESSAGE,
    START_MESSAGE,
    STICKER_ID,
    PASSED_THE_TEST,
)
from bot.keyboards import (
    main_menu_markup,
    back_button_markup
)
from bot.core.settings import settings


async def greeting_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    """Базовая функция начинающая диалог с юзером
    и открывающий доступ к conv_handler.
    """
    await update.message.reply_text(START_MESSAGE)
    return CHECK


async def check_the_secret_word_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    """Функция проверяющая доступ к боту по секретному слову."""
    text = update.message.text
    if text.lower() != settings.secret_word.lower():
        await update.message.reply_text(FAILED_THE_TEST)
        return CHECK
    await update.message.reply_sticker(STICKER_ID)
    await update.message.reply_text(
        PASSED_THE_TEST,
        reply_markup=main_menu_markup
    )
    return MAIN_MENU


async def done_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    """Функция заканчивающая работу бота.
    После её работы, бот будет принимать только команду /start.
    """
    await update.message.reply_text("Возвращайтесь, буду рад пообщаться!")
    return ConversationHandler.END


async def main_menu_actions_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    """Функция реализующая разделение обработки команд из главного меню."""
    user_input = update.message.text

    if user_input == 'Обратная связь':
        await update.message.reply_text(
            FEEDBACK_MESSAGE,
            parse_mode=ParseMode.MARKDOWN_V2,
            disable_web_page_preview=True,
            reply_markup=back_button_markup
        )
        return FEEDBACK

    # Добавить обработку других кнопок.

    return MAIN_MENU
