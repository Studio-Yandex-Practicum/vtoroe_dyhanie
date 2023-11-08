import asyncio
import re
import smtplib
import ssl
from typing import Dict

from sqlalchemy import select
from telegram import InlineKeyboardMarkup, Message, Update
from telegram.constants import ParseMode

from .constants.keyword_serch import (
    CONTACTS_FOUND,
    MAX_CONTACTS,
    MORE_THAN_MAX_CONTACTS_FOUND,
    NO_CONTACTS_FOUND,
    RESTRICTED_WORDS,
)
from .core.db import AsyncSessionLocal
from .core.settings import settings
from .models import Contact, ContactKeyword


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


def parse_request(text: str) -> tuple[str]:
    '''
    Поиск по ключевым словам.
    Создание кортежа слов из текста запроса пользователя.
    '''
    words = re.split(',| ', text.lower())
    words = tuple(
        word for word in words
        if len(word) > 1 and word not in RESTRICTED_WORDS
    )
    return words


async def get_similars(word):
    '''
    Поиск по ключевым словам.
    Запрос к БД.
    '''
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(Contact).join(ContactKeyword).filter(
                ContactKeyword.keyword.contains(word)
            ).distinct()
        )
        return result.scalars().all()


async def find_contacts_in_DB(words: tuple) -> tuple:
    '''
    Поиск по ключевым словам.
    Поиск контактов в БД.
    '''
    tasks = []
    for word in words:
        tasks.append(asyncio.create_task(get_similars(word)))
    similar_contacts_list = await asyncio.gather(*tasks)
    results = dict()
    for similar_contacts in similar_contacts_list:
        for similar_contact in similar_contacts:
            results[similar_contact] = results.get(similar_contact, 0) + 1
    contacts = [key for key, value in results.items() if value == len(words)]
    if not contacts:
        contacts = sorted(
            [(key, value) for key, value in results.items()],
            key=lambda x: -x[1]
        )
        contacts = [x[0] for x in contacts]
    return contacts


def generate_answer(contacts):
    '''
    Поиск по ключевым словам.
    Генерация текста ответа.
    '''
    if not contacts:
        return NO_CONTACTS_FOUND
    contacts_to_print = contacts[:MAX_CONTACTS]
    result = CONTACTS_FOUND + '\n'
    for contact in contacts_to_print:
        result += f'\n{str(contact)}\n'
    if len(contacts) != len(contacts_to_print):
        result += '\n' + MORE_THAN_MAX_CONTACTS_FOUND
    return result.strip()


async def find_contacts(user_text: str) -> str:
    '''
    Поиск по ключевым словам.
    Поиск контактов по запросу пользователя.
    '''
    words = parse_request(user_text)
    contacts = await find_contacts_in_DB(words)
    answer = generate_answer(contacts)
    return answer
