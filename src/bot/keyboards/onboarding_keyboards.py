from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from bot.constants.query_patterns import INFO_PREFIX
from bot.utils.admin_api import get_django_json


# 1. Клавиатура для подраздела "Онбординг"
async def onboarding_markup():
    messages = await get_django_json(
        'http://127.0.0.1:8000/onboarding_keyboards/1:4/'
    )
    onboarding_keyboard = [
        [
            InlineKeyboardButton(
                messages['onboarding_keyboard_beginner'],
                callback_data=f'{INFO_PREFIX}beginner',
            )
        ],
        [
            InlineKeyboardButton(
                messages['onboarding_keyboard_director'],
                callback_data=f'{INFO_PREFIX}director',
            )
        ],
        [
            InlineKeyboardButton(
                messages['onboarding_keyboard_mentor_or_buddy'],
                callback_data=f'{INFO_PREFIX}mentor_or_buddy',
            )
        ],
        [
            InlineKeyboardButton(
                messages['onboarding_keyboard_back_to_main_menu'],
                callback_data='back_to_main_menu',
            )
        ],
    ]
    return InlineKeyboardMarkup(onboarding_keyboard)


# 2. Клавиатура для "Наставник/Бадди"
async def mentor_markup():
    messages = await get_django_json(
        'http://127.0.0.1:8000/onboarding_keyboards/5:6/'
    )
    mentor_keyboard = [
        [
            InlineKeyboardButton(
                messages['mentor_keyboard_menor_tasks'],
                callback_data=f'{INFO_PREFIX}menor_tasks',
            )
        ],
        [
            InlineKeyboardButton(
                messages['mentor_keyboard_back_to_main_menu'],
                callback_data='back_to_main_menu',
            )
        ],
    ]
    return InlineKeyboardMarkup(mentor_keyboard)


# 3. Клавиатура для "Задачи Наставника/Бадди"
async def mentor_tasks_markup():
    messages = await get_django_json(
        'http://127.0.0.1:8000/onboarding_keyboards/7/'
    )
    mentor_tasks_keyboard = [
        [
            InlineKeyboardButton(
                messages['mentor_tasks_keyboard_back_to_main_menu'],
                callback_data='back_to_main_menu',
            )
        ],
    ]
    return InlineKeyboardMarkup(mentor_tasks_keyboard)


# 4. Клавиатура для 'Новичка'
async def beginner_markup():
    messages = await get_django_json(
        'http://127.0.0.1:8000/onboarding_keyboards/8/'
    )
    beginner_keyboard = [
        [
            InlineKeyboardButton(
                messages['beginner_keyboard_back_to_main_menu'],
                callback_data='back_to_main_menu',
            )
        ],
    ]
    return InlineKeyboardMarkup(beginner_keyboard)


# 5. Клавиатура после турдоустройства 'Новичка'
async def beginner_employment_markup():
    messages = await get_django_json(
        'http://127.0.0.1:8000/onboarding_keyboards/9:12/'
    )
    beginner_employment_keyboard = [
        [
            InlineKeyboardButton(
                messages['beginner_employment_keyboard_first_day'],
                callback_data=f'{INFO_PREFIX}first_day',
            )
        ],
        [
            InlineKeyboardButton(
                messages['beginner_employment_keyboard_adaptation'],
                callback_data=f'{INFO_PREFIX}adaptation',
            )
        ],
        [
            InlineKeyboardButton(
                messages['beginner_employment_keyboard_work_plan'],
                callback_data=f'{INFO_PREFIX}work_plan',
            )
        ],
        [
            InlineKeyboardButton(
                messages['beginner_employment_keyboard_checklist'],
                callback_data=f'{INFO_PREFIX}checklist',
            )
        ],
    ]
    return InlineKeyboardMarkup(beginner_employment_keyboard)


# 6. Клавиатура для выхода из раздела 'Первый день'
async def first_day_markup():
    messages = await get_django_json(
        'http://127.0.0.1:8000/onboarding_keyboards/13:15/'
    )
    first_day_keyboard = [
        [
            InlineKeyboardButton(
                messages['first_day_keyboard_checklist'],
                callback_data=f'{INFO_PREFIX}checklist',
            )
        ],
        [
            InlineKeyboardButton(
                messages['navigation_menu_beginner_back'],
                callback_data='beginner_back',
            ),
        ],
        [
            InlineKeyboardButton(
                messages['navigation_menu_back_to_main_menu'],
                callback_data='back_to_main_menu',
            ),
        ],
    ]
    return InlineKeyboardMarkup(first_day_keyboard)


