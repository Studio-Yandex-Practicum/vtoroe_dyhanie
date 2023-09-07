from telegram.ext import Application, CommandHandler

from bot.handlers import greeting

TOKEN = 'TOKEN'


def main() -> None:
    """Start the bot"""
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', greeting))
    app.run_polling()


if __name__ == '__main__':
    main()
