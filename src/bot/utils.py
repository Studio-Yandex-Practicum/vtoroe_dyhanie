from functools import wraps

from sqlalchemy import select
from telegram import Update

from bot.core.db.base import AsyncSessionLocal
from bot.core.db.models import UserPermission
import telegram
from telegram import CallbackQuery


def permission_required(func):
    @wraps(func)
    async def wrapped(update: Update, context, *args, **kwargs):
        user_id = update.effective_user.id
        async with AsyncSessionLocal() as session:
            result = await session.scalars(
                select(UserPermission).
                where(UserPermission.tg_user_id == user_id)
            )
            current_user = result.first()
        if current_user and current_user.permission:
            return await func(update, context, *args, **kwargs)
        await update.message.reply_text('Доступ запрещен')
        return
    return wrapped


async def add_permission(user_id):
    async with AsyncSessionLocal() as session:
        result = await session.scalars(
            select(UserPermission).
            where(UserPermission.tg_user_id == user_id)
        )
        current_user = result.first()
        if current_user:
            current_user.permission = True
        else:
            current_user = UserPermission(tg_user_id=user_id, permission=True)
        session.add(current_user)
        await session.commit()


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
