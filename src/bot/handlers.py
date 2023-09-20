from telegram.ext import (
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)

from bot.constants.state import CHECK
from bot.conversations.main_application import (
    greeting_callback,
    done_callback,
    check_the_secret_word_callback,
)

conv_handler = ConversationHandler(
    entry_points=[CommandHandler("start", greeting_callback)],
    states={
        CHECK: [
            MessageHandler(filters.TEXT, check_the_secret_word_callback),
        ],
    },
    fallbacks=[MessageHandler(filters.Regex("^Done$"), done_callback)],
)


reg_form_handler = MessageHandler(
    filters.Text(['Регламенты и формы']),
    reg_form_callback
)
