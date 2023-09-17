from telegram.ext import Application, CallbackQueryHandler, CommandHandler


from bot.conversations.command_application import help, stop
from bot.conversations.menu_application import menu_button
from bot.core.settings import settings
from bot.handlers import greeting


def main() -> None:
    """Start the bot"""
    app = Application.builder().token(settings.telegram_token).build()
    app.add_handler(CommandHandler('start', greeting))
# start feature 15: обработка кнопок Меню ->
    app.add_handler(CallbackQueryHandler(menu_button))
# <- end feature 15: обработка кнопок Меню
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler("stop", stop))

    app.run_polling()


if __name__ == "__main__":
    main()
