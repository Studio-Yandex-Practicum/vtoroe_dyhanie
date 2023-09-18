from telegram import Update
from telegram.ext import ContextTypes

from bot.constants.text import KNOWLEDGE_BASE


async def knowledge_base(
        update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Send message with knowledge base"""
    await update.message.reply_text(
        text=KNOWLEDGE_BASE,
        parse_mode="Markdown",
        disable_web_page_preview=True
    )