# 7. Клавиатура для выхода из раздела 'Этапы адаптации'
async def adaptation_markup():
    messages = await get_django_json(
        'http://127.0.0.1:8000/onboarding_keyboards/'
    )
    adaptation_keyboard = [
        [
            InlineKeyboardButton(
                messages['adaptation_keyboard_work_plan'],
                callback_data=f'{INFO_PREFIX}work_plan',
            )
        ],
        [
            InlineKeyboardButton(
                messages['navigation_menu_beginner_back'],
                callback_data='beginner_back',
            ),
        ],
        [
            InlineKeyboardButton(
                messages['navigation_menu_back_to_main_menu'],
                callback_data='back_to_main_menu',
            ),
        ],
    ]
    return InlineKeyboardMarkup(adaptation_keyboard)


# 8. Клавиатура для выхода из раздела 'План работы на испытательный срок'
async def work_plan_markup():
    messages = await get_django_json(
        'http://127.0.0.1:8000/onboarding_keyboards/17:18/'
    )
    work_plan_keyboard = [
        [
            InlineKeyboardButton(
                messages['work_plan_keyboard_back_to_main_menu'],
                # на схеме нет
                callback_data='back_to_main_menu',
            )
        ],
        [
            InlineKeyboardButton(
                messages['work_plan_keyboard_beginner_back'],
                callback_data='beginner_back',
            )
        ],
    ]
    return InlineKeyboardMarkup(work_plan_keyboard)


# 9. Клавиатура для выхода из раздела 'Чек лист нового сотрудника'
async def checklist_markup():
    messages = await get_django_json(
        'http://127.0.0.1:8000/onboarding_keyboards/19:20/'
    )
    checklist_keyboard = [
        [
            InlineKeyboardButton(
                messages['checklist_keyboard_back_to_main_menu'],
                # на схеме нет
                callback_data='back_to_main_menu',
            )
        ],
        [
            InlineKeyboardButton(
                messages['checklist_keyboard_beginner_back'],
                callback_data='beginner_back',
            )
        ],
    ]
    return InlineKeyboardMarkup(checklist_keyboard)


# 10. Клавиатура для 'Руководитель'
async def director_markup():
    messages = await get_django_json(
        'http://127.0.0.1:8000/onboarding_keyboards/21:24/'
    )
    director_keyboard = [
        [
            InlineKeyboardButton(
                messages['director_keyboard_director_confirmation'],
                callback_data=f'{INFO_PREFIX}director_confirmation',
            )
        ],
        [
            InlineKeyboardButton(
                messages['director_keyboard_director_question'],
                callback_data=f'{INFO_PREFIX}director_question',
            )
        ],
        [
            InlineKeyboardButton(
                messages['director_keyboard_director_tasks'],
                callback_data=f'{INFO_PREFIX}director_tasks',
            )
        ],
        [
            InlineKeyboardButton(
                messages['director_keyboard_back_to_main_menu'],
                callback_data='back_to_main_menu',
            )
        ],
    ]
    return InlineKeyboardMarkup(director_keyboard)


# 11. Клавиатура для 'Задачи Руководителя'
async def director_tasks_markup():
    messages = await get_django_json(
        'http://127.0.0.1:8000/onboarding_keyboards/25/'
    )
    director_tasks_keyboard = [
        [
            InlineKeyboardButton(
                messages['director_tasks_keyboard_back_to_main_menu'],
                callback_data='back_to_main_menu',
            )
        ],
    ]
    return InlineKeyboardMarkup(director_tasks_keyboard)


# 12. Клавиатура для возврата из раздела 'Что за встречи'
async def director_question_markup():
    messages = await get_django_json(
        'http://127.0.0.1:8000/onboarding_keyboards/26/'
    )
    director_question_keyboard = [
        [
            InlineKeyboardButton(
                messages['director_question_keyboard_back_to_main_menu'],
                callback_data='back_to_main_menu',
            )
        ],
    ]
    return InlineKeyboardMarkup(director_question_keyboard)


# 13. Клавиатура для возврата из раздела 'Супер, давай'
async def director_confirm_markup():
    messages = await get_django_json(
        'http://127.0.0.1:8000/onboarding_keyboards/27/'
    )
    director_confirm_keyboard = [
        [
            InlineKeyboardButton(
                messages['director_confirm_keyboard_back_to_main_menu'],
                callback_data='back_to_main_menu',
            )
        ],
    ]
    return InlineKeyboardMarkup(director_confirm_keyboard)


# 14. Клавиатура с вариантами ответов
# после сообщения BEGINNER_AFTER_25_DAY_MESSAGE
feedback_keyboard = [
    [InlineKeyboardButton('Все отлично!', callback_data='feedback_great')],
    [InlineKeyboardButton('50/50', callback_data='feedback_so_so')],
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
    [InlineKeyboardButton('Да все в календаре', callback_data='calendar_yes')],
    [InlineKeyboardButton('Еще не успел', callback_data='calendar_no')],
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
