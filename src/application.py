from telegram.ext import (
    Application,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)

from bot.conversations.command_application import (
    help,
    stop,
)
from bot.core.settings import settings
from bot.handlers import (
    greeting_callback,
    done_callback,
    check_the_secret_word_callback,
)
from bot.utils import CHECK


def main() -> None:
    """Start the bot"""
    app = Application.builder().token(settings.telegram_token).build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", greeting_callback)],
        states={
            CHECK: [
                MessageHandler(filters.TEXT, check_the_secret_word_callback),
            ],
        },
        fallbacks=[MessageHandler(filters.Regex("^Done$"), done_callback)],
    )

    app.add_handler(conv_handler)
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("stop", stop))

    app.run_polling()


if __name__ == "__main__":
    main()
