from functools import wraps

from sqlalchemy import select
from telegram import Update

from bot.core.db.base import AsyncSessionLocal
from bot.core.db.models import UserPermission
from bot.constants import text


def permission_required(func):
    """
    Декоратор для проверки доступа пользователя.
    Применяется к любым callback функциям к которым нужно ограничить доступ.
    """
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
        query = update.callback_query
        if query:
            await query.answer()
        await update.effective_chat.send_message(
            text=text.PERMISSION_ERROR_MESSAGE,
        )
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
