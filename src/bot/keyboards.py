from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup
)

from bot.constants.callback import (
    ABOUT_FUND_CALLBACKS
)


main_menu_keyboard = [
    ["О Фонде", "Онбординг"],
    ["Основная информация", "Общие правила"],
    ["База знаний", "Обратная связь"],
    ["Регламенты и формы", "FAQ"],
    ["Список контактов"],
]
main_menu_markup = ReplyKeyboardMarkup(
    main_menu_keyboard, one_time_keyboard=True, resize_keyboard=True
)


about_fund_section = {
    'mission': 'Миссия и основная цель',
    'things_path': 'Путь вещей',
    'processes_anatomy': 'Анатомия процессов',
    'fund_projects': 'Проекты Фонда',
    'annual_reports': 'Годовые отчеты'
}

about_fund_keyboard = [
    (about_fund_section.get('mission'),),
    (about_fund_section.get('things_path'),),
    (about_fund_section.get('processes_anatomy'),),
    (about_fund_section.get('fund_projects'),),
    (about_fund_section.get('annual_reports'),)
]
about_fund_markup = ReplyKeyboardMarkup(
    about_fund_keyboard,
    resize_keyboard=True,
    one_time_keyboard=True
)

navigation_menu = [
    (InlineKeyboardButton(
        'В меню раздела',
        callback_data=ABOUT_FUND_CALLBACKS.get('back_to_menu')
    ),),
    (InlineKeyboardButton(
        'В главное меню',
        callback_data=ABOUT_FUND_CALLBACKS.get('back_to_main_menu')
    ),)
]

fund_history_menu = [
    (InlineKeyboardButton(
        'Конечно! Расскажи подробнее!',
        callback_data=ABOUT_FUND_CALLBACKS.get('more_info')
    ),),
]
fund_history_menu.extend(navigation_menu)
fund_history_markup = InlineKeyboardMarkup(fund_history_menu)

things_path_menu = [
    (InlineKeyboardButton(
        'Да, было бы здорово посмотреть!',
        callback_data=ABOUT_FUND_CALLBACKS.get('more_info')
    ),),
]
things_path_menu.extend(navigation_menu)
things_path_markup = InlineKeyboardMarkup(things_path_menu)

processes_anatomy_menu = [
    (InlineKeyboardButton(
        'Конечно! Какие?',
        callback_data=ABOUT_FUND_CALLBACKS.get('more_info')
    ),),
]
processes_anatomy_menu.extend(navigation_menu)
processes_anatomy_markup = InlineKeyboardMarkup(
    processes_anatomy_menu
)

fund_projects_menu = [
    (InlineKeyboardButton(
        'Почитаю с удовольствием!',
        callback_data=ABOUT_FUND_CALLBACKS.get('more_info')
    ),),
]
fund_projects_menu.extend(navigation_menu)
fund_projects_markup = InlineKeyboardMarkup(
    fund_projects_menu
)

annual_reports_menu = [
    (InlineKeyboardButton(
        'Обязательно прочту!',
        callback_data=ABOUT_FUND_CALLBACKS.get('more_info')
    ),),
]
annual_reports_markup = InlineKeyboardMarkup(
    annual_reports_menu
)
