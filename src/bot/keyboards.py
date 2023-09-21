from telegram import ReplyKeyboardMarkup


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
    ["Назад"],
]
faq_menu_markup = ReplyKeyboardMarkup(
    faq_menu_keyboard, one_time_keyboard=False, resize_keyboard=True
)
