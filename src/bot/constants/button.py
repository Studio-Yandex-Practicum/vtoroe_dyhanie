from telegram import BotCommand


MENU_ABOUT_FOND = 'О Фонде'
MENU_ONBOARDING = 'Онбординг'
MENU_BASIC_INFO = 'Основная информация'
MENU_GENERAL_RULES = 'Общие правила'
MENU_KNOWLEDGE_BASE = 'База знаний'
MENU_FEEDBACK = 'Обратная связь'
MENU_REGLAMENTS_AND_FORMS = 'Регламенты и формы'
MENU_FAQ = 'FAQ'
MENU_CONTACT_LIST = 'Список контактов'
BACK_BUTTON = 'Назад'
BACK_TO_MAIN_MENU = 'В главное меню'

START_CMD = BotCommand('/start', 'Начать работу')
STOP_CMD = BotCommand('/stop', 'Завершить работу')
HELP_CMD = BotCommand('/help', 'Написать в поддержку')
MENU_CMD = BotCommand('/menu', 'Главное меню')
