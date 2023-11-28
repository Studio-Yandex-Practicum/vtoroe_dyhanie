from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from bot.utils.admin_api import get_django_json


async def contact_list_download_markup():
    '''Клавиатура для скачивания справочника контактов.'''
    messages = await get_django_json(
        'http://127.0.0.1:8000/contact_list_keyboards/1/'
    )
    links = await get_django_json('http://127.0.0.1:8000/links/3/')
    contact_list_download_keyboard = [
        [
            InlineKeyboardButton(
                messages['contact_list_download_keyboard'],
                url=links['CONTACT_LIST_LINK'],
            ),
        ],
    ]
    return InlineKeyboardMarkup(contact_list_download_keyboard)


async def contact_list_exit_markup():
    '''Клавиатура для выхода в главное меню после поиска контактов.'''
    messages = await get_django_json(
        'http://127.0.0.1:8000/contact_list_keyboards/2/'
    )
    contact_list_exit_keyboard = [
        (
            InlineKeyboardButton(
                messages['contact_list_exit_keyboard'],
                callback_data='exit_from_contact_search',
            ),
        ),
    ]
    return InlineKeyboardMarkup(contact_list_exit_keyboard)
