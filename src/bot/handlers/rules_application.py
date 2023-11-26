from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import Application, CallbackQueryHandler, ContextTypes

from bot.constants import rules_text
from bot.constants.query_patterns import INFO_PREFIX
from bot.constants.rules_text import (
    COMMUNICATION,
    IN_COMMUNICATION,
    OUT_COMMUNICATION,
    WORKSHOP,
)
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
from bot.utils.send_message import send_message


async def communication_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Коммуникация.'''
    await send_message(
        update.callback_query.message,
        COMMUNICATION,
        reply_markup=communication_markup,
    )


async def workshop_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    '''Обработка кнопки Мастерская.'''
    await send_message(
        update.callback_query.message, WORKSHOP, reply_markup=workshop_markup
    )


async def kitchen_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    '''Обработка кнопки Кухня.'''
    await update.callback_query.message.edit_text(
        rules_text.KITCHEN,
        parse_mode=ParseMode.MARKDOWN_V2,
        disable_web_page_preview=True,
        reply_markup=kitchen_markup,
    )


async def separate_collection_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    '''Обработка кнопки Раздельный сбор.'''
    await update.callback_query.message.edit_text(
        rules_text.SEPARATE_COLLECTION,
        parse_mode=ParseMode.MARKDOWN_V2,
        disable_web_page_preview=True,
        reply_markup=separate_collection_markup,
    )


async def regular_meetings_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    '''Обработка кнопки Регулярные встречи.'''
    await update.callback_query.message.edit_text(
        rules_text.REGULAR_MEETINGS,
        parse_mode=ParseMode.MARKDOWN_V2,
        disable_web_page_preview=True,
        reply_markup=regular_meetings_markup,
    )


async def rules_back_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Возврата в меню Общие правила.'''
    await update.callback_query.message.edit_text(
        'Выберете действие:', reply_markup=rules_markup
    )


async def in_communication_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Внутренняя коммуникация.'''
    await update.callback_query.message.reply_text(
        IN_COMMUNICATION,
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=in_communication_markup,
    )


async def out_communication_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработка кнопки Внешняя коммуникация.'''
    await send_message(
        update.callback_query.message,
        OUT_COMMUNICATION,
        reply_markup=out_communication_markup,
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
