from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint

from ..core.db import Base


class DepartmentJobTitle(Base):
    '''Модель должностей в отделах.'''

    __table_args__ = (
        UniqueConstraint(
            'department_id', 'job_title_id', name="unique_department_job_title"
        ),
    )

    department_id = Column(Integer, ForeignKey('department.id'))
    job_title_id = Column(Integer, ForeignKey('jobtitle.id'))
