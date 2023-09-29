from functools import wraps

import telegram
from telegram import CallbackQuery


def safe_edit_text(func):
    @wraps(func)
    async def wrapper(query: CallbackQuery, *args, **kwargs):
        try:
            return await func(query, *args, **kwargs)
        except telegram.error.BadRequest as e:
            if "Message is not modified" in str(e):
                return
            else:
                raise e

    return wrapper
