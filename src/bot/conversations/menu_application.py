from telegram import (
    CallbackQuery,
    MessageEntity,
    Update
)
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from bot.constants.callback import (
    ABOUT_FUND_CALLBACKS
)
from bot.constants.state import (
    ABOUT_FUND_MENU_STATE,
    FUND_MISSION_STATE,
    FUND_PROJECTS_STATE,
    MENU,
    PROCESSES_ANATOMY_STATE,
    THINGS_PATH_STATE,
    ANNUAL_REPORTS_STATE
)
from bot.constants.text import (
    ABOUT_FUND_HISTORY,
    ANNUAL_REPORTS,
    BACK_TO_MENU,
    FUND_MISSION,
    FUND_PROJECTS,
    PROCESS_ANATOMY,
    THINGS_PATH,
    FUND_PROJECTS,
    ANNUAL_REPORTS
)
from bot.keyboards import (
    about_fund_markup,
    about_fund_section,
    annual_reports_markup,
    fund_history_markup,
    fund_projects_markup,
    main_menu_markup,
    processes_anatomy_markup,
    things_path_markup,
    fund_projects_markup,
    annual_reports_markup
)


async def about_fund_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> int:
    await update.message.reply_text(ABOUT_FUND_HISTORY.get('part_1'))
    await update.message.reply_text(ABOUT_FUND_HISTORY.get('part_2'))
    await update.message.reply_text(
        ABOUT_FUND_HISTORY.get('part_3'),
        reply_markup=about_fund_markup
    )
    return ABOUT_FUND_MENU_STATE


async def about_fund_menu_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> int:
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
        await annual_reports(update, context)
        return ANNUAL_REPORTS_STATE


async def handle_back_to_main_menu(query: CallbackQuery) -> None:
    """Обработчик нажатия кнопки В главное меню"""
    await query.message.edit_text('Возвращаемся в главное меню...')
    await query.message.reply_text(
        BACK_TO_MENU, reply_markup=main_menu_markup
    )


async def handle_back_to_menu(query: CallbackQuery) -> None:
    """Обработчик нажатия кнопки В меню раздела"""
    await query.message.edit_text(
        'Возвращаемся в меню раздела «О фонде»...'
    )
    await query.message.reply_text(
        BACK_TO_MENU, reply_markup=about_fund_markup
    )


