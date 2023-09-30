from telegram.ext import (
    CallbackQueryHandler,
    CommandHandler,
    ConversationHandler,
    filters,
    MessageHandler,
)

from bot.constants.state import (
    CHECK,
    MAIN_MENU,
    BASIC_INFORMATION,
    FIO,
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
from bot.conversations.contact_list_application import (
    find_contact_by_fio,
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
        FIO: [
            MessageHandler(filters.TEXT, find_contact_by_fio),
        ]
    },
    fallbacks=[MessageHandler(filters.Regex("^Done$"), done_callback)],
)
