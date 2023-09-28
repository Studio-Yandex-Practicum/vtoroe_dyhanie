from telegram.ext import (
    CallbackQueryHandler,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)

from bot.constants.state import (
    ABOUT_FUND_MENU_STATE,
    ANNUAL_REPORTS_STATE,
    CHECK,
    FUND_MISSION_STATE,
    FUND_PROJECTS_STATE,
    MENU,
    PROCESSES_ANATOMY_STATE,
    THINGS_PATH_STATE,
    FUND_PROJECTS_STATE,
    ANNUAL_REPORTS_STATE,
)
from bot.conversations.main_application import (
    greeting_callback,
    done_callback,
    check_the_secret_word_callback,
    main_menu_actions_callback,
)
from bot.conversations.menu_application import (
    about_fund_menu_callback,
    about_fund_more_info,
    annual_reports_more_info,
    fund_projects_more_info,
    processes_anatomy_more_info,
    things_path_more_info,
    fund_projects_more_info,
    annual_reports_more_info,
)

conv_handler = ConversationHandler(
    entry_points=[CommandHandler("start", greeting_callback)],
    states={
        CHECK: [
            MessageHandler(filters.TEXT, check_the_secret_word_callback),
        ],
        MENU: [
            MessageHandler(filters.TEXT, main_menu_actions_callback)
        ],
        ABOUT_FUND_MENU_STATE: [
            MessageHandler(filters.TEXT, about_fund_menu_callback)
        ],
        FUND_MISSION_STATE: [
            CallbackQueryHandler(about_fund_more_info)
        ],
        THINGS_PATH_STATE: [
            CallbackQueryHandler(things_path_more_info)
        ],
        PROCESSES_ANATOMY_STATE: [
            CallbackQueryHandler(processes_anatomy_more_info)
        ],
        FUND_PROJECTS_STATE: [
           CallbackQueryHandler(fund_projects_more_info)
        ],
        ANNUAL_REPORTS_STATE: [
            CallbackQueryHandler(annual_reports_more_info)
        ]
    },
    fallbacks=[MessageHandler(filters.Regex("^Done$"), done_callback)],
)
