from telegram.ext import Application

from bot.core.settings import settings
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

    app.run_polling()


if __name__ == "__main__":
    main()
