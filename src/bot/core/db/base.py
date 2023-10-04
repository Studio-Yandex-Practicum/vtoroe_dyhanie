from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import (
    DeclarativeBase, declared_attr, Mapped, mapped_column
)

from bot.core.settings import settings


class Base(DeclarativeBase):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id: Mapped[int] = mapped_column(primary_key=True)


engine = create_async_engine(settings.database_url)
AsyncSessionLocal = async_sessionmaker(engine)
