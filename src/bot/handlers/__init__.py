import threading
import time

from telegram.ext import Application

from . import (
    about_fund_application,
    basic_info_application,
    command_application,
    faq_application,
    main_application,
    menu_application,
    onboarding_application,
    rules_application,
)


# interval через какой промежуток времени идёт перрегистрация всех хэндлеров
# для обновления значений взятых из БД
def update_handlers_periodically(app: Application, interval=5):
    while True:
        try:
            register_all_handlers(app)
            time.sleep(interval)
        except Exception as e:
            print(f"Ошибка при обновлении обработчиков: {e}")


def register_all_handlers(app: Application):
    main_application.register_handlers(app)
    menu_application.register_handlers(app)
    faq_application.register_handlers(app)
    basic_info_application.register_handlers(app)
    about_fund_application.register_handlers(app)
    command_application.register_handlers(app)
    rules_application.register_handlers(app)
    onboarding_application.register_handlers(app)


# запуск регистрации хэндлеров в отдельном потоке
def start_handler_updater_thread(app):
    updater_thread = threading.Thread(
        target=update_handlers_periodically, args=(app,))
    updater_thread.daemon = True
    updater_thread.start()
