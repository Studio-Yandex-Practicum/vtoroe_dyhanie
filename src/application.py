from telegram.ext import Application, CommandHandler, filters, MessageHandler

from bot.conversations.command_application import help, stop
from bot.core.settings import settings
from bot.handlers import greeting, reg_form_callback


def main() -> None:
    """Start the bot"""
    app = Application.builder().token(settings.telegram_token).build()
    app.add_handler(CommandHandler('start', greeting))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler("stop", stop))
    app.add_handler(
        MessageHandler(
            filters.Text(['Регламенты и формы']),
            reg_form_callback
        )
    )

    app.run_polling()


if __name__ == "__main__":
    main()
