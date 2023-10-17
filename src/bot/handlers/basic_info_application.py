from telegram import Update
from telegram.ext import Application, CallbackQueryHandler, ContextTypes

from bot.constants import basic_info_text
from bot.constants.query_patterns import INFO_PREFIX
from bot.keyboards.basic_info_keyboards import (
    basic_information_markup,
    council_markup,
    departments_final_markup,
    departments_markup,
    departmentss_markup,
    guardian_council_markup,
    org_structure_markup,
    our_team_markup,
    social_networks_markup,
)


async def organization_structure_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """Обработка кнопки Организационная структура."""
    query = update.callback_query
    await query.answer()
    await query.message.edit_text(
        basic_info_text.ORGANIZATION_MESSAGE,
        parse_mode='HTML',
        disable_web_page_preview=True,
        reply_markup=org_structure_markup,
    )


async def about_council_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """Обработка кнопки Совет фонда."""
    query = update.callback_query
    await query.answer()
    await query.message.edit_text(
        basic_info_text.COUNCIL_INTRODUCTION_MESSAGE,
        parse_mode='HTML',
        disable_web_page_preview=True,
        reply_markup=council_markup,
    )


async def guardian_council_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """Обработка кнопки Попечительский совет."""
    query = update.callback_query
    await query.answer()
    await query.message.edit_text(
        basic_info_text.GARDIAN_COUNCIL_INTRODUCTION_MESSAGE,
        parse_mode='HTML',
        disable_web_page_preview=True,
        reply_markup=guardian_council_markup,
    )


async def about_departments_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """Обработка кнопки Отделы Фонда."""
    query = update.callback_query
    await query.answer()
    await query.message.edit_text(
        text=basic_info_text.DEPARTMENTS, reply_markup=departments_markup
    )


async def our_team_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """Обработка кнопки Наша команда."""
    query = update.callback_query
    await query.answer()
    await query.message.edit_text(
        basic_info_text.OUR_TEAM_MESSAGE,
        parse_mode='HTML',
        disable_web_page_preview=True,
        reply_markup=our_team_markup,
    )


async def contact_list_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """Обработка кнопки список контактов."""
    query = update.callback_query
    await query.answer()
    await query.message.edit_text(
        'Информация о контактах.', reply_markup=our_team_markup
    )


async def org_departments_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.edit_text(
        text=basic_info_text.DEPARTMENTS, reply_markup=departmentss_markup
    )


async def social_networks_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Обработка клавиатуры Социальные сети."""
    query = update.callback_query
    await query.answer()
    await query.message.edit_text(
        basic_info_text.FUND_NEWS,
        disable_web_page_preview=True,
        reply_markup=social_networks_markup,
    )


async def handle_multipattern(
    update: Update, context: ContextTypes.DEFAULT_TYPE, text: dict, markup
) -> None:
    query = update.callback_query
    await query.answer()
    new_text = text.get(query.data)
    if query.message.text_html == new_text or query.message.text == new_text:
        return
    await query.message.edit_text(
        new_text,
        parse_mode='HTML',
        disable_web_page_preview=True,
        reply_markup=markup,
    )


async def council_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Обработка клавиатуры совета Фонда."""
    text = basic_info_text.COUNCIL_QUESTIONS
    markup = council_markup
    await handle_multipattern(update, context, text, markup)


async def departments_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Обработка клавиатуры отделов Фонда."""
    text = basic_info_text.DEPARTMENTS_MESSAGE
    markup = departments_final_markup
    await handle_multipattern(update, context, text, markup)


async def basic_information_back_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Обработка кнопки Возврата в меню Основной информации."""
    query = update.callback_query
    await query.answer()
    await query.message.edit_text(
        "Выберите действие:", reply_markup=basic_information_markup
    )


def register_handlers(app: Application) -> None:
    registrator = {
        fr'{INFO_PREFIX}department(\w+)': departments_callback,
        fr'{INFO_PREFIX}council_question(\w+)': council_callback,
        'basic_information_back': basic_information_back_callback,
        f'{INFO_PREFIX}our_team': our_team_callback,
        f'{INFO_PREFIX}contact_list': contact_list_callback,
        f'{INFO_PREFIX}org_departmentss': org_departments_callback,
        f'{INFO_PREFIX}organization_structure': (
            organization_structure_callback
        ),
        f'{INFO_PREFIX}council': about_council_callback,
        f'{INFO_PREFIX}guardian_council': guardian_council_callback,
        f'{INFO_PREFIX}social_networks': social_networks_callback,
        f'{INFO_PREFIX}about_departments': about_departments_callback,
    }
    for pattern, handler in registrator.items():
        app.add_handler(CallbackQueryHandler(handler, pattern=pattern))
