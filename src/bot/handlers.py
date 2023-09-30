from telegram.ext import (
    CallbackQueryHandler,
    CommandHandler,
    ConversationHandler,
    filters,
    MessageHandler,
)

from bot.constants.state import (
    ABOUT_FUND_BLOCK,
    ABOUT_FUND_MENU_STATE,
    BASIC_INFORMATION,
    CHECK,
    FAQ,
    FEEDBACK,
    MAIN_MENU,
    BASIC_INFORMATION,
    FIO,
    REG_FORMS,
)
from bot.conversations.about_fund_application import (
    about_fund_inline_btns_handler,
    about_fund_menu_callback,
)
from bot.conversations.basic_info_application import basic_information_callback
from bot.conversations.contact_list_application import (
    find_contact_by_fio,
)
from bot.conversations.faq_application import faq_callback
from bot.conversations.main_application import (
    greeting_callback,
    done_callback,
    check_the_secret_word_callback,
    main_menu_actions_callback,
)
from bot.conversations.menu_application import back_to_menu_callback


conv_handler = ConversationHandler(
    entry_points=[CommandHandler("start", greeting_callback)],
    states={
        CHECK: [
            MessageHandler(filters.TEXT, check_the_secret_word_callback),
        ],
        MAIN_MENU: [
            MessageHandler(filters.TEXT, main_menu_actions_callback),
        ],
        # Обработка команды "основная информация"
        BASIC_INFORMATION: [
            CallbackQueryHandler(basic_information_callback),
        ],
        FEEDBACK: [
            CallbackQueryHandler(back_to_menu_callback),
        ],
        ABOUT_FUND_MENU_STATE: [
            MessageHandler(filters.TEXT, about_fund_menu_callback)
        ],
        ABOUT_FUND_BLOCK: [
            CallbackQueryHandler(about_fund_inline_btns_handler)
        ],
        REG_FORMS: [
            CallbackQueryHandler(back_to_menu_callback),
        ],
        FAQ: [
            MessageHandler(filters.Text(), faq_callback),
        ],
        FIO: [
            MessageHandler(filters.TEXT, find_contact_by_fio),
        ],
    },
    fallbacks=[MessageHandler(filters.Regex("^Done$"), done_callback)],
)
