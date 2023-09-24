from telegram import (
    Update,
    CallbackQuery,
)
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
)

from bot.constants.state import (
    CHECK,
    MAIN_MENU,
    BASIC_INFORMATION,
)
from bot.constants.text import (
    START_MESSAGE,
    FAILED_THE_TEST,
    PASSED_THE_TEST,
    STICKER_ID,
    BASIC_INFORMATION_MENU,
    FUND_NEWS,
    OUR_TEAM_MESSAGE,
    ORGANIZATION_MESSAGE,
    BACK_TO_THE_MENU,
    COUNCIL_INTRODUCTION_MESSAGE,
    COUNCIL_ANSWER_01,
    COUNCIL_ANSWER_02,
    COUNCIL_ANSWER_03,
    COUNCIL_ANSWER_04,
    COUNCIL_ANSWER_05,
    COUNCIL_ANSWER_06,
    GARDIAN_COUNCIL_INTRODUCTION_MESSAGE,
    DEPARTMENT_01,
    DEPARTMENT_02,
    DEPARTMENT_03,
    DEPARTMENT_04,
    DEPARTMENT_05,
    DEPARTMENT_06,
    DEPARTMENT_07,
    DEPARTMENT_08,
    DEPARTMENT_09,
    DEPARTMENT_10,
    DEPARTMENTS,
)
from bot.keyboards import (
    main_menu_markup,
    basic_information_markup,
    org_structure_markup,
    our_team_markup,
    social_networks_markup,
    guardian_council_markup,
    council_markup,
    departments_final_markup,
    departments_markup,
)
from bot.core.settings import settings

async def greeting_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    """Базовая функция начинающая диалог с юзером и открывающий доступ к conv_handler."""
    await update.message.reply_text(START_MESSAGE)
    return CHECK


async def check_the_secret_word_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    """Функция проверяющая доступ к боту по секретному слову."""
    text = update.message.text
    if text.lower() != settings.secret_word.lower():
        await update.message.reply_text(FAILED_THE_TEST)
        return CHECK
    await update.message.reply_sticker(STICKER_ID)
    await update.message.reply_text(
        PASSED_THE_TEST, reply_markup=main_menu_markup
    )
    return MAIN_MENU


async def main_menu_actions_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    user_input = update.message.text

    if user_input == "Основная информация":
        await update.message.reply_text(
            BASIC_INFORMATION_MENU, reply_markup=basic_information_markup
        )
        return BASIC_INFORMATION

    # Добавить обработку других кнопок.

    return MAIN_MENU


# Обработка структуры организации
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
    elif query_data in [
        "council_question_01",
        "council_question_02",
        "council_question_03",
        "council_question_04",
        "council_question_05",
        "council_question_06",
    ]:
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
    elif query_data in [
        "department_01",
        "department_02",
        "department_03",
        "department_04",
        "department_05",
        "department_06",
        "department_07",
        "department_08",
        "department_09",
        "department_10",
    ]:
        await handle_departments(query)


# Информация о команде.
async def handle_our_team(query: CallbackQuery) -> None:
    query_data = query.data

    if query_data == "our_team":
        await query.message.edit_text(
            OUR_TEAM_MESSAGE,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=our_team_markup,
        )
        # await query.message.reply_text(OUR_TEAM_SECOND_MESSAGE, reply_markup=our_team_markup)

    elif query_data == "contact_list":
        await query.message.edit_text(
            "Информация о контактах.", reply_markup=our_team_markup
        )


async def handle_schedule(query: CallbackQuery) -> None:
    # Заменить на информацию о расписании работы фонда
    await query.answer()


# Информация о социальных сетях.
async def handle_social_networks(query: CallbackQuery) -> None:
    await query.message.edit_text(
        FUND_NEWS,
        disable_web_page_preview=True,
        reply_markup=social_networks_markup,
    )


# Информация о совете Фонда
async def handle_council(query: CallbackQuery) -> None:
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


# Информация об отделах фонда
async def handle_departments(query: CallbackQuery) -> None:
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


# возвращение в подраздел "основная информация".
async def handle_basic_information_back(query: CallbackQuery) -> None:
    await query.message.edit_text(
        "Выберите действие:", reply_markup=basic_information_markup
    )


# Возвращение в главное меню.
async def handle_main_menu(query: CallbackQuery) -> int:
    await query.message.edit_text("Возвращаемся в главное меню...")
    await query.message.reply_text(
        BACK_TO_THE_MENU, reply_markup=main_menu_markup
    )
    return MAIN_MENU


# Обработка команды основного меню "Основная информация"
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
        "departments",
        "council_question_01",
        "council_question_02",
        "council_question_03",
        "council_question_04",
        "council_question_05",
        "council_question_06",
        "department_01",
        "department_02",
        "department_03",
        "department_04",
        "department_05",
        "department_06",
        "department_07",
        "department_08",
        "department_09",
        "department_10",
    ]:
        await handle_organization_structure(query)
    elif query_data in ["our_team", "contact_list"]:
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


async def done_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> int:
    """Функция заканчивающая работу бота. После её работы, бот будет принимать только команду /start."""
    await update.message.reply_text("Возвращайтесь, буду рад пообщаться!")
    return ConversationHandler.END
