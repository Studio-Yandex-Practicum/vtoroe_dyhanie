from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from bot.constants import button, reg_forms_text, text
from bot.constants.about_fund_text import ABOUT_FUND_HISTORY
from bot.constants.basic_info_text import BASIC_INFORMATION_MENU
from bot.constants.faq_text import FAQ_MESSAGE
from bot.constants.rules_text import RULES_INFORMATION_MENU
from bot.constants.text import FEEDBACK_MESSAGE, KNOWLEDGE_BASE_MESSAGE
from bot.handlers.contact_list_application import contact_list_conv_handler
from bot.keyboards.about_fund_keyboards import about_fund_markup
from bot.keyboards.basic_info_keyboards import basic_information_markup
from bot.keyboards.keyboards import (
    faq_menu_markup,
    main_button_markup,
    main_menu_markup,
)
from bot.keyboards.rules_keyboards import rules_markup


async def reg_forms_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Обрабатывает кнопку "Регламенты и формы" из главного меню."""
    await update.message.reply_text(
        reg_forms_text.REG_FORM_MESSAGE,
        parse_mode=ParseMode.MARKDOWN_V2,
        disable_web_page_preview=True,
        reply_markup=main_button_markup,
    )


async def about_fund_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Обрабатывает кнопку "О Фонде" из главного меню."""
    await update.message.reply_text(ABOUT_FUND_HISTORY.get('msg_1'))
    await update.message.reply_text(ABOUT_FUND_HISTORY.get('msg_2'))
    await update.message.reply_text(
        ABOUT_FUND_HISTORY.get('msg_3'), reply_markup=about_fund_markup
    )


async def feedback_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Обрабатывает кнопку "Обратная связь" из главного меню."""
    await update.message.reply_text(
        FEEDBACK_MESSAGE,
        parse_mode=ParseMode.MARKDOWN_V2,
        disable_web_page_preview=True,
        reply_markup=main_button_markup,
    )


async def basic_information_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Обрабатывает кнопку "Основная информация" из главного меню."""
    await update.message.reply_text(
        BASIC_INFORMATION_MENU, reply_markup=basic_information_markup
    )


async def faq_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Обрабатывает кнопку "FAQ" из главного меню."""
    await update.message.reply_text(FAQ_MESSAGE, reply_markup=faq_menu_markup)


async def knowledge_base_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Обрабатывает кнопку "База знаний" из главного меню."""
    await update.message.reply_text(
        text=KNOWLEDGE_BASE_MESSAGE,
        parse_mode='Markdown',
        disable_web_page_preview=True,
        reply_markup=main_button_markup,
    )


async def query_back_to_main_menu_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Обработка inline кнопки возврата в главное меню из всех подразделов."""
    query = update.callback_query
    await query.answer()
    await query.message.reply_text(
        text.BACK_TO_MENU, reply_markup=main_menu_markup
    )


async def back_to_main_menu_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Возвращает в главное меню."""
    await update.message.reply_text(
        text.BACK_TO_MENU, reply_markup=main_menu_markup
    )


def register_handlers(app: Application) -> None:
    app.add_handler(
        CallbackQueryHandler(
            query_back_to_main_menu_callback, pattern='back_to_main_menu'
        )
    )
    app.add_handler(contact_list_conv_handler)
    registrator = {
        button.MENU_REGLAMENTS_AND_FORMS: reg_forms_callback,
        button.MENU_ABOUT_FOND: about_fund_callback,
        button.MENU_FEEDBACK: feedback_callback,
        button.MENU_BASIC_INFO: basic_information_callback,
        button.MENU_GENERAL_RULES: rules_information_callback,
        button.MENU_FAQ: faq_callback,
        button.MENU_KNOWLEDGE_BASE: knowledge_base_callback,
        button.BACK_TO_MAIN_MENU: back_to_main_menu_callback,
    }
    for btn, callback in registrator.items():
        app.add_handler(MessageHandler(filters.Text([btn]), callback))


async def rules_information_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Обрабатывает кнопку "Общие правила" из главного меню."""
    await update.message.reply_text(
        RULES_INFORMATION_MENU, reply_markup=rules_markup
    )
