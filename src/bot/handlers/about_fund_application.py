"""Модуль с обработчиками сообщений и кнопок блока "О Фонде"

Модуль состоит из 5 блоков, каждый из которых обрабатывает
сообщения и нажатия кнопок из веток:
    - Миссия и основная цель;
    - Путь вещей;
    - Анатомия процессов;
    - Проекты Фонда;
    - Годовые отчеты.

Каждый блок состоит из 3 функций:
    - функция, отправляющая информацию блока и раскладку меню
под сообщениями;
    - функция, обрабатывающая кнопку меню раздела соответствующего блока;
    - функция, которая обрабатывает переход от одного блока к
другому, в случае, если пользователь нажимает кнопку для получения
дополнительной информации, например "Конечно! Расскажи подробнее!",
"Да, было бы здорово посмотреть!" и др.
"""

from telegram import CallbackQuery, Message, Update
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from bot.constants.about_fund_text import (
    ANNUAL_REPORTS,
    FUND_MISSION,
    FUND_PROJECTS,
    PROCESS_ANATOMY,
    THINGS_PATH,
)
from bot.constants.query_patterns import ABOUT_PREFIX
from bot.constants.text import BACK_TO_MENU
from bot.keyboards.about_fund_keyboards import (
    about_fund_markup,
    about_fund_section,
    annual_reports_markup,
    fund_mission_markup,
    fund_projects_markup,
    processes_anatomy_markup,
    things_path_markup,
)


