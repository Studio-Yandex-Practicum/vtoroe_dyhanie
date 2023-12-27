from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint

from ..core.db import Base


class ContactKeyword(Base):
    '''Модель ключевых слов контактов.'''

    __table_args__ = (
        UniqueConstraint(
            'contact_id', 'keyword_id', name="unique_contact_id_keyword_id"
        ),
    )

    contact_id = Column(Integer, ForeignKey('contact.id'))
    keyword_id = Column(Integer, ForeignKey('keyword.id'))
