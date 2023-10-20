from typing import Dict

from telegram import InlineKeyboardMarkup, Message, Update
from telegram.constants import ParseMode


_TYPES = [Message, Update]


async def send_message(
    message: _TYPES,
    message_text_value: Dict[str, str],
    reply_markup: InlineKeyboardMarkup,
) -> None:
    """Отправляет сообщение и раскладку клавиатуры."""
    for index, value in enumerate(message_text_value.values()):
        if index < len(message_text_value) - 1:
            await message.reply_text(value)
        else:
            await message.reply_text(
                (value),
                parse_mode=ParseMode.MARKDOWN_V2,
                reply_markup=reply_markup,
            )
