from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import Application, CallbackQueryHandler, ContextTypes

from bot.constants import onboarding_text
from bot.constants.query_patterns import INFO_PREFIX
from bot.constants.onboarding_text import (
    TASKS_FOR_MENTOR,
)
from bot.keyboards.onboarding_keyboards import (
    mentor_markup,
    mentor_tasks_markup,
)


async def mentor_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Обработка кнопки Наставник/Бадди."""
    await update.callback_query.message.reply_text(
        onboarding_text.MENTOR,
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=mentor_markup,
    )


async def mentor_tasks_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Обработка кнопки Задачи Наставника/Бадди."""
    await update.callback_query.message.reply_text(
        onboarding_text.TASKS_FOR_MENTOR,
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=mentor_tasks_markup,
    )


def register_handlers(app: Application) -> None:
    registrator = {
        f'{INFO_PREFIX}mentor_or_buddy': mentor_callback,
        f'{INFO_PREFIX}menor_tasks': mentor_tasks_callback,
    }
    for pattern, handler in registrator.items():
        app.add_handler(CallbackQueryHandler(handler, pattern=pattern))
