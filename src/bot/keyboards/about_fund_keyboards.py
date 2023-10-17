"""Модуль с реализацией клавиатур для блока "О Фонде"
"""

from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
)

from bot.constants.query_patterns import ABOUT_PREFIX


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
navigation_menu = [
    (
        InlineKeyboardButton(
            'В меню раздела',
            callback_data=ABOUT_FUND_CALLBACKS.get('back_to_menu'),
        ),
    ),
    (
        InlineKeyboardButton(
            'В главное меню',
            callback_data=ABOUT_FUND_CALLBACKS.get('back_to_main_menu'),
        ),
    ),
]

about_fund_section = [
    'Миссия и основная цель',
    'Путь вещей',
    'Анатомия процессов',
    'Проекты Фонда',
    'Годовые отчеты',
    'В главное меню',
]
about_fund_markup = ReplyKeyboardMarkup(
    [[button] for button in about_fund_section],
    resize_keyboard=True,
    one_time_keyboard=True,
)


fund_mission_menu = [
    (
        InlineKeyboardButton(
            'Конечно! Расскажи подробнее!',
            callback_data=ABOUT_FUND_CALLBACKS.get('more_info_mission'),
        ),
    ),
]
fund_mission_menu.extend(navigation_menu)
fund_mission_markup = InlineKeyboardMarkup(fund_mission_menu)


things_path_menu = [
    (
        InlineKeyboardButton(
            'Да, было бы здорово посмотреть!',
            callback_data=ABOUT_FUND_CALLBACKS.get('more_info_path'),
        ),
    ),
]
things_path_menu.extend(navigation_menu)
things_path_markup = InlineKeyboardMarkup(things_path_menu)


processes_anatomy_menu = [
    (
        InlineKeyboardButton(
            'Конечно! Какие?',
            callback_data=ABOUT_FUND_CALLBACKS.get('more_info_processes'),
        ),
    ),
]
processes_anatomy_menu.extend(navigation_menu)
processes_anatomy_markup = InlineKeyboardMarkup(processes_anatomy_menu)


fund_projects_menu = [
    (
        InlineKeyboardButton(
            'Почитаю с удовольствием!',
            callback_data=ABOUT_FUND_CALLBACKS.get('more_info_projects'),
        ),
    ),
]
fund_projects_menu.extend(navigation_menu)
fund_projects_markup = InlineKeyboardMarkup(fund_projects_menu)


annual_reports_menu = [
    (
        InlineKeyboardButton(
            'Обязательно прочту!', callback_data='back_to_main_menu'
        ),
    ),
]
annual_reports_markup = InlineKeyboardMarkup(annual_reports_menu)