async def handle_back_to_menu(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Обработчик нажатия кнопки "В меню раздела" """
    query = update.callback_query
    await query.answer()
    await query.message.edit_text('Возвращаемся в меню раздела «О фонде»...')
    await query.message.reply_text(
        BACK_TO_MENU, reply_markup=about_fund_markup
    )


async def about_fund_menu_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Обработчик кнопок основного меню блока "О Фонде"."""
    menu_item = update.message.text
    await about_menu_handlers.get(menu_item)(update, context)


async def about_fund_inline_btns_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Обработчик inline кнопок всех меню блока "О Фонде" """
    query = update.callback_query
    menu_item = query.data
    await query.answer()
    await about_inline_handlers.get(menu_item)(query)


# Блок "Миссия и основная цель"
async def send_about_fund_message(message: Message) -> None:
    """Отправляет сообщение и раскладку клавиатуры
    при нажатии кнопки "Миссия и основная цель".
    """
    await message.reply_text(FUND_MISSION.get('msg_1'))
    await message.reply_text(FUND_MISSION.get('msg_2'))
    await message.reply_text(FUND_MISSION.get('msg_3'))
    await message.reply_text(FUND_MISSION.get('msg_4'))
    await message.reply_text(FUND_MISSION.get('msg_5'))
    await message.reply_text(
        FUND_MISSION.get('msg_6'),
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=fund_mission_markup,
    )


async def about_fund_mission(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Обработчик кнопки "Миссия и основная цель" """
    await send_about_fund_message(update.message)


async def handle_mission_more_info(query: CallbackQuery) -> None:
    """Обработчик кнопки "Конечно! Расскажи подробнее"
    ветки "Миссия и основная цель".
    """
    # Спрятать inline-клавиатуру после нажатия кнопки
    # await query.edit_message_reply_markup()
    await query.answer()
    await send_things_path_message(query.message)


# Блок "Путь вещей"


async def send_things_path_message(message: Message) -> None:
    """Отправляет сообщение и раскладку клавиатуры
    при нажатии кнопки "Путь вещей".
    """
    await message.reply_text(THINGS_PATH.get('msg_1'))
    await message.reply_text(THINGS_PATH.get('msg_2'))
    await message.reply_text(THINGS_PATH.get('msg_3'))
    await message.reply_text(THINGS_PATH.get('msg_4'))
    await message.reply_text(
        THINGS_PATH.get('msg_5'),
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=things_path_markup,
    )


async def things_path(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Обработчик кнопки "Путь вещей"."""
    await send_things_path_message(update.message)


async def handle_path_more_info(query: CallbackQuery) -> None:
    """Обработчик кнопки "Да, было бы здорово посмотреть!"
    ветки "Путь вещей".
    """
    # Спрятать inline-клавиатуру после нажатия кнопки
    # await query.edit_message_reply_markup()
    await query.answer()
    await send_processes_anatomy_message(query.message)


# Блок "Анатомия процессов"


async def send_processes_anatomy_message(message: Message) -> None:
    """Отправляет сообщение и раскладку клавиатуры
    при нажатии кнопки "Анатомия процессов".
    """
    await message.reply_text(
        PROCESS_ANATOMY,
        parse_mode=ParseMode.MARKDOWN_V2,
        disable_web_page_preview=True,
        reply_markup=processes_anatomy_markup,
    )


async def processes_anatomy(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Обработчик кнопки "Анатомия процессов"."""
    await send_processes_anatomy_message(update.message)


async def handle_process_anatomy_more_info(query: CallbackQuery) -> None:
    """Обработчик кнопки "Конечно! Какие?"
    ветки "Анатомия процессов".
    """
    # Спрятать inline-клавиатуру после нажатия кнопки
    # await query.edit_message_reply_markup()
    await query.answer()
    await send_fund_projects_message(query.message)


# Блок "Проекты Фонда"


async def send_fund_projects_message(message: Message) -> None:
    """Отправляет сообщение и раскладку клавиатуры
    при нажатии кнопки "Проекты Фонда".
    """
    await message.reply_text(FUND_PROJECTS.get('msg_1'))
    await message.reply_text(FUND_PROJECTS.get('msg_2'))
    await message.reply_text(FUND_PROJECTS.get('msg_3'))
    await message.reply_markdown(
        FUND_PROJECTS.get('msg_4'), reply_markup=fund_projects_markup
    )


async def fund_projects(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Обработчик кнопки "Проекты Фонда"."""
    await send_fund_projects_message(update.message)


async def handle_projects_more_info(query: CallbackQuery) -> None:
    """Обработчик кнопки "Почитаю с удовольствием!"
    ветки "Проекты Фонда".
    """
    # Спрятать inline-клавиатуру после нажатия кнопки
    # await query.edit_message_reply_markup()
    await query.answer()
    await send_annual_reports_message(query.message)


# Блок "Годовые отчеты"


async def send_annual_reports_message(message: Message) -> None:
    """Отправляет сообщение и раскладку клавиатуры
    при нажатии кнопки "Годовые отчеты".
    """
    await message.reply_markdown_v2(
        ANNUAL_REPORTS,
        disable_web_page_preview=True,
        reply_markup=annual_reports_markup,
    )


async def annual_reports(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Обработчик кнопки "Годовые отчеты"."""
    await send_annual_reports_message(update.message)


about_inline_handlers = {
    f'{ABOUT_PREFIX}more_info_mission': handle_mission_more_info,
    f'{ABOUT_PREFIX}more_info_path': handle_path_more_info,
    f'{ABOUT_PREFIX}more_info_processes': handle_process_anatomy_more_info,
    f'{ABOUT_PREFIX}more_info_projects': handle_projects_more_info,
}
about_menu_handlers = {
    'Миссия и основная цель': about_fund_mission,
    'Путь вещей': things_path,
    'Анатомия процессов': processes_anatomy,
    'Проекты Фонда': fund_projects,
    'Годовые отчеты': annual_reports,
}


def register_handlers(app: Application) -> None:
    app.add_handler(
        CallbackQueryHandler(
            about_fund_inline_btns_handler,
            pattern=fr'{ABOUT_PREFIX}more_info(\w+)',
        )
    )
    app.add_handler(
        CallbackQueryHandler(
            handle_back_to_menu, pattern=fr'{ABOUT_PREFIX}back_to_menu'
        )
    )
    app.add_handler(
        MessageHandler(
            filters.Text(about_fund_section), about_fund_menu_callback
        )
    )
