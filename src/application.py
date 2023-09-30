from telegram.ext import Application

from bot.core.settings import settings
from bot.handlers import register_all_handlers


def main() -> None:  # noqa
    """Start the bot"""
    app = Application.builder().token(settings.telegram_token).build()

    register_all_handlers(app)

    app.run_polling()


if __name__ == "__main__":
    main()
