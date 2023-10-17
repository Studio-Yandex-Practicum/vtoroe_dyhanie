import logging

from telegram import Update
from telegram.ext import ContextTypes


async def error_handler(
    update: object, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Log the error while Update."""
    logging.error(
        msg='Exception while handling an update:', exc_info=context.error
    )
