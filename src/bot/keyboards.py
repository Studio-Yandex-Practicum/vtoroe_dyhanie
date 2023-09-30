from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup
)

from bot.constants.button import BACK_BUTTON
from bot.constants.callback import FEEDBACK_BACK_BUTTON, MAIN_MENU_BUTTON

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

faq_menu_keyboard = [
    ["Организационные вопросы", "Волонтёрство"],
    ["Обучение", "Отпуск"],
    ["Рабочий процесс", "Административные вопросы"],
    ["Оформление документов", "Командировки"],
    ["В главное меню"],
]
faq_menu_markup = ReplyKeyboardMarkup(
    faq_menu_keyboard, one_time_keyboard=False, resize_keyboard=True
)

back_button_keyboard = [
    [InlineKeyboardButton(BACK_BUTTON, callback_data=FEEDBACK_BACK_BUTTON)]
]
back_button_markup = InlineKeyboardMarkup(back_button_keyboard)

main_button_keyboard = [
    [InlineKeyboardButton(BACK_BUTTON, callback_data=MAIN_MENU_BUTTON)]
]
main_button_markup = InlineKeyboardMarkup(main_button_keyboard)
