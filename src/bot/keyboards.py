from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
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

about_fund_keyboard = [
    [InlineKeyboardButton('Миссия и основная цель', callback_data='mission')],
    [InlineKeyboardButton('Путь вещей', callback_data='clothes_path')],
    [InlineKeyboardButton('Анатомия процессов', callback_data='process')],
    [InlineKeyboardButton('Годовые отчеты', callback_data='report')]
]
about_fund_markup = InlineKeyboardMarkup(about_fund_keyboard)
