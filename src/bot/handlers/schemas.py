from pydantic import BaseModel, validator
from datetime import datetime


class DateModel(BaseModel):
    employment_date: datetime

    @validator('employment_date')
    def date_must_be_past_or_present(cls, v):
        if v.date() > datetime.today().date():
            raise ValueError('Дата должна быть прошлой или сегодняшней. Будущие даты вводить нельзя.')
        return v
