from telegram.ext import Application, CommandHandler

from bot.handlers import greeting
from bot.conversations.command_application import stop
from bot.core.settings import settings


def main() -> None:
    """Start the bot"""
    app = Application.builder().token(settings.telegram_token).build()
    app.add_handler(CommandHandler("start", greeting))
    app.add_handler(CommandHandler("stop", stop))
    app.run_polling()


if __name__ == "__main__":
    main()
