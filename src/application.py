from telegram.ext import Application

from bot.core.settings import settings
from bot.error_handler import error_handler
from bot.handlers import register_all_handlers
from bot.keyboards.keyboards import menu_button


def main() -> None:  # noqa
    """Start the bot"""

    app = (
        Application.builder()
        .token(settings.telegram_token)
        .post_init(menu_button)
        .build()
    )

    register_all_handlers(app)

    app.add_error_handler(error_handler)

    app.run_polling()


if __name__ == "__main__":
    main()
