from telegram import (
    Update,
    CallbackQuery,
)
from telegram.ext import (
    ContextTypes,
)

from bot.constants.state import (
    MAIN_MENU, BASIC_INFORMATION,
)
from bot.constants.basic_info_text import (
    FUND_NEWS,
    OUR_TEAM_MESSAGE,
    ORGANIZATION_MESSAGE,
    COUNCIL_INTRODUCTION_MESSAGE,
    COUNCIL_QUESTION_LIST,
    COUNCIL_ANSWER_01,
    COUNCIL_ANSWER_02,
    COUNCIL_ANSWER_03,
    COUNCIL_ANSWER_04,
    COUNCIL_ANSWER_05,
    COUNCIL_ANSWER_06,
    GARDIAN_COUNCIL_INTRODUCTION_MESSAGE,
    DEPARTMENTS, DEPARTMENT_LIST,
    DEPARTMENT_01, DEPARTMENT_02, DEPARTMENT_03,
    DEPARTMENT_04, DEPARTMENT_05, DEPARTMENT_06,
    DEPARTMENT_07, DEPARTMENT_08, DEPARTMENT_09,
    DEPARTMENT_10,
)
from bot.constants.text import (
    BACK_TO_THE_MENU,
)
from bot.basic_info_keyboards import (
    basic_information_markup,
    org_structure_markup,
    our_team_markup,
    social_networks_markup,
    guardian_council_markup,
    council_markup,
    departments_final_markup,
    departments_markup,
)
from bot.keyboards import (
    main_menu_markup,
)


async def handle_organization_structure(query: CallbackQuery) -> None:
    query_data = query.data

    if query_data == "organization_structure":
        await query.message.edit_text(
            ORGANIZATION_MESSAGE,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=org_structure_markup,
        )

    elif query_data == "council":
        await query.message.edit_text(
            COUNCIL_INTRODUCTION_MESSAGE,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=council_markup,
        )
    elif query_data in COUNCIL_QUESTION_LIST:
        await handle_council(query)

    elif query_data == "guardian_council":
        await query.message.edit_text(
            GARDIAN_COUNCIL_INTRODUCTION_MESSAGE,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=guardian_council_markup,
        )

    elif query_data == "departments":
        await query.message.edit_text(
            text=DEPARTMENTS,
            reply_markup=departments_markup
        )
    elif query_data in DEPARTMENT_LIST:
        await handle_departments(query)


async def handle_our_team(query: CallbackQuery) -> None:
    query_data = query.data

    if query_data == "our_team":
        await query.message.edit_text(
            OUR_TEAM_MESSAGE,
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
            text=DEPARTMENTS,
            reply_markup=departments_markup
        )


async def handle_schedule(query: CallbackQuery) -> None:
    # Заменить на информацию о расписании работы фонда
    await query.answer()


async def handle_social_networks(query: CallbackQuery) -> None:
    await query.message.edit_text(
        FUND_NEWS,
        disable_web_page_preview=True,
        reply_markup=social_networks_markup,
    )


async def handle_council(query: CallbackQuery) -> None:
    """Обработка клавиатуры совета Фонда."""
    query_data = query.data

    if query_data == "council_question_01":
        await query.message.edit_text(
            COUNCIL_ANSWER_01,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=council_markup,
        )
    elif query_data == "council_question_02":
        await query.message.edit_text(
            COUNCIL_ANSWER_02,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=council_markup,
        )
    elif query_data == "council_question_03":
        await query.message.edit_text(
            COUNCIL_ANSWER_03,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=council_markup,
        )
    elif query_data == "council_question_04":
        await query.message.edit_text(
            COUNCIL_ANSWER_04,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=council_markup,
        )
    elif query_data == "council_question_05":
        await query.message.edit_text(
            COUNCIL_ANSWER_05,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=council_markup,
        )
    elif query_data == "council_question_06":
        await query.message.edit_text(
            COUNCIL_ANSWER_06,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=council_markup,
        )


async def handle_departments(query: CallbackQuery) -> None:
    """Обработка клавиатуры отделов Фонда."""
    query_data = query.data
    if query_data == "department_01":
        await query.message.edit_text(
            DEPARTMENT_01,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=departments_final_markup,
        )
    elif query_data == "department_02":
        await query.message.edit_text(
            DEPARTMENT_02,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=departments_final_markup,
        )
    elif query_data == "department_03":
        await query.message.edit_text(
            DEPARTMENT_03,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=departments_final_markup,
        )
    elif query_data == "department_04":
        await query.message.edit_text(
            DEPARTMENT_04,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=departments_final_markup,
        )
    elif query_data == "department_05":
        await query.message.edit_text(
            DEPARTMENT_05,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=departments_final_markup,
        )
    elif query_data == "department_06":
        await query.message.edit_text(
            DEPARTMENT_06,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=departments_final_markup,
        )
    elif query_data == "department_07":
        await query.message.edit_text(
            DEPARTMENT_07,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=departments_final_markup,
        )
    elif query_data == "department_08":
        await query.message.edit_text(
            DEPARTMENT_08,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=departments_final_markup,
        )
    elif query_data == "department_09":
        await query.message.edit_text(
            DEPARTMENT_09,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=departments_final_markup,
        )
    elif query_data == "department_10":
        await query.message.edit_text(
            DEPARTMENT_10,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=departments_final_markup,
        )


async def handle_basic_information_back(query: CallbackQuery) -> None:
    await query.message.edit_text(
        "Выберите действие:", reply_markup=basic_information_markup
    )


async def handle_main_menu(query: CallbackQuery) -> int:
    await query.message.edit_text("Возвращаемся в главное меню...")
    await query.message.reply_text(
        BACK_TO_THE_MENU, reply_markup=main_menu_markup
    )
    return MAIN_MENU


async def basic_information_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    query = update.callback_query
    query_data = query.data

    if query_data in [
        "organization_structure",
        "council",
        "guardian_council",
        "departments", *COUNCIL_QUESTION_LIST, *DEPARTMENT_LIST
    ]:
        await handle_organization_structure(query)
    elif query_data in ["our_team", "contact_list", "departmentss"]:
        await handle_our_team(query)
    elif query_data == "schedule":
        await handle_schedule(query)
    elif query_data == "social_networks":
        await handle_social_networks(query)
    elif query_data == "basic_information_back":
        await handle_basic_information_back(query)
    elif query_data == "main_menu":
        return await handle_main_menu(query)
    return BASIC_INFORMATION
