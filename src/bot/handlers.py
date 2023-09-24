from telegram.ext import (
    CallbackQueryHandler,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)

from bot.constants.state import (
    ABOUT_FUND_MENU_STATE,
    CHECK,
    FUND_MISSION_STATE,
    MENU
)
from bot.conversations.main_application import (
    greeting_callback,
    done_callback,
    check_the_secret_word_callback,
)
from bot.conversations.menu_application import (
    about_fund_callback,
    about_fund_menu_callback,
    about_fund_more_info
)

conv_handler = ConversationHandler(
    entry_points=[CommandHandler("start", greeting_callback)],
    states={
        CHECK: [
            MessageHandler(filters.TEXT, check_the_secret_word_callback),
        ],
        MENU: [
            MessageHandler(filters.Text('О Фонде'), about_fund_callback)
        ],
        ABOUT_FUND_MENU_STATE: [
            MessageHandler(filters.TEXT, about_fund_menu_callback)
        ],
        FUND_MISSION_STATE: [
            CallbackQueryHandler(about_fund_more_info)
        ]
    },
    fallbacks=[MessageHandler(filters.Regex("^Done$"), done_callback)],
)
