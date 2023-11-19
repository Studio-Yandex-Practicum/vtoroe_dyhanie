from telegram import Update
from telegram.ext import Application, CallbackQueryHandler, ContextTypes

from bot.constants.query_patterns import INFO_PREFIX
from bot.keyboards.basic_info_keyboards import (
    basic_information_markup,
    council_markup,
    departments_final_markup,
    departmentss_markup,
    func_departments_keyboard_base,
    guardian_council_markup,
    org_structure_markup,
    our_team_markup,
    social_networks_markup,
)
from bot.utils import get_django_json


async def organization_structure_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    '''Обработка кнопки Организационная структура.'''
    query = update.callback_query
    await query.answer()
    message_data = await get_django_json(
        'http://127.0.0.1:8000/basic_info_text/4:25/')
    org_structure_text = message_data.get("ORGANIZATION_MESSAGE", "")
    org_structure_link = message_data.get("ORGANIZATION_MESSAGE_LINK", "")
    org_structure_text = org_structure_text.format(
        org_structure_link=org_structure_link
        )
    await query.message.edit_text(
        org_structure_text,
        parse_mode='HTML',
        disable_web_page_preview=True,
        reply_markup=await org_structure_markup(),
    )


async def about_council_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    '''Обработка кнопки Совет фонда.'''
    query = update.callback_query
    await query.answer()
    message_data = await get_django_json(
        'http://127.0.0.1:8000/basic_info_text/5/')
    council_intro_text = message_data.get("COUNCIL_INTRODUCTION_MESSAGE", "")
    await query.message.edit_text(
        council_intro_text,
        parse_mode='HTML',
        disable_web_page_preview=True,
        reply_markup=await council_markup(),
    )


async def guardian_council_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    '''Обработка кнопки Попечительский совет.'''
    query = update.callback_query
    await query.answer()
    message_data = await get_django_json(
        'http://127.0.0.1:8000/basic_info_text/12/')
    guardian_council_intro_text = message_data.get(
        "GARDIAN_COUNCIL_INTRODUCTION_MESSAGE", ""
        )
    await query.message.edit_text(
        guardian_council_intro_text,
        parse_mode='HTML',
        disable_web_page_preview=True,
        reply_markup=await guardian_council_markup(),
    )


async def about_departments_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    '''Обработка кнопки Отделы Фонда.'''
    query = update.callback_query
    await query.answer()
    message_data = await get_django_json(
        'http://127.0.0.1:8000/basic_info_text/13/')
    departments_text = message_data.get("DEPARTMENTS", "")
    await query.message.edit_text(
        departments_text,
        reply_markup=await func_departments_keyboard_base()
    )


async def our_team_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    '''Обработка кнопки Наша команда.'''
    query = update.callback_query
    await query.answer()
    message_data = await get_django_json(
        'http://127.0.0.1:8000/basic_info_text/3:24/')
    our_team_message = message_data.get("OUR_TEAM_MESSAGE", "")
    our_team_message_link = message_data.get(
        "OUR_TEAM_MESSAGE_LINK", "")
    our_team_message = our_team_message.format(
        our_team_message_link=our_team_message_link
        )
    await query.message.edit_text(
        our_team_message,
        parse_mode='HTML',
        disable_web_page_preview=True,
        reply_markup=await our_team_markup(),
    )


async def contact_list_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    '''Обработка кнопки Список контактов.'''
    query = update.callback_query
    await query.answer()
    await query.message.edit_text(
        'Информация о контактах.',
        reply_markup=await our_team_markup()
    )


async def org_departments_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    '''Обработка кнопки Организационная структура.'''
    query = update.callback_query
    await query.answer()
    message_data = await get_django_json(
        'http://127.0.0.1:8000/basic_info_text/13/')
    departments_text = message_data.get("DEPARTMENTS", "")
    await query.message.edit_text(
        departments_text,
        reply_markup=await departmentss_markup()
    )


async def social_networks_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка клавиатуры Социальные сети.'''
    query = update.callback_query
    await query.answer()
    message_data = await get_django_json(
        'http://127.0.0.1:8000/basic_info_text/2/')
    fund_news_text = message_data.get("FUND_NEWS", "")
    await query.message.edit_text(
        fund_news_text,
        disable_web_page_preview=True,
        reply_markup=await social_networks_markup(),
    )


async def handle_multipattern(
    update: Update, context: ContextTypes.DEFAULT_TYPE, text: dict, markup
) -> None:
    '''Обработка клавиатуры.'''
    message_data = await get_django_json(
        'http://127.0.0.1:8000/basic_info_text/26/')
    message_link = message_data.get("COUNCIL_ANSWER_01_LINK", "")
    query = update.callback_query
    await query.answer()
    new_text = text.get(query.data)
    new_text = new_text.format(
        message_link=message_link
        )
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
    '''Обработка клавиатуры Совет Фонда.'''
    markup = await council_markup()
    message_data = await get_django_json(
        'http://127.0.0.1:8000/basic_info_text/6:11/')
    await handle_multipattern(update, context, message_data, markup)


async def departments_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка клавиатуры Отделы Фонда.'''
    markup = await departments_final_markup()
    message_data = await get_django_json(
        'http://127.0.0.1:8000/basic_info_text/14:23/')
    await handle_multipattern(update, context, message_data, markup)


async def basic_information_back_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Возврата в меню Основной информации.'''
    query = update.callback_query
    await query.answer()
    await query.message.edit_text(
        'Выберите действие:',
        reply_markup=await basic_information_markup()
    )


def register_handlers(app: Application) -> None:
    '''Регистрация обработчиков.'''
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
