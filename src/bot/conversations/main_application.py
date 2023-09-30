from telegram import (
    Update,
)
from telegram.constants import ParseMode
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
from bot.basic_info_keyboards import (
    basic_information_markup,
)
from bot.constants import main_text, reg_forms_text
from bot.constants.basic_info_text import (
    BASIC_INFORMATION_MENU,
)
from bot.constants.state import (
    CHECK,
    FAQ,
    FEEDBACK,
    MAIN_MENU,
    BASIC_INFORMATION,
    REG_FORMS,
)
from bot.constants.contact_list_text import (
    MENU_CONTACT_LIST_INPUT_FIO,
    MENU_CONTACT_LIST_LOAD_CONTACT_LIST,
)
from bot.constants.faq_text import (
    BACK_TO_MENU,
    FAQ_MESSAGE,
)
from bot.constants.text import (
    FEEDBACK_MESSAGE,
    START_MESSAGE
)
from bot.conversations.about_fund_application import about_fund_callback
from bot.keyboards import (
    faq_menu_markup,
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
    """
    Функция проверяющая доступ к боту по секретному слову.
    """
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

    if user_input == "FAQ":
        await update.message.reply_text(
            FAQ_MESSAGE, reply_markup=faq_menu_markup
        )
        return FAQ
    if user_input == "Основная информация":
        await update.message.reply_text(
            BASIC_INFORMATION_MENU, reply_markup=basic_information_markup
        )
        return BASIC_INFORMATION
    if user_input == MENU_CONTACT_LIST:
        await update.message.reply_text(
            MENU_CONTACT_LIST_INPUT_FIO
        )
        await update.message.reply_text(
            MENU_CONTACT_LIST_LOAD_CONTACT_LIST
        )
        return FIO
    if user_input == 'Обратная связь':
        await update.message.reply_text(
            FEEDBACK_MESSAGE,
            parse_mode=ParseMode.MARKDOWN_V2,
            disable_web_page_preview=True,
            reply_markup=back_button_markup
        )
        return FEEDBACK
    if user_input == 'О Фонде':
        return await about_fund_callback(update, context)
    if user_input == 'Регламенты и формы':
        await update.message.reply_text(
            reg_forms_text.REG_FORM_MESSAGE,
            parse_mode=ParseMode.MARKDOWN_V2,
            disable_web_page_preview=True,
            reply_markup=back_button_markup
        )
        return REG_FORMS
    # Добавить обработку других кнопок.

    return MAIN_MENU


async def back_button_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> int:
    """Возвращает в главное меню"""
    await update.message.reply_text(
        BACK_TO_MENU, reply_markup=main_menu_markup
    )


async def done_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    """Функция заканчивающая работу бота.
    После её работы, бот будет принимать только команду /start.
    """
    await update.message.reply_text("Возвращайтесь, буду рад пообщаться!")
    return ConversationHandler.END
