import re

from pydantic import BaseModel, validator


class QuestionModel(BaseModel):
    question: str

    @validator('question')
    def check_question_length(cls, value):
        if not (3 <= len(value) <= 150):
            raise ValueError(
                'Длина сообщения должна быть от 3 до 150 символов'
            )
        return value

    @validator('question')
    def check_question_content(cls, value):
        if not re.match(r'^[а-яА-Я0-9\s\W]*$', value):
            raise ValueError('Сообщение должно содержать только кириллицу.')
        return value
