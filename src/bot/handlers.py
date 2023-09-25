from telegram.ext import (
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
    CallbackQueryHandler,
)

from bot.constants.state import (
    CHECK,
    MAIN_MENU,
    BASIC_INFORMATION,
)
from bot.conversations.main_application import (
    greeting_callback,
    done_callback,
    check_the_secret_word_callback,
    main_menu_actions_callback,
)
from bot.conversations.basic_info_application import (
    basic_information_callback,
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
        # Обработка команды "основная информация"
        BASIC_INFORMATION: [
            CallbackQueryHandler(basic_information_callback),
        ],
    },
    fallbacks=[MessageHandler(filters.Regex("^Done$"), done_callback)],
)
