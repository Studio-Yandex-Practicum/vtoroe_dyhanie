from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
)

from bot.utils.admin_api import get_django_json


# Основное меню
async def main_menu_markup():
    messages = await get_django_json('/keyboards/1:9/')
    messages = [text for text in messages.values()]
    about_fund_markup = ReplyKeyboardMarkup(
        [messages[x : x + 2] for x in range(0, len(messages), 2)],  # noqa
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    return about_fund_markup  # noqa


async def faq_menu_markup():
    messages = await get_django_json('/keyboards/10:18/')
    messages = [text for text in messages.values()]
    faq_menu_keyboard = ReplyKeyboardMarkup(
        [messages[x : x + 2] for x in range(0, len(messages), 2)],  # noqa
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    return faq_menu_keyboard  # noqa


async def main_button_markup():
    messages = await get_django_json('/keyboards/19/')
    main_button_keyboard = [
        [
            InlineKeyboardButton(
                messages.get('BACK_BUTTON', ''),
                callback_data='back_to_main_menu',
            )
        ]  # ?
    ]
    return InlineKeyboardMarkup(main_button_keyboard)
