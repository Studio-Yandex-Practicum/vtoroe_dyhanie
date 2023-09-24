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
    [InlineKeyboardButton("Совет Фонда", callback_data="council")],
    [
        InlineKeyboardButton(
            "Попечительский совет", callback_data="guardian_council"
        )
    ],
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

# 5. Клавиатура для 'council'
council_keyboard = [
    [InlineKeyboardButton(
        "За что отвечает Совет фонда?",
        callback_data="council_question_01"
    )],
    [InlineKeyboardButton(
        "Что делает Совет фонда?",
        callback_data="council_question_02"
    )],
    [InlineKeyboardButton(
        "Как связаны Директор и Совет фонда?",
        callback_data="council_question_03"
    )],
    [InlineKeyboardButton(
        "В чем различие между Директором фонда и Председателем Совета?"
        "Кто 'главнее'?",
        callback_data="council_question_04"
    )],
    [InlineKeyboardButton(
        "Как формировался Совет фонда?",
        callback_data="council_question_05"
    )],
    [InlineKeyboardButton(
        "Чем занимается Попечительский Совет фонда?",
        callback_data="council_question_06")],
    [InlineKeyboardButton(
        "Назад",
        callback_data="basic_information_back")],
    [InlineKeyboardButton(
        "В главное меню",
        callback_data="main_menu")],
]
council_markup = InlineKeyboardMarkup(council_keyboard)

# 6. Клавиатура для возвратов из раздела о департаментах
departments_final_keyboard = [
    [InlineKeyboardButton("Понятно, спасибо!", callback_data="main_menu")],
    [InlineKeyboardButton("Назад", callback_data="departments")],
]
departments_final_markup = InlineKeyboardMarkup(departments_final_keyboard)

# 7. Клавиатура для 'departments'
departments_keyboard = [
    [InlineKeyboardButton(
        "Отдел благотворительных программ",
        callback_data="department_01"
    )],
    [InlineKeyboardButton(
        "Отдел информационных программ",
        callback_data="department_02"
    )],
    [InlineKeyboardButton(
        "Центр сортировки г. Москва",
        callback_data="department_03"
    )],
    [InlineKeyboardButton(
        "Центр сортировки и переработки г. Кострома",
        callback_data="department_04"
    )],
    [InlineKeyboardButton(
        "Центр гуманитарной помощи г. Кострома",
        callback_data="department_05"
    )],
    [InlineKeyboardButton(
        "Отдел по работе с партнёрами",
        callback_data="department_06"
    )],
    [InlineKeyboardButton(
        "Отдел коммуникаций",
        callback_data="department_07"
    )],
    [InlineKeyboardButton(
        "Финансово-административный отдел/Административный отдел",
        callback_data="department_08"
    )],
    [InlineKeyboardButton(
        "Мастерская г. Москва",
        callback_data="department_09"
    )],
    [InlineKeyboardButton(
        "Отдел управления персоналом",
        callback_data="department_10"
    )],
]
departments_markup = InlineKeyboardMarkup(departments_keyboard)

# 8. Клавиатура для 'guardian_council'
guardian_council_keyboard = [
    [InlineKeyboardButton("Понятно, спасибо!", callback_data="main_menu")],
    [InlineKeyboardButton("Назад", callback_data="organization_structure")],
]
guardian_council_markup = InlineKeyboardMarkup(guardian_council_keyboard)
