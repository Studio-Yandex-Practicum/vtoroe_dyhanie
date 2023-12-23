from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from bot.constants.query_patterns import INFO_PREFIX
from bot.utils.admin_api import get_django_json


# 1. Клавиатура для подраздела "Общие правила"
async def rules_markup():
    messages = await get_django_json('/rules_keyboards/1:5/')
    rules_keyboard = [
        [
            InlineKeyboardButton(
                messages.get('rules_keyboard_communication', ''),
                callback_data=f'{INFO_PREFIX}communication',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('rules_keyboard_workshop', ''),
                callback_data=f'{INFO_PREFIX}workshop',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('rules_keyboard_kitchen', ''),
                callback_data=f'{INFO_PREFIX}kitchen',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('rules_keyboard_separate_collection', ''),
                callback_data=f'{INFO_PREFIX}separate_collection',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('rules_keyboard_regular_meetings', ''),
                callback_data=f'{INFO_PREFIX}regular_meetings',
            )
        ],
    ]
    return InlineKeyboardMarkup(rules_keyboard)


# 2. Клавиатура для 'Коммуникация'
async def communication_markup():
    messages = await get_django_json('/rules_keyboards/6:9/')
    communication_keyboard = [
        [
            InlineKeyboardButton(
                messages.get('communication_keyboard_in_communication', ''),
                callback_data=f'{INFO_PREFIX}in_communication',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('communication_keyboard_out_communication', ''),
                callback_data=f'{INFO_PREFIX}out_communication',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('communication_keyboard_rules_back', ''),
                callback_data='rules_back',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('communication_keyboard_back_to_main_menu', ''),
                callback_data='back_to_main_menu',
            )
        ],
    ]
    return InlineKeyboardMarkup(communication_keyboard)


# 3. Клавиатура для 'Мастерская'
async def workshop_markup():
    messages = await get_django_json('/rules_keyboards/10:11/')
    workshop_keyboard = [
        [
            InlineKeyboardButton(
                messages.get('workshop_keyboard_rules_back', ''),
                callback_data='rules_back',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('workshop_keyboard_back_to_main_menu', ''),
                callback_data='back_to_main_menu',
            )
        ],
    ]
    return InlineKeyboardMarkup(workshop_keyboard)


# 4. Клавиатура для 'Кухня'
async def kitchen_markup():
    messages = await get_django_json('/rules_keyboards/12:13/')
    kitchen_keyboard = [
        [
            InlineKeyboardButton(
                messages.get('kitchen_keyboard_rules_back', ''),
                callback_data='rules_back',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('kitchen_keyboard_back_to_main_menu', ''),
                callback_data='back_to_main_menu',
            )
        ],
    ]
    return InlineKeyboardMarkup(kitchen_keyboard)


# 5. Клавиатура для 'Раздельный сбор'
async def separate_collection_markup():
    messages = await get_django_json('/rules_keyboards/14:15/')
    separate_collection_keyboard = [
        [
            InlineKeyboardButton(
                messages.get('separate_collection_keyboard_rules_back', ''),
                callback_data='rules_back',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get(
                    'separate_collection_keyboard_back_to_main_menu', ''
                ),
                callback_data='back_to_main_menu',
            )
        ],
    ]
    return InlineKeyboardMarkup(separate_collection_keyboard)


# 6. Клавиатура для 'Регулярные встречи'
async def regular_meetings_markup():
    messages = await get_django_json('/rules_keyboards/16:17/')
    regular_meetings_keyboard = [
        [
            InlineKeyboardButton(
                messages.get('regular_meetings_keyboard_rules_back', ''),
                callback_data='rules_back',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get(
                    'regular_meetings_keyboard_back_to_main_menu', ''
                ),
                callback_data='back_to_main_menu',
            )
        ],
    ]
    return InlineKeyboardMarkup(regular_meetings_keyboard)


# 7. Клавиатура для возврата из раздела о внутренней коммуникации
async def in_communication_markup():
    messages = await get_django_json('/rules_keyboards/18:19/')
    in_communication_keyboard = [
        [
            InlineKeyboardButton(
                messages.get(
                    'in_communication_keyboard_back_to_main_menu', ''
                ),
                callback_data='back_to_main_menu',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('in_communication_keyboard_rules_back', ''),
                callback_data='rules_back',
            )
        ],
    ]
    return InlineKeyboardMarkup(in_communication_keyboard)


# 8. Клавиатура для возврата из раздела о внешней коммуникации
async def out_communication_markup():
    messages = await get_django_json('/rules_keyboards/20:22/')
    message_link = await get_django_json('/rules_text/14/')
    link = message_link.get("RULES_LINK", "")
    out_communication_keyboard = [
        [
            InlineKeyboardButton(
                messages.get('out_communication_keyboard_rules_back', ''),
                callback_data='rules_back',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get(
                    'out_communication_keyboard_back_to_main_menu', ''
                ),
                callback_data='back_to_main_menu',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('out_communication_keyboard_url', ''), url=link
            )
        ],
    ]
    return InlineKeyboardMarkup(out_communication_keyboard)
