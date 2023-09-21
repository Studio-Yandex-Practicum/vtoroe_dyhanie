from telegram import Update

# from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from bot.constants.text import (
    ORG_QSTS_MESSAGE,
    VOLUNTARISM_MESSAGE,
    STUDIES_MESSAGE,
    VACATION_MESSAGE,
    WORK_PROC_MESSAGE,
    ADMIN_QSTS_MESSAGE,
    DOCFLOW_MESSAGE,
    BUSINESS_TRIP_MESSAGE,
)


async def org_qsts_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Отсылает информацию об организационных вопросах."""
    await update.message.reply_text(
        text=ORG_QSTS_MESSAGE,
        parse_mode="Markdown",
    )


async def voluntarism_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Отсылает информацию по вопросам волонтёрства и ссылку."""
    await update.message.reply_text(
        text=VOLUNTARISM_MESSAGE,
        parse_mode="Markdown",
        disable_web_page_preview=True,
    )


async def studies_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Отсылает информацию по вопросам обучения и ссылку."""
    await update.message.reply_text(
        text=STUDIES_MESSAGE,
        parse_mode="Markdown",
        disable_web_page_preview=True,
    )


async def vacation_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Отсылает информацию по вопросу отпуска."""
    await update.message.reply_text(
        text=VACATION_MESSAGE,
        parse_mode="Markdown",
        disable_web_page_preview=False,
    )


async def work_proc_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Отсылает информацию по вопросам рабочего процесса и ссылку."""
    await update.message.reply_text(
        text=WORK_PROC_MESSAGE,
        parse_mode="Markdown",
        disable_web_page_preview=True,
    )


async def admin_qsts_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Отсылает информацию об административных вопросах."""
    await update.message.reply_text(
        text=ADMIN_QSTS_MESSAGE,
        parse_mode="Markdown",
        disable_web_page_preview=False,
    )


async def docflow_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Отсылает информацию по вопросам оформления документов."""
    await update.message.reply_text(
        text=DOCFLOW_MESSAGE,
        parse_mode="Markdown",
        disable_web_page_preview=False,
    )


async def business_trip_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Отсылает информацию по вопросам командировок."""
    await update.message.reply_text(
        text=BUSINESS_TRIP_MESSAGE,
        parse_mode="Markdown",
        disable_web_page_preview=False,
    )
