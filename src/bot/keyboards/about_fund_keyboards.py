'''Модуль с реализацией клавиатур для блока "О Фонде".
'''
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
)

from bot.constants.query_patterns import ABOUT_PREFIX
from bot.utils.admin_api import get_django_json


ABOUT_FUND_CALLBACKS = {
    'back_to_menu': f'{ABOUT_PREFIX}back_to_menu',
    'back_to_main_menu': 'back_to_main_menu',
    'more_info_mission': f'{ABOUT_PREFIX}more_info_mission',
    'more_info_path': f'{ABOUT_PREFIX}more_info_path',
    'more_info_processes': f'{ABOUT_PREFIX}more_info_processes',
    'more_info_projects': f'{ABOUT_PREFIX}more_info_projects',
    'more_info_reports': f'{ABOUT_PREFIX}more_info_reports',
}
# Общая часть для разных меню из блока О Фонде -
# две кнопки: Назад в меню блока и Назад в главное меню


async def func_navigation_menu():
    messages = await get_django_json(
        'http://127.0.0.1:8000/about_fund_keyboards/'
    )
    result = [
        (
            InlineKeyboardButton(
                messages['navigation_menu_back_to_menu'],
                callback_data=ABOUT_FUND_CALLBACKS.get('back_to_menu'),
            ),
        ),
        (
            InlineKeyboardButton(
                messages['navigation_menu_back_to_main_menu'],
                callback_data=ABOUT_FUND_CALLBACKS.get('back_to_main_menu'),
            ),
        ),
        (
            InlineKeyboardButton(
                messages['fund_mission_menu'],
                callback_data=ABOUT_FUND_CALLBACKS.get('more_info_mission'),
            ),
        ),
    ]
    return InlineKeyboardMarkup(result)


async def about_fund_section():
    messages = await get_django_json(
        'http://127.0.0.1:8000/about_fund_keyboards/3:8/'
    )
    about_fund_section_text = [text for text in messages.values()]
    about_fund_markup = ReplyKeyboardMarkup(
        [[button] for button in about_fund_section_text],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    return about_fund_markup  # noqa


async def things_path_markup():
    # response = requests.get('http://127.0.0.1:8000/about_fund_keyboards/')
    # messages = response.json()
    messages = await get_django_json(
        'http://127.0.0.1:8000/about_fund_keyboards/'
    )
    result = [
        (
            InlineKeyboardButton(
                messages['navigation_menu_back_to_menu'],
                callback_data=ABOUT_FUND_CALLBACKS.get('back_to_menu'),
            ),
        ),
        (
            InlineKeyboardButton(
                messages['navigation_menu_back_to_main_menu'],
                callback_data=ABOUT_FUND_CALLBACKS.get('back_to_main_menu'),
            ),
        ),
        (
            InlineKeyboardButton(
                messages['things_path_menu'],
                callback_data=ABOUT_FUND_CALLBACKS.get('more_info_path'),
            ),
        ),
    ]
    return InlineKeyboardMarkup(result)


async def processes_anatomy_markup():
    # response = requests.get('http://127.0.0.1:8000/about_fund_keyboards/')
    # messages = response.json()
    messages = await get_django_json(
        'http://127.0.0.1:8000/about_fund_keyboards/'
    )
    result = [
        (
            InlineKeyboardButton(
                messages['navigation_menu_back_to_menu'],
                callback_data=ABOUT_FUND_CALLBACKS.get('back_to_menu'),
            ),
        ),
        (
            InlineKeyboardButton(
                messages['navigation_menu_back_to_main_menu'],
                callback_data=ABOUT_FUND_CALLBACKS.get('back_to_main_menu'),
            ),
        ),
        (
            InlineKeyboardButton(
                messages['processes_anatomy_menu'],
                callback_data=ABOUT_FUND_CALLBACKS.get('more_info_processes'),
            ),
        ),
    ]
    return InlineKeyboardMarkup(result)


async def fund_projects_markup():
    # response = requests.get('http://127.0.0.1:8000/about_fund_keyboards/')
    # messages = response.json()
    messages = await get_django_json(
        'http://127.0.0.1:8000/about_fund_keyboards/'
    )
    result = [
        (
            InlineKeyboardButton(
                messages['navigation_menu_back_to_menu'],
                callback_data=ABOUT_FUND_CALLBACKS.get('back_to_menu'),
            ),
        ),
        (
            InlineKeyboardButton(
                messages['navigation_menu_back_to_main_menu'],
                callback_data=ABOUT_FUND_CALLBACKS.get('back_to_main_menu'),
            ),
        ),
        (
            InlineKeyboardButton(
                messages['fund_projects_menu'],
                callback_data=ABOUT_FUND_CALLBACKS.get('more_info_projects'),
            ),
        ),
    ]
    return InlineKeyboardMarkup(result)


async def annual_reports_markup():
    # response = requests.get('http://127.0.0.1:8000/about_fund_keyboards/13/')
    # messages = response.json()
    messages = await get_django_json(
        'http://127.0.0.1:8000/about_fund_keyboards/13/'
    )
    result = [
        (
            InlineKeyboardButton(
                messages['annual_reports_menu'],
                callback_data='back_to_main_menu',
            ),
        ),
    ]
    return InlineKeyboardMarkup(result)
