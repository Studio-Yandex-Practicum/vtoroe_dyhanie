from telegram.ext import (
    CommandHandler,
    ConversationHandler,
    filters,
    MessageHandler
)

from bot.constants.state import CHECK, MENU
from bot.conversations.main_application import (
    check_the_secret_word_callback,
    done_callback,
    greeting_callback
)
from bot.conversations.menu_application import reg_form_callback

conv_handler = ConversationHandler(
    entry_points=[CommandHandler("start", greeting_callback)],
    states={
        CHECK: [
            MessageHandler(filters.TEXT, check_the_secret_word_callback),
        ],
        MENU: [
            MessageHandler(
                filters.Text(['Регламенты и формы']),
                reg_form_callback
                ),
        ],
    },
    fallbacks=[MessageHandler(filters.Regex("^Done$"), done_callback)],
)
