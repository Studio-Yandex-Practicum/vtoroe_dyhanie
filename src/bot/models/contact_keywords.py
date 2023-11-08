from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint

from ..core.db import Base


class ContactKeyword(Base):
    '''Модель, содержащая ключевые слова для поиска контактов.'''
    __table_args__ = (
        UniqueConstraint(
            'keyword',
            'contact_id',
            name="unique_keywords_for_contact"
        ),
    )
    keyword = Column(String(100), nullable=False)
    contact_id = Column(Integer, ForeignKey('contact.id'))
