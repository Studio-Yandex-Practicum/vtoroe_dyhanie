from telegram import ReplyKeyboardMarkup


menu_keyboard = [
    ["О Фонде", "Онбординг"],
    ["Основная информация", "Общие правила"],
    ["База знаний", "Обратная связь"],
    ["Регламенты и формы", "FAQ"],
    ["Список контактов"],
]
menu_markup = ReplyKeyboardMarkup(
    menu_keyboard, one_time_keyboard=True, resize_keyboard=True
)
