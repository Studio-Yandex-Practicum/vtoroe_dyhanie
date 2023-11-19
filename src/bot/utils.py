import smtplib
import ssl
from typing import Dict
import requests
import aiohttp

from telegram import InlineKeyboardMarkup, Message, Update
from telegram.constants import ParseMode

from bot.core.settings import settings


_TYPES = [Message, Update]


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


async def check_text():
    response = requests.get('http://127.0.0.1:8000/keyboards/10:17/')
    message_data = response.json()
    return message_data.values()


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


async def get_django_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

# Тестовые данные
# subject = 'Тестирование'
# body_text = '''Ненужная одежда — огромный ресурс и катализатор изменений. Она
# важна для того, чтобы бездомный не замёрз на улице, а девушка из нуждающейся
# семьи пошла на свой первый в жизни выпускной бал красивой. Одежда не только
# помогает людям, но и создает рабочие места и даже может вернуться в нашу
# жизнь в качестве набивки для дивана. '''

# send_email(subject, body_text)
