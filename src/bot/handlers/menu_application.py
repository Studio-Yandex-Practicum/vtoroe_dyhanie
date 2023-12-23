import html

from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

from bot.constants.state import FIND_CONTACT, FIND_CONTACT_AGAIN
from bot.handlers.command_application import stop_callback
from bot.handlers.contact_list_application import (
    contact_list_callback,
    find_contact_callback,
    main_menu_pressed_callback,
)
from bot.keyboards.about_fund_keyboards import about_fund_section
from bot.keyboards.basic_info_keyboards import basic_information_markup
from bot.keyboards.keyboards import (
    faq_menu_markup,
    main_button_markup,
    main_menu_markup,
)
from bot.keyboards.onboarding_keyboards import onboarding_markup
from bot.keyboards.rules_keyboards import rules_markup
from bot.utils.admin_api import get_django_json, get_django_json_sync
from bot.utils.send_message import send_message


async def reg_forms_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обрабатывает кнопку "Регламенты и формы" из главного меню.'''
    message_data = await get_django_json('/reg_forms_text/16/')
    message_links = await get_django_json('/reg_forms_text/1:15/')
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
    messages = await get_django_json('/about_fund_text/1:3/')
    await send_message(
        message=update.message,
        message_text_value=messages,
        reply_markup=await about_fund_section(),
    )


async def feedback_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обрабатывает кнопку "Обратная связь" из главного меню.'''
    message_data = await get_django_json('/text/9:13/')
    feedback_message_link = message_data.get("FEEDBACK_LINK", "")
    feedback_message = message_data.get("FEEDBACK_MESSAGE", "").format(
        FEEDBACK_LINK=feedback_message_link
    )
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
    message_data = await get_django_json('/basic_info_text/1/')
    basic_info_message = message_data.get("BASIC_INFORMATION_MENU", "")
    await update.message.reply_text(
        basic_info_message, reply_markup=await basic_information_markup()
    )


async def faq_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обрабатывает кнопку "FAQ" из главного меню.'''
    message_data = await get_django_json('/faq_text/4/')
    faq_message = message_data.get("FAQ_MESSAGE", "")
    await update.message.reply_text(
        faq_message, reply_markup=await faq_menu_markup()
    )


async def knowledge_base_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обрабатывает кнопку "База знаний" из главного меню.'''
    message_data = await get_django_json('/text/6:12/')
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
    message_data = await get_django_json('/text/10/')
    back_to_menu_text = message_data.get("BACK_TO_MENU", "")
    await query.message.reply_text(
        back_to_menu_text, reply_markup=await main_menu_markup()
    )


async def back_to_main_menu_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Возвращает в главное меню.'''
    message_data = await get_django_json('/text/10/')
    back_to_menu_text = message_data.get("BACK_TO_MENU", "")
    await update.message.reply_text(
        back_to_menu_text, reply_markup=await main_menu_markup()
    )


async def rules_information_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обрабатывает кнопку "Общие правила" из главного меню.'''
    message_data = await get_django_json('/rules_text/1/')
    rules_info_text = message_data.get("RULES_INFORMATION_MENU", "")
    await update.message.reply_text(
        rules_info_text, reply_markup=await rules_markup()
    )


async def onboarding_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Обрабатывает кнопку "Онбординг" из главного меню."""
    # Получение текста из эндпоинта
    message_data = await get_django_json('/onboarding_text/1:7/')
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


def register_handlers(app: Application) -> None:
    '''Регистрация обработчиков.'''
    app.add_handler(
        CallbackQueryHandler(
            query_back_to_main_menu_callback, pattern='back_to_main_menu'
        )
    )
    key_data = get_django_json_sync('/keyboards/1:9/')
    app.add_handler(
        ConversationHandler(
            entry_points=[
                MessageHandler(
                    filters.Text(key_data.get('main_menu_keyboard_5', '')),
                    contact_list_callback,
                )
            ],
            states={
                FIND_CONTACT: [
                    MessageHandler(filters.TEXT, find_contact_callback),
                ],
                FIND_CONTACT_AGAIN: [
                    CallbackQueryHandler(
                        main_menu_pressed_callback,
                        pattern='exit_from_contact_search',
                    ),
                    MessageHandler(filters.TEXT, find_contact_callback),
                ],
            },
            fallbacks=[CommandHandler('stop', stop_callback)],
        )
    )
    registrator = {
        key_data.get('main_menu_keyboard_1_1', ''): about_fund_callback,
        key_data.get('main_menu_keyboard_1_2', ''): onboarding_callback,
        key_data.get('main_menu_keyboard_2_1', ''): basic_information_callback,
        key_data.get('main_menu_keyboard_2_2', ''): rules_information_callback,
        key_data.get('main_menu_keyboard_3_1', ''): knowledge_base_callback,
        key_data.get('main_menu_keyboard_3_2', ''): feedback_callback,
        key_data.get('main_menu_keyboard_4_1', ''): reg_forms_callback,
        key_data.get('main_menu_keyboard_4_2', ''): faq_callback,
        key_data.get('faq_menu_keyboard_5', ''): back_to_main_menu_callback,
    }
    for btn, callback in registrator.items():
        app.add_handler(MessageHandler(filters.Text([btn]), callback))
