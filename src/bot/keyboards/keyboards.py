from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
)

from bot.constants.button import BACK_BUTTON


main_menu_keyboard = [
    ['О Фонде', 'Онбординг'],
    ['Основная информация', 'Общие правила'],
    ['База знаний', 'Обратная связь'],
    ['Регламенты и формы', 'FAQ'],
    ['Список контактов'],
]

main_menu_markup = ReplyKeyboardMarkup(
    main_menu_keyboard, one_time_keyboard=True, resize_keyboard=True
)

faq_menu_keyboard = [
    ['Организационные вопросы', 'Волонтёрство'],
    ['Обучение', 'Отпуск'],
    ['Рабочий процесс', 'Административные вопросы'],
    ['Оформление документов', 'Командировки'],
    ['В главное меню'],
]
faq_menu_markup = ReplyKeyboardMarkup(
    faq_menu_keyboard, one_time_keyboard=False, resize_keyboard=True
)

main_button_keyboard = [
    [InlineKeyboardButton(BACK_BUTTON, callback_data='back_to_main_menu')]
]

main_button_markup = InlineKeyboardMarkup(main_button_keyboard)
