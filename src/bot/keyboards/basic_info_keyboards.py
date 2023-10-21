from copy import deepcopy

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from bot.constants.query_patterns import INFO_PREFIX


# 1. Клавиатура для подраздела "основная информация"
basic_information_keyboard = [
    [
        InlineKeyboardButton(
            'Организационная структура',
            callback_data=f'{INFO_PREFIX}organization_structure',
        )
    ],
    [
        InlineKeyboardButton(
            'Наша команда', callback_data=f'{INFO_PREFIX}our_team'
        )
    ],
    [
        InlineKeyboardButton(
            'Соцсети Фонда', callback_data=f'{INFO_PREFIX}social_networks'
        )
    ],
    [
        InlineKeyboardButton(
            'Вернуться в главное меню', callback_data='back_to_main_menu'
        )
    ],
]
basic_information_markup = InlineKeyboardMarkup(basic_information_keyboard)

# 2. Клавиатура для 'organization_structure'
org_structure_keyboard = [
    [
        InlineKeyboardButton(
            'Совет Фонда', callback_data=f'{INFO_PREFIX}council'
        )
    ],
    [
        InlineKeyboardButton(
            'Попечительский совет',
            callback_data=f'{INFO_PREFIX}guardian_council',
        )
    ],
    [
        InlineKeyboardButton(
            'Отделы Фонда', callback_data=f'{INFO_PREFIX}about_departments'
        )
    ],
    [InlineKeyboardButton('Назад', callback_data='basic_information_back')],
    [
        InlineKeyboardButton(
            'В главное меню', callback_data='back_to_main_menu'
        )
    ],
]
org_structure_markup = InlineKeyboardMarkup(org_structure_keyboard)

# 3. Клавиатура для 'our_team'
our_team_keyboard = [
    # Пока ещё не реализовано и на схеме нет:
    [
        InlineKeyboardButton(
            'Список контактов', callback_data=f'{INFO_PREFIX}contact_list'
        )
    ],
    [
        InlineKeyboardButton(
            'Отделы Фонда', callback_data=f'{INFO_PREFIX}org_departmentss'
        )
    ],
    [InlineKeyboardButton('Назад', callback_data='basic_information_back')],
    # На схеме этой кнопки нет, но она мне кажется логичной
    [
        InlineKeyboardButton(
            'В главное меню', callback_data='back_to_main_menu'
        )
    ],
]
our_team_markup = InlineKeyboardMarkup(our_team_keyboard)

# 4. Клавиатура для 'social_networks'
social_networks_keyboard = [
    [
        InlineKeyboardButton(
            'Спасибо, изучу!', callback_data='basic_information_back'
        )
    ],
    [
        InlineKeyboardButton(
            'В главное меню', callback_data='back_to_main_menu'
        )
    ],
]
social_networks_markup = InlineKeyboardMarkup(social_networks_keyboard)

# 5. Клавиатура для 'council'
council_keyboard = [
    [
        InlineKeyboardButton(
            'За что отвечает Совет Фонда?',
            callback_data=f'{INFO_PREFIX}council_question_01',
        )
    ],
    [
        InlineKeyboardButton(
            'Что делает Совет Фонда?',
            callback_data=f'{INFO_PREFIX}council_question_02',
        )
    ],
    [
        InlineKeyboardButton(
            'Как связаны Директор и Совет Фонда?',
            callback_data=f'{INFO_PREFIX}council_question_03',
        )
    ],
    [
        InlineKeyboardButton(
            'В чем различие между директором Фонда и Председателем Совета?'
            'Кто "главнее"?',
            callback_data=f'{INFO_PREFIX}council_question_04',
        )
    ],
    [
        InlineKeyboardButton(
            'Как формировался Совет фонда?',
            callback_data=f'{INFO_PREFIX}council_question_05',
        )
    ],
    [
        InlineKeyboardButton(
            'Чем занимается Попечительский Совет Фонда?',
            callback_data=f'{INFO_PREFIX}council_question_06',
        )
    ],
    [
        InlineKeyboardButton(
            'Назад', callback_data=f'{INFO_PREFIX}organization_structure'
        )
    ],
    [
        InlineKeyboardButton(
            'В главное меню', callback_data='back_to_main_menu'
        )
    ],
]
council_markup = InlineKeyboardMarkup(council_keyboard)

