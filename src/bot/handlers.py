from telegram.ext import (
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)

from bot.constants.state import CHECK, FAQ, MENU
from bot.conversations.main_application import (
    greeting_callback,
    done_callback,
    check_the_secret_word_callback,
    faq_callback,
    back_button_callback,
)
from bot.conversations.menu_application import (
    org_qsts_callback,
    voluntarism_callback,
    studies_callback,
    vacation_callback,
    work_proc_callback,
    admin_qsts_callback,
    docflow_callback,
    business_trip_callback,
)


conv_handler = ConversationHandler(
    entry_points=[CommandHandler("start", greeting_callback)],
    states={
        CHECK: [
            MessageHandler(filters.TEXT, check_the_secret_word_callback),
        ],
        MENU: [
            MessageHandler(filters.Text(["FAQ"]), faq_callback),
        ],
        FAQ: [
            MessageHandler(
                filters.Text(["Организационные вопросы"]), org_qsts_callback
            ),
            MessageHandler(
                filters.Text(["Волонтёрство"]), voluntarism_callback
            ),
            MessageHandler(filters.Text(["Обучение"]), studies_callback),
            MessageHandler(filters.Text(["Отпуск"]), vacation_callback),
            MessageHandler(
                filters.Text(["Рабочий процесс"]), work_proc_callback
            ),
            MessageHandler(
                filters.Text(["Административные вопросы"]), admin_qsts_callback
            ),
            MessageHandler(
                filters.Text(["Оформление документов"]), docflow_callback
            ),
            MessageHandler(
                filters.Text(["Командировки"]), business_trip_callback
            ),
            MessageHandler(filters.Text(["Назад"]), back_button_callback),
        ],
    },
    fallbacks=[MessageHandler(filters.Regex("^Done$"), done_callback)],
)
