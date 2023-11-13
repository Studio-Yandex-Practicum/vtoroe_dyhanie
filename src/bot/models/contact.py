from sqlalchemy import Column, String
from sqlalchemy_utils import EmailType

from ..core.db import Base


class Contact(Base):
    '''Модель контактов.'''

    full_name = Column(String(255), nullable=False)
    phone = Column(String(255), nullable=True)
    telegram = Column(String(255), nullable=True)
    email = Column(EmailType, nullable=False)

    def __eq__(self, other):
        if isinstance(other, Contact):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)
