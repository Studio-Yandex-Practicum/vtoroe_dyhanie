from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from bot.constants.query_patterns import INFO_PREFIX


# 1. Клавиатура для подраздела 'Онбординг'
onboarding_keyboard = [
    [InlineKeyboardButton('Новичок', callback_data=f'{INFO_PREFIX}beginner')],
    [
        InlineKeyboardButton(
            'Руководитель', callback_data=f'{INFO_PREFIX}director'
        )
    ],
    [
        InlineKeyboardButton(
            'Наставник/Бадди',
            callback_data=f'{INFO_PREFIX}mentor_or_buddy',
        )
    ],
    [InlineKeyboardButton('Назад в меню', callback_data='back_to_main_menu')],
]
onboarding_markup = InlineKeyboardMarkup(onboarding_keyboard)

# 2. Клавиатура для 'Наставник/Бадди'
mentor_keyboard = [
    [
        InlineKeyboardButton(
            'Задачи Наставника/Бадди',
            callback_data=f'{INFO_PREFIX}menor_tasks',
        )
    ],
    [
        InlineKeyboardButton(
            'Ой, мне не сюда', callback_data='back_to_main_menu'
        )
    ],
]
mentor_markup = InlineKeyboardMarkup(mentor_keyboard)

# 3. Клавиатура для 'Задачи Наставника/Бадди'
mentor_tasks_keyboard = [
    [
        InlineKeyboardButton(
            'Понятно, спасибо!', callback_data='back_to_main_menu'
        )
    ],
]
mentor_tasks_markup = InlineKeyboardMarkup(mentor_tasks_keyboard)

# 4. Клавиатура для 'Новичка'
beginner_keyboard = [
    [
        InlineKeyboardButton(
            'Ой, мне не сюда', callback_data='back_to_main_menu'
        )
    ],
]
beginner_markup = InlineKeyboardMarkup(beginner_keyboard)

# 5. Клавиатура после турдоустройства 'Новичка'
beginner_employment_keyboard = [
    [
        InlineKeyboardButton(
            'Первый день',
            callback_data=f'{INFO_PREFIX}first_day',
        )
    ],
    [
        InlineKeyboardButton(
            'Этапы адаптации',
            callback_data=f'{INFO_PREFIX}adaptation',
        )
    ],
    [
        InlineKeyboardButton(
            'План работы на испытательный срок',
            callback_data=f'{INFO_PREFIX}work_plan',
        )
    ],
    [
        InlineKeyboardButton(
            'Чек-лист нового сотрудника',
            callback_data=f'{INFO_PREFIX}checklist',
        )
    ],
]
beginner_employment_markup = InlineKeyboardMarkup(beginner_employment_keyboard)

# общая часть меню раздела Новичок
navigation_menu = [
    (
        InlineKeyboardButton(
            'Назад',
            callback_data='beginner_back',
        ),
    ),
    (
        InlineKeyboardButton(
            'В главное меню',
            callback_data='back_to_main_menu',
        ),
    ),
]

# 6. Клавиатура для выхода из раздела 'Первый день'
first_day_keyboard = [
    [
        InlineKeyboardButton(
            'Да, нужен чек-лист, спасибо!',
            callback_data=f'{INFO_PREFIX}checklist',
        )
    ],
]
first_day_keyboard.extend(navigation_menu)
first_day_markup = InlineKeyboardMarkup(first_day_keyboard)

# 7. Клавиатура для выхода из раздела 'Этапы адаптации'
adaptation_keyboard = [
    [
        InlineKeyboardButton(
            'Да, давай!', callback_data=f'{INFO_PREFIX}work_plan'
        )
    ],
]
adaptation_keyboard.extend(navigation_menu)
adaptation_markup = InlineKeyboardMarkup(adaptation_keyboard)

# 8. Клавиатура для выхода из раздела 'План работы на испытательный срок'
work_plan_keyboard = [
    [
        InlineKeyboardButton(
            'Все ясно, спасибо',
            # на схеме нет
            callback_data='back_to_main_menu',
        )
    ],
    [
        InlineKeyboardButton(
            'Назад',
            callback_data='beginner_back',
        )
    ],
]
work_plan_markup = InlineKeyboardMarkup(work_plan_keyboard)

# 9. Клавиатура для выхода из раздела 'Чек лист нового сотрудника'
checklist_keyboard = [
    [
        InlineKeyboardButton(
            'То, что нужно! Спасибо!',
            # на схеме нет
            callback_data='back_to_main_menu',
        )
    ],
    [
        InlineKeyboardButton(
            'Назад',
            callback_data='beginner_back',
        )
    ],
]
checklist_markup = InlineKeyboardMarkup(checklist_keyboard)


# 10. Клавиатура для 'Руководитель'
director_keyboard = [
    # Расходится со схемой - такое меню показалось логичней
    [
        InlineKeyboardButton(
            'Супер, давай!',
            callback_data=f'{INFO_PREFIX}director_confirmation',
        )
    ],
    [
        InlineKeyboardButton(
            'Что за встречи?',
            callback_data=f'{INFO_PREFIX}director_question',
        )
    ],
    [
        InlineKeyboardButton(
            'Задачи руководителя',
            callback_data=f'{INFO_PREFIX}director_tasks',
        )
    ],
    [
        InlineKeyboardButton(
            'Ой, мне не сюда', callback_data='back_to_main_menu'
        )
    ],
]
director_markup = InlineKeyboardMarkup(director_keyboard)

# 11. Клавиатура для 'Задачи Руководителя'
director_tasks_keyboard = [
    [InlineKeyboardButton('Ок, спасибо!', callback_data='back_to_main_menu')],
]
director_tasks_markup = InlineKeyboardMarkup(director_tasks_keyboard)

# 12. Клавиатура для возврата из раздела 'Что за встречи'
director_question_keyboard = [
    [
        InlineKeyboardButton(
            'Ясно, спасибо!', callback_data='back_to_main_menu'
        )
    ],
]
director_question_markup = InlineKeyboardMarkup(director_question_keyboard)

# 13. Клавиатура для возврата из раздела 'Супер, давай'
director_confirm_keyboard = [
    [InlineKeyboardButton('Назад', callback_data='back_to_main_menu')],
]
director_confirm_markup = InlineKeyboardMarkup(director_confirm_keyboard)

# 14. Клавиатура с вариантами ответов
# после сообщения BEGINNER_AFTER_25_DAY_MESSAGE
feedback_keyboard = [
    [
        InlineKeyboardButton(
            'Все отлично!', callback_data='feedback_great'
        )
    ],
    [
        InlineKeyboardButton(
            '50/50', callback_data='feedback_so_so'
        )
    ],
    [
        InlineKeyboardButton(
            'Не все гладко, help', callback_data='feedback_help'
        )
    ],
]
feedback_keyboard_markup = InlineKeyboardMarkup(feedback_keyboard)

# 15. Клавиатура с вариантами ответов
# после сообщения BEGINNER_DEFERRED_MESSAGES_VARIANTS
calendar_keyboard = [
    [
        InlineKeyboardButton(
            'Да все в календаре', callback_data='calendar_yes'
        )
    ],
    [
        InlineKeyboardButton(
            'Еще не успел', callback_data='calendar_no'
        )
    ],
]
calendar_keyboard_markup = InlineKeyboardMarkup(calendar_keyboard)

# 16. Клавиатура "Ок, спасибо"
thanks_keyboard = [
    [
        InlineKeyboardButton(
            'Ясно, спасибо!', callback_data='back_to_main_menu'
        )
    ],
]
thanks_markup = InlineKeyboardMarkup(thanks_keyboard)
