import re
import smtplib
import ssl
from typing import Dict

from pydantic import BaseModel, validator
from telegram import InlineKeyboardMarkup, Message, Update
from telegram.constants import ParseMode

from bot.core.settings import settings


_TYPES = [Message, Update]


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


async def send_message(
    message: _TYPES,
    message_text_value: Dict[str, str],
    reply_markup: InlineKeyboardMarkup,
) -> None:
    '''Отправляет сообщение и раскладку клавиатуры.'''
    for index, value in enumerate(message_text_value.values()):
        if index < len(message_text_value) - 1:
            await message.reply_text(value)
        else:
            await message.reply_text(
                (value),
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=reply_markup,
            )


def send_email(subject, body_text):
    '''
    Отправляет сообщение на электронную почту.
    '''
    # Создание безопасного контекста SSL
    context = ssl.create_default_context()

    message = '\r\n'.join(
        (
            f'From: {settings.sender_email}',
            f'To: {settings.receiver_email}',
            f'Subject: {subject}',
            '',
            body_text,
        )
    )

    with smtplib.SMTP_SSL(
        settings.smtp_server, settings.port, context=context
    ) as server:
        server.login(settings.sender_email, settings.password_email)
        server.sendmail(
            settings.sender_email,
            settings.receiver_email,
            message.encode('UTF-8'),
        )


# Тестовые данные
# subject = 'Тестирование'
# body_text = '''Ненужная одежда — огромный ресурс и катализатор изменений. Она
# важна для того, чтобы бездомный не замёрз на улице, а девушка из нуждающейся
# семьи пошла на свой первый в жизни выпускной бал красивой. Одежда не только
# помогает людям, но и создает рабочие места и даже может вернуться в нашу
# жизнь в качестве набивки для дивана. '''

# send_email(subject, body_text)
