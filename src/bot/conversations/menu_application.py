from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from bot.keyboards import about_fund_markup


async def about_fund_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    await update.message.reply_text(
        'Сообщение 1',
        reply_markup=about_fund_markup
    )
