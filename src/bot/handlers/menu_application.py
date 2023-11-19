import html
import re

import requests
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from bot.handlers.contact_list_application import contact_list_conv_handler
from bot.keyboards.about_fund_keyboards import about_fund_section
from bot.keyboards.basic_info_keyboards import basic_information_markup
from bot.keyboards.keyboards import (
    faq_menu_markup,
    main_button_markup,
    main_menu_markup,
)
from bot.keyboards.onboarding_keyboards import onboarding_markup
from bot.keyboards.rules_keyboards import rules_markup
from bot.utils import get_django_json, send_message


async def reg_forms_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обрабатывает кнопку "Регламенты и формы" из главного меню.'''
    message_data = await get_django_json(
        'http://127.0.0.1:8000/reg_forms_text/16/')
    message_links = await get_django_json(
        'http://127.0.0.1:8000/reg_forms_text/1:15/')
    text = message_data.get('REG_FORM_MESSAGE', '')
    text = text.format(*(message_links.values()))
    await update.message.reply_text(
        text,
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True,
        reply_markup=await main_button_markup(),
    )


async def about_fund_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обрабатывает кнопку "О Фонде" из главного меню.'''
    response = requests.get('http://127.0.0.1:8000/about_fund_text/1:3/')
    messages = response.json()
    await send_message(
        message=update.message,
        message_text_value=messages,
        reply_markup=await about_fund_section(),
    )


async def feedback_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обрабатывает кнопку "Обратная связь" из главного меню.'''
    response = requests.get('http://127.0.0.1:8000/text/9:13/')
    message_data = response.json()
    feedback_message_link = message_data.get("FEEDBACK_LINK", "")
    feedback_message = message_data.get(
        "FEEDBACK_MESSAGE", "").format(FEEDBACK_LINK=feedback_message_link)
    await update.message.reply_text(
        feedback_message,
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True,
        reply_markup=await main_button_markup(),
    )


async def basic_information_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обрабатывает кнопку "Основная информация" из главного меню.'''
    response = requests.get('http://127.0.0.1:8000/basic_info_text/1/')
    message_data = response.json()
    basic_info_message = message_data.get("BASIC_INFORMATION_MENU", "")
    await update.message.reply_text(
        basic_info_message,
        reply_markup=await basic_information_markup()
    )


async def faq_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обрабатывает кнопку "FAQ" из главного меню.'''
    response = requests.get('http://127.0.0.1:8000/faq_text/4/')
    message_data = response.json()
    faq_message = message_data.get("FAQ_MESSAGE", "")
    await update.message.reply_text(
        faq_message,
        reply_markup=await faq_menu_markup()
    )


async def knowledge_base_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обрабатывает кнопку "База знаний" из главного меню.'''
    response = requests.get('http://127.0.0.1:8000/text/6:12/')
    message_data = response.json()
    kb_message = message_data.get("KNOWLEDGE_BASE_MESSAGE", "")
    kb_message_link = message_data.get("URL_KNOWLEDGE_BASE", "")
    kb_message = kb_message.format(URL_KNOWLEDGE_BASE=kb_message_link)
    await update.message.reply_text(
        text=kb_message,
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True,
        reply_markup=await main_button_markup(),
    )


async def query_back_to_main_menu_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка inline кнопки возврата в главное меню из всех подразделов.'''
    query = update.callback_query
    await query.answer()
    response = requests.get('http://127.0.0.1:8000/text/10/')
    message_data = response.json()
    back_to_menu_text = message_data.get("BACK_TO_MENU", "")
    await query.message.reply_text(
        back_to_menu_text,
        reply_markup=await main_menu_markup()
    )


async def back_to_main_menu_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Возвращает в главное меню.'''
    response = requests.get('http://127.0.0.1:8000/text/10/')
    message_data = response.json()
    back_to_menu_text = message_data.get("BACK_TO_MENU", "")
    await update.message.reply_text(
        back_to_menu_text,
        reply_markup=await main_menu_markup()
    )


def register_handlers(app: Application) -> None:
    '''Регистрация обработчиков.'''
    app.add_handler(
        CallbackQueryHandler(
            query_back_to_main_menu_callback, pattern='back_to_main_menu'
        )
    )
    app.add_handler(contact_list_conv_handler)
    response = requests.get('http://127.0.0.1:8000/keyboards/')
    key_data = response.json()
    registrator = {
        key_data['main_menu_keyboard_4_1']: reg_forms_callback,
        key_data['main_menu_keyboard_1_1']: about_fund_callback,
        key_data['main_menu_keyboard_1_2']: onboarding_callback,
        key_data['main_menu_keyboard_3_2']: feedback_callback,
        key_data['main_menu_keyboard_2_1']: basic_information_callback,
        key_data['main_menu_keyboard_2_2']: rules_information_callback,
        key_data['main_menu_keyboard_4_2']: faq_callback,
        key_data['main_menu_keyboard_3_1']: knowledge_base_callback,
        key_data['faq_menu_keyboard_5']: back_to_main_menu_callback,
    }
    for btn, callback in registrator.items():
        app.add_handler(MessageHandler(filters.Text([btn]), callback))


async def rules_information_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обрабатывает кнопку "Общие правила" из главного меню.'''
    response = requests.get('http://127.0.0.1:8000/rules_text/1/')
    message_data = response.json()
    rules_info_text = message_data.get("RULES_INFORMATION_MENU", "")
    await update.message.reply_text(
        rules_info_text,
        reply_markup=await rules_markup()
    )


async def onboarding_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Обрабатывает кнопку "Онбординг" из главного меню."""
    # Получение текста из эндпоинта
    response = requests.get('http://127.0.0.1:8000/onboarding_text/1:7/')
    message_data = response.json()
    onboarding_text = message_data.get("ONBOARDING_MENU", "")
    onboarding_text_link = message_data.get("ONBOARDING_LINK", "")
    onboarding_text_message = html.unescape(onboarding_text).format(
        ONBOARDING_LINK=onboarding_text_link
        )
    await update.message.reply_text(
        onboarding_text_message,
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True,
        reply_markup=await onboarding_markup(),
    )
