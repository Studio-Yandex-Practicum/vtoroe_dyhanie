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
    - функция, обрабатывающая кнопки меню соответствующего блока,
а именно: получение дополнительной информации, назад в меню блока
и назад в основное меню.
    - функция, которая обрабатывает переход от одного блока к
другому, в случае, если пользователь нажимает кнопку для получения
дополнительной информации, например "Конечно! Расскажи подробнее!",
"Да, было бы здорово посмотреть!" и др.
"""
from telegram import (
    CallbackQuery,
    MessageEntity,
    Update
)
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from bot.constants.about_fund_text import (
    ABOUT_FUND_HISTORY,
    ANNUAL_REPORTS,
    FUND_MISSION,
    FUND_PROJECTS,
    PROCESS_ANATOMY,
    THINGS_PATH
)
from bot.constants.callback import (
    ABOUT_FUND_CALLBACKS
)
from bot.constants.state import (
    ABOUT_FUND_MENU_STATE,
    FUND_MISSION_STATE,
    FUND_PROJECTS_STATE,
    MAIN_MENU,
    PROCESSES_ANATOMY_STATE,
    THINGS_PATH_STATE,
    ANNUAL_REPORTS_STATE
)
from bot.constants.text import BACK_TO_MENU
from bot.conversations.menu_application import (
    handle_back_to_main_menu
)
from bot.keyboards_about_fund import (
    about_fund_markup,
    about_fund_section,
    annual_reports_markup,
    fund_history_markup,
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


async def about_fund_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> int:
    """Отправляет сообщения и раскладку клавиатуры при
    нажатии кнопки "О Фонде" из главного меню.
    """
    await update.message.reply_text(ABOUT_FUND_HISTORY.get('msg_1'))
    await update.message.reply_text(ABOUT_FUND_HISTORY.get('msg_2'))
    await update.message.reply_text(
        ABOUT_FUND_HISTORY.get('msg_3'),
        reply_markup=about_fund_markup
    )
    return ABOUT_FUND_MENU_STATE


async def about_fund_menu_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> int:
    """Обработчик кнопок основного меню блока "О Фонде".
    """
    menu_item = update.message.text
    # Миссия и основная цель
    if menu_item == about_fund_section.get('mission'):
        await about_fund_mission(update, context)
        return FUND_MISSION_STATE
    # Путь вещей
    elif menu_item == about_fund_section.get('things_path'):
        await things_path(update, context)
        return THINGS_PATH_STATE
    # Анатомия процессов
    elif menu_item == about_fund_section.get('processes_anatomy'):
        await processes_anatomy(update, context)
        return PROCESSES_ANATOMY_STATE
    # Проекты Фонда
    elif menu_item == about_fund_section.get('fund_projects'):
        await fund_projects(update, context)
        return FUND_PROJECTS_STATE
    # Годовые отчеты
    elif menu_item == about_fund_section.get('annual_reports'):
        await annual_reports(update, context)
        return ANNUAL_REPORTS_STATE


# Блок "Миссия и основная цель"

async def about_fund_mission(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Отправляет сообщение и раскладку клавиатуры
    при нажатии кнопки "Миссия и основная цель".
    """
    await update.message.reply_text(FUND_MISSION.get('msg_1'))
    await update.message.reply_text(FUND_MISSION.get('msg_2'))
    await update.message.reply_text(FUND_MISSION.get('msg_3'))
    await update.message.reply_text(FUND_MISSION.get('msg_4'))
    await update.message.reply_text(FUND_MISSION.get('msg_5'))
    await update.message.reply_text(
        FUND_MISSION.get('msg_6'),
        entities=(
            MessageEntity(
                type=MessageEntity.BOLD,
                offset=0,
                length=len(FUND_MISSION.get('msg_6'))
            ),
        ),
        reply_markup=fund_history_markup
    )


async def about_fund_more_info(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
) -> int:
    """Обработчик меню из раздела "Миссия и основная цель".
    """
    menu_item = update.callback_query.data
    if menu_item == ABOUT_FUND_CALLBACKS.get('more_info'):
        await handle_mission_more_info(update.callback_query)
        return THINGS_PATH_STATE
    elif menu_item == ABOUT_FUND_CALLBACKS.get('back_to_main_menu'):
        await handle_back_to_main_menu(update.callback_query)
        return MAIN_MENU
    elif menu_item == ABOUT_FUND_CALLBACKS.get('back_to_menu'):
        await handle_back_to_menu(update.callback_query)
        return ABOUT_FUND_MENU_STATE


