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
)
from .core.db import AsyncSessionLocal
from .core.settings import settings
from .models import (
    Contact,
    ContactKeyword,
    Department,
    DepartmentJobTitle,
    JobTitle,
    Keyword,
    Position,
)


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


def prepare_words(word_string: str) -> set[str]:
    '''
    Поиск по ключевым словам.
    Создание сета слов из текста.
    '''
    words = re.split(r'\(|\)|,|\.| ', word_string)
    return set(word.lower().strip() for word in words if len(word) > 1)


async def get_similars(word: str) -> list[Contact]:
    '''
    Поиск по ключевым словам.
    Получение из БД информации о контакте по ключевому слову.
    '''
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(Contact)
            .select_from(Contact)
            .join(ContactKeyword, ContactKeyword.contact_id == Contact.id)
            .join(Keyword, Keyword.id == ContactKeyword.keyword_id)
            .where(Keyword.name.contains(word))
            .distinct()
        )
        return result.scalars().all()


async def get_contacts_full_info(contacts: Contact) -> list:
    '''
    Поиск по ключевым словам.
    Получение из БД полной информации о контакте.
    '''
    contact_ids = [contact.id for contact in contacts]
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(
                Contact.full_name,
                JobTitle.name,
                Department.name,
                Contact.phone,
                Contact.telegram,
                Contact.email,
            )
            .select_from(Contact)
            .join(Position, Position.contact_id == Contact.id)
            .join(
                DepartmentJobTitle,
                DepartmentJobTitle.id == Position.department_job_title_id,
            )
            .join(
                Department, Department.id == DepartmentJobTitle.department_id
            )
            .join(JobTitle, JobTitle.id == DepartmentJobTitle.job_title_id)
            .where(Contact.id.in_(contact_ids))
        )
    return result.all()


async def find_contacts_in_DB(words: set) -> list:
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
            key=lambda x: -x[1],
        )
        contacts = [x[0] for x in contacts]
    return contacts  # noqa


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
        result += f'\n{contact[0]}\n{contact[1]}\n{contact[2]}\n'
        if contact[3]:
            result += f'{contact[3]}\n'
        if contact[4]:
            result += f'{contact[4]}\n'
        result += f'{contact[5]}\n'
    if len(contacts) != len(contacts_to_print):
        result += '\n' + MORE_THAN_MAX_CONTACTS_FOUND
    return result.strip()


async def find_contacts(user_text: str) -> str:
    '''
    Поиск по ключевым словам.
    Поиск контактов по запросу пользователя.
    '''
    words = prepare_words(user_text)
    contacts = await find_contacts_in_DB(words)
    contacts_full_info = await get_contacts_full_info(contacts)
    return generate_answer(contacts_full_info)
