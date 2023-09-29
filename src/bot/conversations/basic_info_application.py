from telegram import (
    Update,
    CallbackQuery,
)
from telegram.ext import (
    ContextTypes,
)

from bot.constants.state import BASIC_INFORMATION
from bot.constants import basic_info_text
from bot.conversations.menu_application import handle_back_to_main_menu
from bot.basic_info_keyboards import (
    basic_information_markup,
    org_structure_markup,
    our_team_markup,
    social_networks_markup,
    guardian_council_markup,
    council_markup,
    departments_final_markup,
    departments_markup,
    departmentss_markup,
)
from bot.constants import basic_info_text
from bot.constants.state import (
    MAIN_MENU,
    BASIC_INFORMATION,
)
from bot.constants.text import BACK_TO_MENU
from bot.keyboards import (
    main_menu_markup,
)
from bot.utils import safe_edit_text


@safe_edit_text
async def handle_organization_structure(query: CallbackQuery) -> None:
    """Обработка клавиатуры Организационная структура."""
    query_data = query.data

    if query_data == "organization_structure":
        await query.message.edit_text(
            basic_info_text.ORGANIZATION_MESSAGE,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=org_structure_markup,
        )

    elif query_data == "council":
        await query.message.edit_text(
            basic_info_text.COUNCIL_INTRODUCTION_MESSAGE,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=council_markup,
        )
    elif query_data in basic_info_text.COUNCIL_QUESTION_LIST:
        await handle_council(query)

    elif query_data == "guardian_council":
        await query.message.edit_text(
            basic_info_text.GARDIAN_COUNCIL_INTRODUCTION_MESSAGE,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=guardian_council_markup,
        )

    elif query_data == "departments":
        await query.message.edit_text(
            text=basic_info_text.DEPARTMENTS, reply_markup=departments_markup
        )
    elif query_data in basic_info_text.DEPARTMENT_LIST:
        await handle_departments(query)


@safe_edit_text
async def handle_our_team(query: CallbackQuery) -> None:
    """Обработка кнопки Наша команда."""
    query_data = query.data

    if query_data == "our_team":
        await query.message.edit_text(
            basic_info_text.OUR_TEAM_MESSAGE,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=our_team_markup,
        )

    elif query_data == "contact_list":
        await query.message.edit_text(
            "Информация о контактах.", reply_markup=our_team_markup
        )
    elif query_data == "departmentss":
        await query.message.edit_text(
            text=basic_info_text.DEPARTMENTS, reply_markup=departmentss_markup
        )


async def handle_social_networks(query: CallbackQuery) -> None:
    """Обработка клавиатуры Социальные сети."""
    await query.message.edit_text(
        basic_info_text.FUND_NEWS,
        disable_web_page_preview=True,
        reply_markup=social_networks_markup,
    )


@safe_edit_text
async def handle_council(query: CallbackQuery) -> None:
    """Обработка клавиатуры совета Фонда."""
    query_data = query.data

    if query_data == "council_question_01":
        await query.message.edit_text(
            basic_info_text.COUNCIL_ANSWER_01,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=council_markup,
        )
    elif query_data == "council_question_02":
        await query.message.edit_text(
            basic_info_text.COUNCIL_ANSWER_02,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=council_markup,
        )
    elif query_data == "council_question_03":
        await query.message.edit_text(
            basic_info_text.COUNCIL_ANSWER_03,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=council_markup,
        )
    elif query_data == "council_question_04":
        await query.message.edit_text(
            basic_info_text.COUNCIL_ANSWER_04,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=council_markup,
        )
    elif query_data == "council_question_05":
        await query.message.edit_text(
            basic_info_text.COUNCIL_ANSWER_05,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=council_markup,
        )
    elif query_data == "council_question_06":
        await query.message.edit_text(
            basic_info_text.COUNCIL_ANSWER_06,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=council_markup,
        )


async def handle_departments(query: CallbackQuery) -> None:
    """Обработка клавиатуры отделов Фонда."""
    query_data = query.data
    if query_data == "department_01":
        await query.message.edit_text(
            basic_info_text.DEPARTMENT_01,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=departments_final_markup,
        )
    elif query_data == "department_02":
        await query.message.edit_text(
            basic_info_text.DEPARTMENT_02,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=departments_final_markup,
        )
    elif query_data == "department_03":
        await query.message.edit_text(
            basic_info_text.DEPARTMENT_03,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=departments_final_markup,
        )
    elif query_data == "department_04":
        await query.message.edit_text(
            basic_info_text.DEPARTMENT_04,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=departments_final_markup,
        )
    elif query_data == "department_05":
        await query.message.edit_text(
            basic_info_text.DEPARTMENT_05,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=departments_final_markup,
        )
    elif query_data == "department_06":
        await query.message.edit_text(
            basic_info_text.DEPARTMENT_06,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=departments_final_markup,
        )
    elif query_data == "department_07":
        await query.message.edit_text(
            basic_info_text.DEPARTMENT_07,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=departments_final_markup,
        )
    elif query_data == "department_08":
        await query.message.edit_text(
            basic_info_text.DEPARTMENT_08,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=departments_final_markup,
        )
    elif query_data == "department_09":
        await query.message.edit_text(
            basic_info_text.DEPARTMENT_09,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=departments_final_markup,
        )
    elif query_data == "department_10":
        await query.message.edit_text(
            basic_info_text.DEPARTMENT_10,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=departments_final_markup,
        )


async def handle_basic_information_back(query: CallbackQuery) -> None:
    """Обработка кнопки Возврата в меню Основной информации."""
    await query.message.edit_text(
        "Выберите действие:", reply_markup=basic_information_markup
    )


async def basic_information_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    """Обработка клавиатуры Основной информации."""
    query = update.callback_query
    await query.answer()
    query_data = query.data

    if query_data in [
        "organization_structure",
        "council",
        "guardian_council",
        "departments",
        *basic_info_text.COUNCIL_QUESTION_LIST,
        *basic_info_text.DEPARTMENT_LIST,
    ]:
        await handle_organization_structure(query)
    elif query_data in ["our_team", "contact_list", "departmentss"]:
        await handle_our_team(query)
    elif query_data == "social_networks":
        await handle_social_networks(query)
    elif query_data == "basic_information_back":
        await handle_basic_information_back(query)
    elif query_data == "main_menu":
        return await handle_back_to_main_menu(query)
    return BASIC_INFORMATION