async def handle_mission_more_info(query: CallbackQuery) -> None:
    """Обработчик кнопки "Конечно! Расскажи подробнее"
    ветки "Миссия и основная цель".
    """
    await query.answer()
    await query.message.reply_text(THINGS_PATH.get('msg_1'))
    await query.message.reply_text(THINGS_PATH.get('msg_2'))
    await query.message.reply_text(THINGS_PATH.get('msg_3'))
    await query.message.reply_text(THINGS_PATH.get('msg_4'))
    await query.message.reply_text(
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


# Блок "Путь вещей"

async def things_path(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Отправляет сообщение и раскладку клавиатуры
    при нажатии кнопки "Путь вещей".
    """
    await update.message.reply_text(THINGS_PATH.get('msg_1'))
    await update.message.reply_text(THINGS_PATH.get('msg_2'))
    await update.message.reply_text(THINGS_PATH.get('msg_3'))
    await update.message.reply_text(THINGS_PATH.get('msg_4'))
    await update.message.reply_text(
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


async def things_path_more_info(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
) -> int:
    """Обработчик меню из раздела "Путь вещей".
    """
    menu_item = update.callback_query.data
    if menu_item == ABOUT_FUND_CALLBACKS.get('more_info'):
        await handle_path_more_info(update.callback_query)
        return PROCESSES_ANATOMY_STATE
    elif menu_item == ABOUT_FUND_CALLBACKS.get('back_to_main_menu'):
        await handle_back_to_main_menu(update.callback_query)
        return MAIN_MENU
    elif menu_item == ABOUT_FUND_CALLBACKS.get('back_to_menu'):
        await handle_back_to_menu(update.callback_query)
        return ABOUT_FUND_MENU_STATE


async def handle_path_more_info(query: CallbackQuery) -> None:
    """Обработчик кнопки "Да, было бы здорово посмотреть!"
    ветки "Путь вещей".
    """
    await query.answer()
    await query.message.reply_text(
        PROCESS_ANATOMY,
        parse_mode=ParseMode.MARKDOWN_V2,
        disable_web_page_preview=True,
        reply_markup=processes_anatomy_markup
    )


# Блок "Анатомия процессов"

async def processes_anatomy(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Отправляет сообщение и раскладку клавиатуры
    при нажатии кнопки "Анатомия процессов".
    """
    await update.message.reply_text(
        PROCESS_ANATOMY,
        parse_mode=ParseMode.MARKDOWN_V2,
        disable_web_page_preview=True,
        reply_markup=processes_anatomy_markup
    )


async def handle_processes_anatomy(query: CallbackQuery) -> None:
    """Обработчик меню из раздела "Анатомия процессов".
    """
    await query.answer()
    await query.message.reply_markdown_v2(
        PROCESS_ANATOMY,
        disable_web_page_preview=True,
        reply_markup=processes_anatomy_markup
    )


async def processes_anatomy_more_info(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
) -> int:
    """Обработчик кнопки "Конечно! Какие?"
    ветки "Анатомия процессов".
    """
    menu_item = update.callback_query.data
    if menu_item == ABOUT_FUND_CALLBACKS.get('more_info'):
        await handle_fund_projects(update.callback_query)
        return FUND_PROJECTS_STATE
    elif menu_item == ABOUT_FUND_CALLBACKS.get('back_to_main_menu'):
        await handle_back_to_main_menu(update.callback_query)
        return MAIN_MENU
    elif menu_item == ABOUT_FUND_CALLBACKS.get('back_to_menu'):
        await handle_back_to_menu(update.callback_query)
        return ABOUT_FUND_MENU_STATE


# Блок "Проекты Фонда"

async def fund_projects(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Отправляет сообщение и раскладку клавиатуры
    при нажатии кнопки "Проекты Фонда".
    """
    await update.message.reply_text(FUND_PROJECTS.get('msg_1'))
    await update.message.reply_text(FUND_PROJECTS.get('msg_2'))
    await update.message.reply_text(FUND_PROJECTS.get('msg_3'))
    await update.message.reply_markdown(
        FUND_PROJECTS.get('msg_4'),
        reply_markup=fund_projects_markup
    )


async def handle_fund_projects(query: CallbackQuery) -> None:
    """Обработчик меню из раздела "Проекты Фонда".
    """
    await query.answer()
    await query.message.reply_text(FUND_PROJECTS.get('msg_1'))
    await query.message.reply_text(FUND_PROJECTS.get('msg_2'))
    await query.message.reply_text(FUND_PROJECTS.get('msg_3'))
    await query.message.reply_markdown(
        FUND_PROJECTS.get('msg_4'),
        reply_markup=fund_projects_markup
    )


async def fund_projects_more_info(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
) -> int:
    """Обработчик кнопки "Почитаю с удовольствием!"
    ветки "Проекты Фонда".
    """
    menu_item = update.callback_query.data
    if menu_item == ABOUT_FUND_CALLBACKS.get('more_info'):
        await handle_annual_reports(update.callback_query)
        return ANNUAL_REPORTS_STATE
    elif menu_item == ABOUT_FUND_CALLBACKS.get('back_to_main_menu'):
        await handle_back_to_main_menu(update.callback_query)
        return MAIN_MENU
    elif menu_item == ABOUT_FUND_CALLBACKS.get('back_to_menu'):
        await handle_back_to_menu(update.callback_query)
        return ABOUT_FUND_MENU_STATE


# Блок "Годовые отчеты"

async def annual_reports(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Отправляет сообщение и раскладку клавиатуры
    при нажатии кнопки "Годовые отчеты".
    """
    await update.message.reply_markdown_v2(
        ANNUAL_REPORTS,
        disable_web_page_preview=True,
        reply_markup=annual_reports_markup
    )


async def handle_annual_reports(query: CallbackQuery) -> None:
    """Обработчик меню из раздела "Годовые отчеты".
    """
    await query.answer()
    await query.message.reply_markdown_v2(
        ANNUAL_REPORTS,
        disable_web_page_preview=True,
        reply_markup=annual_reports_markup
    )


async def annual_reports_more_info(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
) -> int:
    """Обработчик кнопки "Обязательно прочту!"
    ветки "Годовые отчеты".
    """
    await handle_back_to_main_menu(update.callback_query)
    return MAIN_MENU
