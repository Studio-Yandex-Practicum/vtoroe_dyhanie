from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType

from ..core.db import Base


class Contact(Base):
    '''Модель, содержащая информацию о контактах.'''
    full_name = Column(String(255), nullable=False)
    job_title = Column(String(255), nullable=False)
    dept = Column(String(255), nullable=False)
    phone_tg = Column(String(255), nullable=True)
    email = Column(EmailType, nullable=False)
    keywords = relationship('ContactKeyword', cascade='delete')

    def __repr__(self):
        return_str = (
            f'{self.full_name}\n'
            f'{self.job_title}\n'
            f'{self.dept}\n'
            f'{self.email}'
        )
        if self.phone_tg:
            return_str += f'\n{self.phone_tg}'
        return return_str

    def __eq__(self, other):
        if isinstance(other, Contact):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)
