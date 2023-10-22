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
            'Наставник/бадди',
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
            'Задачи наставника/Бадди при онбординге',
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

# 2. Клавиатура для 'Задачи Наставника/Бадди'
mentor_tasks_keyboard = [
    [
        InlineKeyboardButton(
            'Понятно, спасибо!', callback_data='back_to_main_menu'
        )
    ],
]
mentor_tasks_markup = InlineKeyboardMarkup(mentor_tasks_keyboard)
