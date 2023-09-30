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
from telegram import (
    CallbackQuery,
    Message,
    MessageEntity,
    Update
)
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from bot.constants.about_fund_text import (
    ANNUAL_REPORTS,
    FUND_MISSION,
    FUND_PROJECTS,
    PROCESS_ANATOMY,
    THINGS_PATH
)
from bot.constants.callback import ABOUT_FUND_CALLBACKS
from bot.constants.text import BACK_TO_MENU

from bot.keyboards.about_fund_keyboards import (
    about_fund_markup,
    about_fund_section,
    annual_reports_markup,
    fund_mission_markup,
    fund_projects_markup,
    processes_anatomy_markup,
    things_path_markup
)


async def handle_back_to_menu(query: CallbackQuery) -> None:
    """Обработчик нажатия кнопки "В меню раздела"
    """
    await query.message.edit_text(
        'Возвращаемся в меню раздела «О фонде»...'
    )
    await query.message.reply_text(
        BACK_TO_MENU, reply_markup=about_fund_markup
    )


async def about_fund_menu_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Обработчик кнопок основного меню блока "О Фонде".
    """
    menu_item = update.message.text

    # Миссия и основная цель
    if menu_item == about_fund_section.get('mission'):
        await about_fund_mission(update, context)
    # Путь вещей
    elif menu_item == about_fund_section.get('things_path'):
        await things_path(update, context)
    # Анатомия процессов
    elif menu_item == about_fund_section.get('processes_anatomy'):
        await processes_anatomy(update, context)
    # Проекты Фонда
    elif menu_item == about_fund_section.get('fund_projects'):
        await fund_projects(update, context)
    # Годовые отчеты
    elif menu_item == about_fund_section.get('annual_reports'):
        await annual_reports(update, context)


async def about_fund_inline_btns_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Обработчик inline кнопок всех меню блока "О Фонде"
    """
    query = update.callback_query
    menu_item = query.data

    await query.answer()
    # Нажатие кнопки "Конечно! Расскажи подробнее" блока
    # "Миссия и основная цель"
    if query.data == ABOUT_FUND_CALLBACKS.get('more_info_mission'):
        await handle_mission_more_info(query)
    # Нажатие кнопки "Да, было бы здорово посмотреть" блока
    # "Путь вещей"
    elif query.data == ABOUT_FUND_CALLBACKS.get('more_info_path'):
        await handle_path_more_info(query)
    # Нажатие кнопки "Кончно! Какие?" блока
    # "Анатомия процессов"
    elif query.data == ABOUT_FUND_CALLBACKS.get('more_info_processes'):
        await handle_processes_anatomy_more_info(query)
    # Нажатие кнопки "Почитаю с удовольствием!" блока
    # "Проекты Фонда"
    elif query.data == ABOUT_FUND_CALLBACKS.get('more_info_projects'):
        await handle_projects_more_info(query)

    # Нажатие кнопки "В меню раздела" любого блока
    elif menu_item == ABOUT_FUND_CALLBACKS.get('back_to_menu'):
        await handle_back_to_menu(update.callback_query)


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
        entities=(
            MessageEntity(
                type=MessageEntity.BOLD,
                offset=0,
                length=len(FUND_MISSION.get('msg_6'))
            ),
        ),
        reply_markup=fund_mission_markup
    )


async def about_fund_mission(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Обработчик кнопки "Миссия и основная цель"
    """
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
        entities=(
            MessageEntity(
                type=MessageEntity.BOLD,
                offset=0,
                length=len(THINGS_PATH.get('msg_5'))
            ),
        ),
        reply_markup=things_path_markup
    )


async def things_path(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Обработчик кнопки "Путь вещей".
    """
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
        reply_markup=processes_anatomy_markup
    )


async def processes_anatomy(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Обработчик кнопки "Анатомия процессов".
    """
    await send_processes_anatomy_message(update.message)


async def handle_processes_anatomy_more_info(query: CallbackQuery) -> None:
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
        FUND_PROJECTS.get('msg_4'),
        reply_markup=fund_projects_markup
    )


async def fund_projects(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Обработчик кнопки "Проекты Фонда".
    """
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
        reply_markup=annual_reports_markup
    )


async def annual_reports(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Обработчик кнопки "Годовые отчеты".
    """
    await send_annual_reports_message(update.message)

