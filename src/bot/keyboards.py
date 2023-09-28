from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup
)

from bot.constants.button import BACK_BUTTON
from bot.constants.callback import FEEDBACK_BACK_BUTTON


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

back_button_keyboard = [
    [InlineKeyboardButton(BACK_BUTTON, callback_data=FEEDBACK_BACK_BUTTON)]
]
back_button_markup = InlineKeyboardMarkup(back_button_keyboard)
