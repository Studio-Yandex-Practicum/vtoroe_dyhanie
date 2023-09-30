from telegram import Update

from telegram.ext import ContextTypes

from bot.constants import faq_text
from bot.constants.state import FAQ, MAIN_MENU
from bot.keyboards import main_menu_markup


async def faq_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    """Обрабатывает команды раздела FAQ"""
    user_input = update.message.text
    if user_input == "Организационные вопросы":
        await update.message.reply_text(
            text=faq_text.ORG_QSTS_MESSAGE,
            parse_mode="Markdown",
        )
        return FAQ
    elif user_input == "Волонтёрство":
        await update.message.reply_text(
            text=faq_text.VOLUNTARISM_MESSAGE,
            parse_mode="Markdown",
            disable_web_page_preview=True,
        )
        return FAQ
    elif user_input == "Обучение":
        await update.message.reply_text(
            text=faq_text.STUDIES_MESSAGE,
            parse_mode="Markdown",
            disable_web_page_preview=True,
        )
        return FAQ
    elif user_input == "Отпуск":
        await update.message.reply_text(
            text=faq_text.VACATION_MESSAGE,
            parse_mode="Markdown",
            disable_web_page_preview=False,
        )
        return FAQ
    elif user_input == "Рабочий процесс":
        await update.message.reply_text(
            text=faq_text.WORK_PROC_MESSAGE,
            parse_mode="Markdown",
            disable_web_page_preview=True,
        )
        return FAQ
    elif user_input == "Административные вопросы":
        await update.message.reply_text(
            text=faq_text.ADMIN_QSTS_MESSAGE,
            parse_mode="Markdown",
            disable_web_page_preview=False,
        )
        return FAQ
    elif user_input == "Оформление документов":
        await update.message.reply_text(
            text=faq_text.DOCFLOW_MESSAGE,
            parse_mode="Markdown",
            disable_web_page_preview=False,
        )
        return FAQ
    elif user_input == "Командировки":
        await update.message.reply_text(
            text=faq_text.BUSINESS_TRIP_MESSAGE,
            parse_mode="Markdown",
            disable_web_page_preview=False,
        )
        return FAQ
    elif user_input == "В главное меню":
        await update.message.reply_text(
            faq_text.BACK_TO_MENU, reply_markup=main_menu_markup
        )
        return MAIN_MENU
