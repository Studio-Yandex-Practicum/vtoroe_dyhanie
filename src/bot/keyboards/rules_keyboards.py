from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from bot.constants.query_patterns import INFO_PREFIX

# 1. Клавиатура для подраздела "Общие правила"
rules_keyboard = [
    [InlineKeyboardButton(
        'Коммуникация',
        callback_data=f'{INFO_PREFIX}communication'
    )],
    [InlineKeyboardButton(
        'Мастерская',
        callback_data=f'{INFO_PREFIX}workshop'
    )],
    [InlineKeyboardButton(
        'Кухня',
        callback_data=f'{INFO_PREFIX}kitchen'
    )],
    [InlineKeyboardButton(
        'Раздельный сбор',
        callback_data=f'{INFO_PREFIX}separate_collection'
    )],
    [InlineKeyboardButton(
        'Регулярные встречи',
        callback_data=f'{INFO_PREFIX}regular_meetings'
    )],
]
rules_markup = InlineKeyboardMarkup(rules_keyboard)

# 2. Клавиатура для 'Коммуникация'
communication_keyboard = [
    [InlineKeyboardButton(
        'Внутренняя коммуникация',
        callback_data=f'{INFO_PREFIX}in_communication'
    )],
    [InlineKeyboardButton(
        'Внешняя коммуникация',
        callback_data=f'{INFO_PREFIX}out_communication'
    )],
    [InlineKeyboardButton(
        'Назад',
        callback_data='rules_back'
    )],
    [InlineKeyboardButton(
        'В главное меню',
        callback_data='back_to_main_menu'
    )],
]
communication_markup = InlineKeyboardMarkup(communication_keyboard)

# 3. Клавиатура для 'Мастерская'
workshop_keyboard = [
    [InlineKeyboardButton(
        'Назад',
        callback_data='rules_back'
    )],
    [InlineKeyboardButton(
        'В главное меню',
        callback_data='back_to_main_menu'
    )],
]
workshop_markup = InlineKeyboardMarkup(workshop_keyboard)

# 4. Клавиатура для 'Кухня'
kitchen_keyboard = [
    [InlineKeyboardButton(
        'Назад',
        callback_data='rules_back'
    )],
    [InlineKeyboardButton(
        'В главное меню',
        callback_data='back_to_main_menu'
    )],
]
kitchen_markup = InlineKeyboardMarkup(kitchen_keyboard)

# 5. Клавиатура для 'Раздельный сбор'
separate_collection_keyboard = [
    [InlineKeyboardButton(
        'Назад',
        callback_data='rules_back'
    )],
    [InlineKeyboardButton(
        'В главное меню',
        callback_data='back_to_main_menu'
    )],
]
separate_collection_markup = InlineKeyboardMarkup(separate_collection_keyboard)

# 6. Клавиатура для 'Регулярные встречи'
regular_meetings_keyboard = [
    [InlineKeyboardButton(
        'Назад',
        callback_data='rules_back'
    )],
    [InlineKeyboardButton(
        'В главное меню',
        callback_data='back_to_main_menu'
    )],
]
regular_meetings_markup = InlineKeyboardMarkup(regular_meetings_keyboard)

# 7. Клавиатура для возврата из раздела о внутренней коммуникации
in_communication_keyboard = [
    [InlineKeyboardButton(
        'Все понятно!',
        callback_data='back_to_main_menu'
    )],
    [InlineKeyboardButton(
        'Назад', callback_data=f'{INFO_PREFIX}in_communication'
    )],
]
in_communication_markup = InlineKeyboardMarkup(in_communication_keyboard)
