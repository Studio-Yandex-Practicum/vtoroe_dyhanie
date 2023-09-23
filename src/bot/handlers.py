from telegram.ext import (
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)

from bot.constants.state import CHECK, MENU
from bot.conversations.main_application import (
    greeting_callback,
    done_callback,
    check_the_secret_word_callback,
)
from bot.conversations.menu_application import feedback_callback


conv_handler = ConversationHandler(
    entry_points=[CommandHandler("start", greeting_callback)],
    states={
        CHECK: [
            MessageHandler(filters.TEXT, check_the_secret_word_callback),
        ],
        MENU: [
            MessageHandler(
                filters.Text('Обратная связь'),
                feedback_callback
            ),
        ]
    },
    fallbacks=[MessageHandler(filters.Regex("^Done$"), done_callback)],
)
