from telegram import (
    CallbackQuery, MessageEntity, Update
)
from telegram.ext import ContextTypes

from bot.constants.callback import (
    FUND_HISTORY_CALLBACKS
)
from bot.constants.text import (
    ABOUT_FUND_HISTORY,
    BACK_TO_MENU,
    FUND_MISSION
)
from bot.keyboards import (
    about_fund_markup,
    about_fund_section,
    fund_history_markup,
    main_menu_markup
)
from bot.constants.state import (
    ABOUT_FUND_MENU_STATE,
    FUND_MISSION_STATE,
    MENU
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
        pass
    # Анатомия процессов
    elif menu_item == about_fund_section.get('processes_anatomy'):
        pass
    # Годовые отчеты
    elif menu_item == about_fund_section.get('annual_reports'):
        pass


async def about_fund_mission(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
) -> int:
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
                length=len(FUND_MISSION.get('part_5'))
            ),
        ),
        reply_markup=fund_history_markup
    )


async def handle_back_to_main_menu(query: CallbackQuery) -> None:
    await query.message.edit_text("Возвращаемся в главное меню...")
    await query.message.reply_text(
        BACK_TO_MENU, reply_markup=main_menu_markup
    )


async def handle_back_to_menu(query: CallbackQuery) -> None:
    await query.message.reply_text(
        BACK_TO_MENU, reply_markup=about_fund_markup
    )


async def handle_more_info(query: CallbackQuery) -> None:
    pass

async def about_fund_more_info(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    menu_item = update.callback_query.data
    if menu_item == FUND_HISTORY_CALLBACKS.get('more_info'):
        await handle_more_info(update.callback_query)
    elif menu_item == FUND_HISTORY_CALLBACKS.get('back_to_main_menu'):
        await handle_back_to_main_menu(update.callback_query)
        return MENU
    elif menu_item == FUND_HISTORY_CALLBACKS.get('back_to_menu'):
        await handle_back_to_menu(update.callback_query)
        return ABOUT_FUND_MENU_STATE
