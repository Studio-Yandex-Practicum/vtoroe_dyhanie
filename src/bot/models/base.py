'''Импорты класса Base и всех моделей для Alembic.'''
from ..core.db import Base  # noqa
from . import Contact  # noqa
from . import (  # noqa
    ContactKeyword,
    Department,
    DepartmentJobTitle,
    JobTitle,
    Keyword,
    Position,
)
