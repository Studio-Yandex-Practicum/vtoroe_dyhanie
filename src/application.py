from telegram.ext import Application

from bot.core.logger import logger  # noqa
from bot.core.settings import settings
from bot.error_handler import error_handler
from bot.handlers import register_all_handlers


def main() -> None:  # noqa
    '''Старт бота.'''

    app = Application.builder().token(settings.telegram_token).build()

    register_all_handlers(app)

    app.add_error_handler(error_handler)

    app.run_polling()


if __name__ == '__main__':
    main()
