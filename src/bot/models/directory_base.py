from sqlalchemy import Column, String

from ..core.db import Base


class DirectotyBase(Base):
    '''Базовая модель для справочников.'''

    __abstract__ = True

    name = Column(String(255), unique=True, nullable=False)
