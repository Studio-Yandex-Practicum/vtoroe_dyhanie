from telegram import Update
from telegram.ext import ContextTypes

from bot.constants.info.text import HELP


async def help(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
) -> None:
    await update.message.reply_text(HELP)
