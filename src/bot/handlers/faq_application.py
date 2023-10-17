from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters

from bot.constants import faq_text


async def faq_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """Обрабатывает команды раздела FAQ"""
    user_input = update.message.text
    await update.message.reply_text(
        text=faq_text.FAQ_MESSAGES.get(user_input),
        parse_mode='Markdown',
        disable_web_page_preview=True,
    )


def register_handlers(app: Application) -> None:
    app.add_handler(
        MessageHandler(
            filters.Text(faq_text.FAQ_MESSAGES.keys()), faq_callback
        )
    )
