from warnings import filterwarnings

from telegram.warnings import PTBUserWarning

filterwarnings(  # noqa
    action="ignore",
    message=r".*CallbackQueryHandler",
    category=PTBUserWarning,  # noqa
)  # noqa

from telegram.ext import (
    Application,
    CommandHandler,
)

from bot.conversations.command_application import (
    help,
    stop,
)
from bot.core.settings import settings
from bot.handlers import conv_handler


def main() -> None:  # noqa
    """Start the bot"""
    app = Application.builder().token(settings.telegram_token).build()

    app.add_handler(conv_handler)
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("stop", stop))

    app.run_polling()


if __name__ == "__main__":
    main()
