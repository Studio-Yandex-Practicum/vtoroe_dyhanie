from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint

from ..core.db import Base


class Position(Base):
    '''Модель занимаемых контактами позиций.'''

    __table_args__ = (
        UniqueConstraint(
            'contact_id',
            'department_job_title_id',
            name="unique_contact_id_department_job_title_id",
        ),
    )

    contact_id = Column(Integer, ForeignKey('contact.id'))
    department_job_title_id = Column(
        Integer, ForeignKey('departmentjobtitle.id')
    )
