from telegram import Update
from telegram.ext import Application, ContextTypes, filters, MessageHandler

from bot.constants import faq_text, text
from bot.constants.button import FAQ
from bot.keyboards.keyboards import main_menu_markup
from bot.utils import permission_required


@permission_required
async def faq_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    """Обрабатывает команды раздела FAQ"""
    user_input = update.message.text
    if user_input == FAQ.get("ORG_QUESTIONS"):
        await update.message.reply_text(
            text=faq_text.ORG_QSTS_MESSAGE,
            parse_mode="Markdown",
        )
        return FAQ
    elif user_input == FAQ.get("VOLUNTARISM"):
        await update.message.reply_text(
            text=faq_text.VOLUNTARISM_MESSAGE,
            parse_mode="Markdown",
            disable_web_page_preview=True,
        )
        return FAQ
    elif user_input == FAQ.get("STUDIES"):
        await update.message.reply_text(
            text=faq_text.STUDIES_MESSAGE,
            parse_mode="Markdown",
            disable_web_page_preview=True,
        )
        return FAQ
    elif user_input == FAQ.get("VACATION"):
        await update.message.reply_text(
            text=faq_text.VACATION_MESSAGE,
            parse_mode="Markdown",
            disable_web_page_preview=False,
        )
        return FAQ
    elif user_input == FAQ.get("WORK_PROC"):
        await update.message.reply_text(
            text=faq_text.WORK_PROC_MESSAGE,
            parse_mode="Markdown",
            disable_web_page_preview=True,
        )
        return FAQ
    elif user_input == FAQ.get("ADMIN_QUESTIONS"):
        await update.message.reply_text(
            text=faq_text.ADMIN_QSTS_MESSAGE,
            parse_mode="Markdown",
            disable_web_page_preview=False,
        )
        return FAQ
    elif user_input == FAQ.get("DOCFLOW"):
        await update.message.reply_text(
            text=faq_text.DOCFLOW_MESSAGE,
            parse_mode="Markdown",
            disable_web_page_preview=False,
        )
        return FAQ
    elif user_input == FAQ.get("BUSINESS_TRIP"):
        await update.message.reply_text(
            text=faq_text.BUSINESS_TRIP_MESSAGE,
            parse_mode="Markdown",
            disable_web_page_preview=False,
        )
        return FAQ
    elif user_input == "В главное меню":
        await update.message.reply_text(
            text.BACK_TO_MENU, reply_markup=main_menu_markup
        )


def register_handlers(app: Application) -> None:
    app.add_handler(
        MessageHandler(
            filters.Text(FAQ.values()),
            faq_callback
        )
    )
