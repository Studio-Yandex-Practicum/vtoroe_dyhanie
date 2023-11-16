import re
from datetime import datetime

from pydantic import BaseModel, validator


class QuestionModel(BaseModel):
    question: str

    @validator('question')
    def check_question_length(cls, value):  # noqa
        '''Проверка на количество символов'''
        if not (3 <= len(value) <= 150):
            raise ValueError(
                'Длина сообщения должна быть от 3 до 150 символов'
            )
        return value

    @validator('question')
    def check_question_content(cls, value):  # noqa
        '''Проверка на кирилицу'''
        if not re.match(r'^[а-яА-Я0-9\s\W]*$', value):
            raise ValueError('Сообщение должно содержать только кириллицу.')
        return value


class DateModel(BaseModel):
    employment_date: datetime

    @validator('employment_date')
    def date_must_be_past_or_present(cls, v):
        '''Проверка правильности введенной даты'''
        if v.date() > datetime.today().date():
            raise ValueError(
                'Дата должна быть прошлой или сегодняшней.'
                'Будущие даты вводить нельзя.'
            )
        return v
