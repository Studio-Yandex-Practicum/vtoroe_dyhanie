from telegram.ext import Application

from . import (
    about_fund_application,
    basic_info_application,
    command_application,
    faq_application,
    main_application,
    menu_application,
    rules_application,
)


def register_all_handlers(app: Application):
    main_application.register_handlers(app)
    menu_application.register_handlers(app)
    faq_application.register_handlers(app)
    basic_info_application.register_handlers(app)
    about_fund_application.register_handlers(app)
    command_application.register_handlers(app)
    rules_application.register_handlers(app)
