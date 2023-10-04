from telegram.ext import Application

from . import (
    menu_application, main_application, faq_application,
    basic_info_application, about_fund_application
)


def register_all_handlers(app: Application):
    main_application.register_handlers(app)
    menu_application.register_handlers(app)
    faq_application.register_handlers(app)
    basic_info_application.register_handlers(app)
    about_fund_application.register_handlers(app)
