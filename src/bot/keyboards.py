from telegram import ReplyKeyboardMarkup
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
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

# 1. Клавиатура для подраздела "основная информация"
basic_information_keyboard = [
    [
        InlineKeyboardButton(
            "Организационная структура", callback_data="organization_structure"
        )
    ],
    [InlineKeyboardButton("Наша команда", callback_data="our_team")],
    [InlineKeyboardButton("График работы", callback_data="schedule")],
    [InlineKeyboardButton("Соцсети фонда", callback_data="social_networks")],
    [
        InlineKeyboardButton(
            "Вернуться в главное меню", callback_data="main_menu"
        )
    ],
]
basic_information_markup = InlineKeyboardMarkup(basic_information_keyboard)

# 2. Клавиатура для 'organization_structure'
org_structure_keyboard = [
    # Маша, нужно реализовать:
    [InlineKeyboardButton("Совет Фонда", callback_data="council")],
    # Маша, нужно реализовать:
    [
        InlineKeyboardButton(
            "Попечительский совет", callback_data="guardian_council"
        )
    ],
    # Маша, нужно реализовать:
    [InlineKeyboardButton("Отделы Фонда", callback_data="departments")],
    [InlineKeyboardButton("Назад", callback_data="basic_information_back")],
    [InlineKeyboardButton("В главное меню", callback_data="main_menu")],
]
org_structure_markup = InlineKeyboardMarkup(org_structure_keyboard)

# 3. Клавиатура для 'our_team'
our_team_keyboard = [
    # Пока ещё не реализовано и на схеме нет:
    [InlineKeyboardButton("Список контактов", callback_data="contact_list")],
    # Пока ещё не реализовано и на схеме нет:
    [InlineKeyboardButton("Отделы Фонда", callback_data="departmentss")],
    [InlineKeyboardButton("Назад", callback_data="basic_information_back")],
    [InlineKeyboardButton("В главное меню", callback_data="main_menu")],
]
our_team_markup = InlineKeyboardMarkup(our_team_keyboard)

# 4. Клавиатура для 'social_networks'
social_networks_keyboard = [
    [InlineKeyboardButton("Назад", callback_data="basic_information_back")],
    [InlineKeyboardButton("В главное меню", callback_data="main_menu")],
]
social_networks_markup = InlineKeyboardMarkup(social_networks_keyboard)
