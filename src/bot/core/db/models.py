from sqlalchemy.orm import Mapped, mapped_column

from bot.core.db.base import Base


class UserPermission(Base):
    tg_user_id: Mapped[int] = mapped_column(unique=True, nullable=False)
    permission: Mapped[bool] = mapped_column()
