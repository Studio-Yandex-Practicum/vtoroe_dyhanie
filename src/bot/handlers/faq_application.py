from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import Application, ContextTypes, MessageHandler, filters

from bot.utils.admin_api import get_django_json, get_django_json_sync


async def faq_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обрабатывает команды раздела FAQ.'''
    keyboard_data = await get_django_json('keyboards/10:17/')
    user_input = update.message.text
    key_message_data = next(
        (key for key, value in keyboard_data.items() if value == user_input),
        None,
    )

    if key_message_data:
        faq_text_data = await get_django_json('faq_text/1:12/')
        STORAGE_LINK = faq_text_data.get('STORAGE_LINK', '')
        STUDIES_LINK = faq_text_data.get('STUDIES_LINK', '')
        VOLUNTARISM_LINK = faq_text_data.get('VOLUNTARISM_LINK', '')
        text = faq_text_data.get(key_message_data).format(
            STORAGE_LINK=STORAGE_LINK,
            STUDIES_LINK=STUDIES_LINK,
            VOLUNTARISM_LINK=VOLUNTARISM_LINK,
        )
        await update.message.reply_text(
            text=text,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
        )


def register_handlers(app: Application) -> None:
    '''Регистрация обработчика.'''
    keyboard_data = get_django_json_sync('keyboards/10:17/')
    app.add_handler(
        MessageHandler(filters.Text(keyboard_data.values()), faq_callback)
    )
