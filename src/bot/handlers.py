from telegram.ext import (
    CallbackQueryHandler,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)

from bot.constants.state import CHECK, MAIN_MENU, FEEDBACK
from bot.conversations.main_application import (
    greeting_callback,
    done_callback,
    check_the_secret_word_callback,
    main_menu_actions_callback
)
from bot.conversations.menu_application import (
    back_to_menu_callback
)


conv_handler = ConversationHandler(
    entry_points=[CommandHandler("start", greeting_callback)],
    states={
        CHECK: [
            MessageHandler(filters.TEXT, check_the_secret_word_callback),
        ],
        MAIN_MENU: [
            MessageHandler(filters.TEXT, main_menu_actions_callback),
        ],
        FEEDBACK: [
            CallbackQueryHandler(
                callback=back_to_menu_callback,
            ),
        ]
    },
    fallbacks=[MessageHandler(filters.Regex("^Done$"), done_callback)],
)
