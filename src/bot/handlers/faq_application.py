import requests
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import Application, ContextTypes, MessageHandler, filters


def get_keyboard_data() -> dict:
    response = requests.get('http://127.0.0.1:8000/keyboards/10:17/')
    return response.json()


def get_faq_text_data() -> dict:
    response = requests.get('http://127.0.0.1:8000/faq_text/1:12/')
    return response.json()


async def faq_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обрабатывает команды раздела FAQ.'''
    keyboard_data = get_keyboard_data()
    user_input = update.message.text
    key_message_data = next(
        (
            key for key,
            value in keyboard_data.items() if value == user_input), None)

    if key_message_data:
        faq_text_data = get_faq_text_data()
        STORAGE_LINK = faq_text_data.get("STORAGE_LINK", "")
        STUDIES_LINK = faq_text_data.get("STUDIES_LINK", "")
        VOLUNTARISM_LINK = faq_text_data.get("VOLUNTARISM_LINK", "")
        text = faq_text_data.get(key_message_data).format(
            STORAGE_LINK=STORAGE_LINK,
            STUDIES_LINK=STUDIES_LINK,
            VOLUNTARISM_LINK=VOLUNTARISM_LINK
        )
        await update.message.reply_text(
            text=text,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
        )


def register_handlers(app: Application) -> None:
    '''Регистрация обработчика.'''
    keyboard_data = get_keyboard_data()
    app.add_handler(
        MessageHandler(
            filters.Text(keyboard_data.values()), faq_callback
        )
    )
