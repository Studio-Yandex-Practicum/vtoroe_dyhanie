from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup
)

from bot.constants.callback import (
    FUND_HISTORY_CALLBACKS
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
    'annual_reports': 'Годовые отчеты'
}

about_fund_keyboard = [
    (about_fund_section.get('mission'),),
    (about_fund_section.get('things_path'),),
    (about_fund_section.get('processes_anatomy'),),
    (about_fund_section.get('annual_reports'),)
]
about_fund_markup = ReplyKeyboardMarkup(about_fund_keyboard)

fund_history_menu = [
    (InlineKeyboardButton(
        'Конечно! Расскажи подробнее!',
        callback_data=FUND_HISTORY_CALLBACKS.get('more_info')
    ),),
    (InlineKeyboardButton(
        'В меню раздела',
        callback_data=FUND_HISTORY_CALLBACKS.get('back_to_menu')
    ),),
    (InlineKeyboardButton(
        'В главное меню',
        callback_data=FUND_HISTORY_CALLBACKS.get('back_to_main_menu')
    ),)
]
fund_history_markup = InlineKeyboardMarkup(fund_history_menu)
