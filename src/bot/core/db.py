from sqlalchemy import Column, Integer
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker

from .settings import database_url


class PreBase:
    @declared_attr
    def __tablename__(cls):  # noqa
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)

engine = create_async_engine(database_url)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)
