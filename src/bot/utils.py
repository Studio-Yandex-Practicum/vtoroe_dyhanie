from functools import wraps

import telegram
from telegram import CallbackQuery


def safe_edit_text(func):
    """
    Декоратор для проверки сообщений на дублирующийся контент.
    В тех случаях когда пользователь может нажать на одну и ту же кнопку
    несколько раз, появляется исключение telegram.error.BadRequest: Message is not modified.
    Данный декоратор создан, чтобы обрабатывать это исключение.
    """

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
