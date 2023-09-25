from telegram.ext import (
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)

from bot.constants.state import (
    CHECK,
    FAQ,
    MAIN_MENU,
)
from bot.conversations.main_application import (
    greeting_callback,
    done_callback,
    check_the_secret_word_callback,
    main_menu_actions_callback,
)
from bot.conversations.faq_application import faq_callback


conv_handler = ConversationHandler(
    entry_points=[CommandHandler("start", greeting_callback)],
    states={
        CHECK: [
            MessageHandler(filters.TEXT, check_the_secret_word_callback),
        ],
        MAIN_MENU: [
            MessageHandler(filters.Text(["FAQ"]), main_menu_actions_callback),
        ],
        FAQ: [
            MessageHandler(filters.Text(), faq_callback),
        ],
    },
    fallbacks=[MessageHandler(filters.Regex("^Done$"), done_callback)],
)