# 6. Клавиатура для возвратов из раздела о департаментах
departments_final_keyboard = [
    [
        InlineKeyboardButton(
            'Понятно, спасибо!', callback_data='back_to_main_menu'
        )
    ],
    [
        InlineKeyboardButton(
            'Назад', callback_data=f'{INFO_PREFIX}about_departments'
        )
    ],
]
departments_final_markup = InlineKeyboardMarkup(departments_final_keyboard)

# 7. Клавиатура для 'departments'
departments_keyboard_base = [
    [
        InlineKeyboardButton(
            'Отдел благотворительных программ',
            callback_data=f'{INFO_PREFIX}department_01',
        )
    ],
    [
        InlineKeyboardButton(
            'Отдел информационных программ',
            callback_data=f'{INFO_PREFIX}department_02',
        )
    ],
    [
        InlineKeyboardButton(
            'Центр сортировки г. Москва',
            callback_data=f'{INFO_PREFIX}department_03',
        )
    ],
    [
        InlineKeyboardButton(
            'Центр сортировки и переработки г. Кострома',
            callback_data=f'{INFO_PREFIX}department_04',
        )
    ],
    [
        InlineKeyboardButton(
            'Центр гуманитарной помощи г. Кострома',
            callback_data=f'{INFO_PREFIX}department_05',
        )
    ],
    [
        InlineKeyboardButton(
            'Отдел по работе с партнёрами',
            callback_data=f'{INFO_PREFIX}department_06',
        )
    ],
    [
        InlineKeyboardButton(
            'Отдел коммуникаций',
            callback_data=f'{INFO_PREFIX}department_07',
        )
    ],
    [
        InlineKeyboardButton(
            'Финансово-административный отдел/Административный отдел',
            callback_data=f'{INFO_PREFIX}department_08',
        )
    ],
    [
        InlineKeyboardButton(
            'Мастерская г. Москва',
            callback_data=f'{INFO_PREFIX}department_09',
        )
    ],
    [
        InlineKeyboardButton(
            'Отдел управления персоналом',
            callback_data=f'{INFO_PREFIX}department_10',
        )
    ],
]
departments_keyboard = deepcopy(departments_keyboard_base)
departments_keyboard.extend(
    [
        [
            InlineKeyboardButton(
                'Назад', callback_data=f'{INFO_PREFIX}organization_structure'
            )
        ],
        [
            InlineKeyboardButton(
                'В главное меню', callback_data='back_to_main_menu'
            )
        ],
    ]
)
departments_markup = InlineKeyboardMarkup(departments_keyboard)

# 7.5. Клавиатура для 'departmentss'
departmentss_keyboard = deepcopy(departments_keyboard_base)
departmentss_keyboard.extend(
    [
        [
            InlineKeyboardButton(
                'Назад', callback_data=f'{INFO_PREFIX}our_team'
            )
        ],
        [
            InlineKeyboardButton(
                'В главное меню', callback_data='back_to_main_menu'
            )
        ],
    ]
)
departmentss_markup = InlineKeyboardMarkup(departmentss_keyboard)

# 8. Клавиатура для 'guardian_council'
guardian_council_keyboard = [
    [
        InlineKeyboardButton(
            'Понятно, спасибо!',
            callback_data=f'{INFO_PREFIX}organization_structure',
        )
    ],
]
guardian_council_markup = InlineKeyboardMarkup(guardian_council_keyboard)

# 9. Клавиатура для 'contact_list'
contact_list_keyboard = [
    (
        InlineKeyboardButton(
            'Скачать справочник',
            url='https://docs.google.com/spreadsheets/d/'
            '1m_y8rtod0VEGBAmhmqxK3ax-ulOUfeJNlvMApluhBFM/edit',
        ),
    ),
]
contact_list_markup = InlineKeyboardMarkup(contact_list_keyboard)