async def about_fund_mission(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Отправляет сообщение и раскладку клавиатуры
    при нажатии кнопки Миссия и основная цель
    """
    await update.message.reply_text(FUND_MISSION.get('part_1'))
    await update.message.reply_text(FUND_MISSION.get('part_2'))
    await update.message.reply_text(FUND_MISSION.get('part_3'))
    await update.message.reply_text(FUND_MISSION.get('part_4'))
    await update.message.reply_text(FUND_MISSION.get('part_5'))
    await update.message.reply_text(
        FUND_MISSION.get('part_6'),
        entities=(
            MessageEntity(
                type=MessageEntity.BOLD,
                offset=0,
                length=len(FUND_MISSION.get('part_6'))
            ),
        ),
        reply_markup=fund_history_markup
    )


async def handle_back_to_main_menu(query: CallbackQuery) -> None:
    await query.answer()
    await query.message.edit_text('Возвращаемся в главное меню...')
    await query.message.reply_text(
        BACK_TO_MENU, reply_markup=main_menu_markup
    )


async def handle_back_to_menu(query: CallbackQuery) -> None:
    await query.answer()
    await query.message.edit_text(
        'Возвращаемся в меню раздела «О фонде»...'
    )
    await query.message.reply_text(
        BACK_TO_MENU, reply_markup=about_fund_markup
    )


async def handle_mission_more_info(query: CallbackQuery) -> None:
    # Идет дублирование кода с методом things_path
    # Пока не нашел способ исправить
    await query.answer()
    await query.message.reply_text(THINGS_PATH.get('part_1'))
    await query.message.reply_text(THINGS_PATH.get('part_2'))
    await query.message.reply_text(THINGS_PATH.get('part_3'))
    await query.message.reply_text(THINGS_PATH.get('part_4'))
    await query.message.reply_text(
        THINGS_PATH.get('part_5'),
        entities=(
            MessageEntity(
                type=MessageEntity.BOLD,
                offset=0,
                length=len(THINGS_PATH.get('part_5'))
            ),
        ),
        reply_markup=things_path_markup
    )


async def about_fund_more_info(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
) -> int:
    """Обработчик меню из раздела Миссия и основная цель"""
    menu_item = update.callback_query.data
    if menu_item == ABOUT_FUND_CALLBACKS.get('more_info'):
        await handle_mission_more_info(update.callback_query)
        return THINGS_PATH_STATE
    elif menu_item == ABOUT_FUND_CALLBACKS.get('back_to_main_menu'):
        await handle_back_to_main_menu(update.callback_query)
        return MENU
    elif menu_item == ABOUT_FUND_CALLBACKS.get('back_to_menu'):
        await handle_back_to_menu(update.callback_query)
        return ABOUT_FUND_MENU_STATE


async def things_path(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Отправляет сообщение и раскладку клавиатуры
    при нажатии кнопки Путь вещей
    """
    await update.message.reply_text(THINGS_PATH.get('part_1'))
    await update.message.reply_text(THINGS_PATH.get('part_2'))
    await update.message.reply_text(THINGS_PATH.get('part_3'))
    await update.message.reply_text(THINGS_PATH.get('part_4'))
    await update.message.reply_text(
        THINGS_PATH.get('part_5'),
        entities=(
            MessageEntity(
                type=MessageEntity.BOLD,
                offset=0,
                length=len(THINGS_PATH.get('part_5'))
            ),
        ),
        reply_markup=things_path_markup
    )


async def things_path_more_info(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
) -> int:
    menu_item = update.callback_query.data
    if menu_item == ABOUT_FUND_CALLBACKS.get('more_info'):
        await handle_path_more_info(update.callback_query)
        return PROCESSES_ANATOMY_STATE
    elif menu_item == ABOUT_FUND_CALLBACKS.get('back_to_main_menu'):
        await handle_back_to_main_menu(update.callback_query)
        return MENU
    elif menu_item == ABOUT_FUND_CALLBACKS.get('back_to_menu'):
        await handle_back_to_menu(update.callback_query)
        return ABOUT_FUND_MENU_STATE


async def handle_path_more_info(query: CallbackQuery) -> None:
    await query.answer()
    await query.message.reply_text(
        PROCESS_ANATOMY,
        parse_mode=ParseMode.MARKDOWN_V2,
        disable_web_page_preview=True,
        reply_markup=processes_anatomy_markup
    )


async def processes_anatomy(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Отправляет сообщение и раскладку клавиатуры
    при нажатии кнопки Анатомия процессов
    """
    await update.message.reply_text(
        PROCESS_ANATOMY,
        parse_mode=ParseMode.MARKDOWN_V2,
        disable_web_page_preview=True,
        reply_markup=processes_anatomy_markup
    )


async def handle_processes_anatomy(query: CallbackQuery) -> None:
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
    menu_item = update.callback_query.data
    if menu_item == ABOUT_FUND_CALLBACKS.get('more_info'):
        await handle_fund_projects(update.callback_query)
        return FUND_PROJECTS_STATE
    elif menu_item == ABOUT_FUND_CALLBACKS.get('back_to_main_menu'):
        await handle_back_to_main_menu(update.callback_query)
        return MENU
    elif menu_item == ABOUT_FUND_CALLBACKS.get('back_to_menu'):
        await handle_back_to_menu(update.callback_query)
        return ABOUT_FUND_MENU_STATE


async def handle_fund_projects(query: CallbackQuery) -> None:
    """
    Функция для перехода в "Проекты фонда" из "Анатомия процессов".
    """
    await query.answer()
    await query.message.reply_text(FUND_PROJECTS.get('msg_1'))
    await query.message.reply_text(FUND_PROJECTS.get('msg_2'))
    await query.message.reply_text(FUND_PROJECTS.get('msg_3'))
    await query.message.reply_markdown(
        FUND_PROJECTS.get('msg_4'),
        reply_markup=fund_projects_markup
    )


async def fund_projects(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
) -> None:
    """
    Функция для перехода в "Проекты фонда" из меню "О Фонде.
    """
    await update.message.reply_text(FUND_PROJECTS.get('msg_1'))
    await update.message.reply_text(FUND_PROJECTS.get('msg_2'))
    await update.message.reply_text(FUND_PROJECTS.get('msg_3'))
    await update.message.reply_markdown(
        FUND_PROJECTS.get('msg_4'),
        reply_markup=fund_projects_markup
    )


async def fund_projects_more_info(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
) -> int:
    """
    Клавиатура для кнопки «Проекты фонда».
    """
    menu_item = update.callback_query.data
    if menu_item == ABOUT_FUND_CALLBACKS.get('more_info'):
        await handle_annual_reports(update.callback_query)
        return ANNUAL_REPORTS_STATE
    elif menu_item == ABOUT_FUND_CALLBACKS.get('back_to_main_menu'):
        await handle_back_to_main_menu(update.callback_query)
        return MENU
    elif menu_item == ABOUT_FUND_CALLBACKS.get('back_to_menu'):
        await handle_back_to_menu(update.callback_query)
        return ABOUT_FUND_MENU_STATE


async def annual_reports(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
) -> None:
    """
     Функция для перехода в "Годовые отчеты" из меню "О Фонде".
    """
    await update.message.reply_markdown_v2(
        ANNUAL_REPORTS,
        disable_web_page_preview=True,
        reply_markup=annual_reports_markup
    )


async def handle_annual_reports(query: CallbackQuery) -> None:
    """
    Функция для перехода в "Годовые отчеты" из "Проекты фонда".
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
    """
    Колбэк для кнопки «Обязательно прочту».
    """
    await handle_back_to_main_menu(update.callback_query)
    return MENU
