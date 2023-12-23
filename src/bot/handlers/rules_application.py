from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import Application, CallbackQueryHandler, ContextTypes

from bot.constants.query_patterns import INFO_PREFIX
from bot.keyboards.rules_keyboards import (
    communication_markup,
    in_communication_markup,
    kitchen_markup,
    out_communication_markup,
    regular_meetings_markup,
    rules_markup,
    separate_collection_markup,
    workshop_markup,
)
from bot.utils.admin_api import get_django_json
from bot.utils.send_message import send_message


async def communication_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Коммуникация.'''
    message_data = await get_django_json('/rules_text/2:3/')
    await send_message(
        update.callback_query.message,
        message_data,
        reply_markup=await communication_markup(),
    )


async def workshop_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    '''Обработка кнопки Мастерская.'''
    message_data = await get_django_json('/rules_text/4:8/')
    await send_message(
        update.callback_query.message,
        message_data,
        reply_markup=await workshop_markup(),
    )


async def kitchen_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    '''Обработка кнопки Кухня.'''
    message_data = await get_django_json('/rules_text/9/')
    await update.callback_query.message.edit_text(
        message_data.get('KITCHEN', ''),
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True,
        reply_markup=await kitchen_markup(),
    )


async def separate_collection_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    '''Обработка кнопки Раздельный сбор.'''
    message_data = await get_django_json('/rules_text/10/')
    await update.callback_query.message.edit_text(
        message_data.get('SEPARATE_COLLECTION', ''),
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True,
        reply_markup=await separate_collection_markup(),
    )


async def regular_meetings_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    '''Обработка кнопки Регулярные встречи.'''
    message_data = await get_django_json('/rules_text/11/')
    await update.callback_query.message.edit_text(
        message_data.get('REGULAR_MEETINGS', ''),
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True,
        reply_markup=await regular_meetings_markup(),
    )


async def rules_back_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Возврата в меню Общие правила.'''
    await update.callback_query.message.edit_text(
        'Выберете действие:', reply_markup=await rules_markup()
    )


async def in_communication_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Внутренняя коммуникация.'''
    message_data = await get_django_json('/rules_text/12/')
    await update.callback_query.message.reply_text(
        message_data.get('IN_COMMUNICATION', ''),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=await in_communication_markup(),
    )


async def out_communication_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Внешняя коммуникация.'''
    message_data = await get_django_json('/rules_text/13/')
    await send_message(
        update.callback_query.message,
        message_data,
        reply_markup=await out_communication_markup(),
    )


def register_handlers(app: Application) -> None:
    '''Регистрация обработчиков.'''
    registrator = {
        f'{INFO_PREFIX}communication': communication_callback,
        f'{INFO_PREFIX}workshop': workshop_callback,
        f'{INFO_PREFIX}kitchen': kitchen_callback,
        f'{INFO_PREFIX}separate_collection': separate_collection_callback,
        f'{INFO_PREFIX}regular_meetings': regular_meetings_callback,
        f'{INFO_PREFIX}in_communication': in_communication_callback,
        f'{INFO_PREFIX}out_communication': out_communication_callback,
        'rules_back': rules_back_callback,
    }
    for pattern, handler in registrator.items():
        app.add_handler(CallbackQueryHandler(handler, pattern=pattern))
