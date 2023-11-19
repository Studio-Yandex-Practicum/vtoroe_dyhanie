from telegram.ext import Application

from bot.core.logger import logger  # noqa
from bot.core.settings import settings
from bot.error_handler import error_handler
from bot.handlers import start_handler_updater_thread


def main() -> None:  # noqa
    '''Старт бота.'''

    app = Application.builder().token(settings.telegram_token).build()

    start_handler_updater_thread(app)

    app.add_error_handler(error_handler)

    app.run_polling()


if __name__ == '__main__':
    main()
