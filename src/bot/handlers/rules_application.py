from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import (
    Application, CallbackQueryHandler, ContextTypes
)

from bot.constants import rules_text
from bot.constants.query_patterns import INFO_PREFIX
from bot.constants.rules_text import COMMUNICATION, WORKSHOP
from bot.keyboards.rules_keyboards import (
    communication_markup, rules_markup,
    kitchen_markup, separate_collection_markup,
    regular_meetings_markup, workshop_markup
)


async def communication_callback(
        update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Обработка кнопки Коммуникация."""
    await update.callback_query.message.edit_text(COMMUNICATION.get('msg_1'))
    await update.callback_query.message.edit_text(
        COMMUNICATION.get('msg_2'),
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=communication_markup
    )


async def workshop_callback(
        update: Update, context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """Обработка кнопки Мастерская."""



async def kitchen_callback(
        update: Update, context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """Обработка кнопки Кухня."""
    query = update.callback_query
    await query.answer()
    await query.message.edit_text(
        rules_text.KITCHEN,
        parse_mode='HTML',
        disable_web_page_preview=True,
        reply_markup=kitchen_markup,
    )


async def separate_collection_callback(
        update: Update, context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """Обработка кнопки Раздельный сбор."""
    query = update.callback_query
    await query.answer()
    await query.message.edit_text(
        rules_text.SEPARATE_COLLECTION,
        parse_mode='HTML',
        disable_web_page_preview=True,
        reply_markup=separate_collection_markup,
    )


async def regular_meetings_callback(
        update: Update, context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """Обработка кнопки Регулярные встречи."""
    query = update.callback_query
    await query.answer()
    await query.message.edit_text(
        rules_text.REGULAR_MEETINGS,
        parse_mode='HTML',
        disable_web_page_preview=True,
        reply_markup=regular_meetings_markup,
    )


async def rules_back_callback(
        update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Обработка кнопки Возврата в меню Общие правила."""
    query = update.callback_query
    await query.answer()
    await query.message.edit_text(
        'Выберете действие:', reply_markup=rules_markup
    )


def register_handlers(app: Application) -> None:
    registrator = {
        f'{INFO_PREFIX}communication': communication_callback,
        f'{INFO_PREFIX}workshop': workshop_callback,
        f'{INFO_PREFIX}kitchen': kitchen_callback,
        f'{INFO_PREFIX}separate_collection': separate_collection_callback,
        f'{INFO_PREFIX}regular_meetings': regular_meetings_callback,
        'rules_back': rules_back_callback
    }
    for pattern, handler in registrator.items():
        app.add_handler(CallbackQueryHandler(handler, pattern=pattern))
