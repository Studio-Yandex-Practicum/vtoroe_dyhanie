from telegram import (
    CallbackQuery
)

from bot.constants.text import (
    BACK_TO_MENU,
)
from bot.keyboards import (
    main_menu_markup,
)


async def handle_back_to_main_menu(query: CallbackQuery) -> None:
    """Обработчик нажатия кнопки В главное меню"""
    await query.message.edit_text('Возвращаемся в главное меню...')
    await query.message.reply_text(
        BACK_TO_MENU, reply_markup=main_menu_markup
    )
