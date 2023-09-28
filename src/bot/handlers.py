from telegram.ext import (
    CallbackQueryHandler,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)

from bot.constants.state import (
    ABOUT_FUND_BLOCK,
    ABOUT_FUND_MENU_STATE,
    CHECK,
    MAIN_MENU
)
from bot.conversations.main_application import (
    greeting_callback,
    done_callback,
    check_the_secret_word_callback,
    main_menu_actions_callback,
)
from bot.conversations.about_fund_application import (
    about_fund_inline_btns_handler,
    about_fund_menu_callback
)

conv_handler = ConversationHandler(
    entry_points=[CommandHandler("start", greeting_callback)],
    states={
        CHECK: [
            MessageHandler(filters.TEXT, check_the_secret_word_callback),
        ],
        MAIN_MENU: [
            MessageHandler(filters.TEXT, main_menu_actions_callback)
        ],
        ABOUT_FUND_MENU_STATE: [
            MessageHandler(filters.TEXT, about_fund_menu_callback)
        ],
        ABOUT_FUND_BLOCK: [
            CallbackQueryHandler(about_fund_inline_btns_handler)
        ],
    },
    fallbacks=[MessageHandler(filters.Regex("^Done$"), done_callback)],
)
