'''Модуль с обработчиками сообщений и кнопок блока "О Фонде".

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
'''

import sys
import requests
from telegram import CallbackQuery, Message, Update
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from bot.constants.query_patterns import ABOUT_PREFIX
from bot.keyboards.about_fund_keyboards import (
    about_fund_section,
    annual_reports_markup,
    func_navigation_menu,
    fund_projects_markup,
    processes_anatomy_markup,
    things_path_markup,
)
from bot.utils import send_message
from bot.utils import get_django_json


async def handle_back_to_menu(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработчик нажатия кнопки "В меню раздела".'''
    query = update.callback_query
    await query.answer()
    await query.message.edit_text('Возвращаемся в меню раздела «О фонде»...')
    message_data = await get_django_json(
        'http://127.0.0.1:8000/text/10/')
    back_to_menu_text = message_data.get("BACK_TO_MENU", "")
    await query.message.reply_text(
        back_to_menu_text,
        reply_markup=await about_fund_section()
    )


async def about_fund_menu_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработчик кнопок основного меню блока "О Фонде".'''
    message_data = await get_django_json(
        'http://127.0.0.1:8000/about_fund_keyboards/3:7/')
    menu_item = update.message.text
    key_message_data = next(
        (
            key for key,
            value in message_data.items() if value == menu_item), None)
    function_to_call = getattr(sys.modules[__name__], key_message_data, None)
    await function_to_call(update, context)


async def about_fund_inline_btns_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработчик inline кнопок всех меню блока "О Фонде".'''
    query = update.callback_query
    menu_item = query.data
    await query.answer()
    await about_inline_handlers.get(menu_item)(query)


# Блок "Миссия и основная цель"
async def send_about_fund_message(message: Message) -> None:
    '''Отправляет сообщение и раскладку клавиатуры
    при нажатии кнопки "Миссия и основная цель".
    '''
    message_data = await get_django_json(
        'http://127.0.0.1:8000/about_fund_text/4:9/')
    await send_message(
        message=message,
        message_text_value=message_data,
        reply_markup=await func_navigation_menu(),
    )


async def about_fund_mission(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработчик кнопки "Миссия и основная цель".'''
    await send_about_fund_message(update.message)


async def handle_mission_more_info(query: CallbackQuery) -> None:
    '''Обработчик кнопки "Конечно! Расскажи подробнее"
    ветки "Миссия и основная цель".
    '''
    # Спрятать inline-клавиатуру после нажатия кнопки
    # await query.edit_message_reply_markup()
    await query.answer()
    await send_things_path_message(query.message)


# Блок "Путь вещей"


async def send_things_path_message(message: Message) -> None:
    '''Отправляет сообщение и раскладку клавиатуры
    при нажатии кнопки "Путь вещей".
    '''
    message_data = await get_django_json(
        'http://127.0.0.1:8000/about_fund_text/10:14/')
    await send_message(
        message=message,
        message_text_value=message_data,
        reply_markup=await things_path_markup(),
    )


async def things_path(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработчик кнопки "Путь вещей".'''
    await send_things_path_message(update.message)


async def handle_path_more_info(query: CallbackQuery) -> None:
    '''Обработчик кнопки "Да, было бы здорово посмотреть!"
    ветки "Путь вещей".
    '''
    # Спрятать inline-клавиатуру после нажатия кнопки
    # await query.edit_message_reply_markup()
    await query.answer()
    await send_processes_anatomy_message(query.message)


# Блок "Анатомия процессов"


async def send_processes_anatomy_message(message: Message) -> None:
    '''Отправляет сообщение и раскладку клавиатуры
    при нажатии кнопки "Анатомия процессов".
    '''
    message_data = await get_django_json(
        'http://127.0.0.1:8000/about_fund_text/15:22/')
    processes_anatomy_text = message_data.get("PROCESS_ANATOMY", "")
    processes_anatomy_link = message_data.get("PROCESSES_LINK", "")
    processes_anatomy_text = processes_anatomy_text.format(
        PROCESSES_LINK=processes_anatomy_link
        )
    await message.reply_text(
        processes_anatomy_text,
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True,
        reply_markup=await processes_anatomy_markup(),
    )


async def processes_anatomy(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработчик кнопки "Анатомия процессов".'''
    await send_processes_anatomy_message(update.message)


async def handle_process_anatomy_more_info(query: CallbackQuery) -> None:
    '''Обработчик кнопки "Конечно! Какие?"
    ветки "Анатомия процессов".
    '''
    # Спрятать inline-клавиатуру после нажатия кнопки
    # await query.edit_message_reply_markup()
    await query.answer()
    await send_fund_projects_message(query.message)


# Блок "Проекты Фонда"


async def send_fund_projects_message(message: Message) -> None:
    '''Отправляет сообщение и раскладку клавиатуры
    при нажатии кнопки "Проекты Фонда".
    '''
    message_data = await get_django_json(
        'http://127.0.0.1:8000/about_fund_text/16:19/')
    await send_message(
            message=message,
            message_text_value=message_data,
            reply_markup=await fund_projects_markup(),
        )


async def fund_projects(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработчик кнопки "Проекты Фонда".'''
    await send_fund_projects_message(update.message)


async def handle_projects_more_info(query: CallbackQuery) -> None:
    '''Обработчик кнопки "Почитаю с удовольствием!"
    ветки "Проекты Фонда".
    '''
    await query.answer()
    await send_annual_reports_message(query.message)


# Блок "Годовые отчеты"
async def send_annual_reports_message(message: Message) -> None:
    '''Отправляет сообщение и раскладку клавиатуры
    при нажатии кнопки "Годовые отчеты".
    '''
    message_data = await get_django_json(
        'http://127.0.0.1:8000/about_fund_text/20:21/')
    annual_reports_text = message_data.get("ANNUAL_REPORTS", "")
    annual_reports_link = message_data.get("ANNUAL_REPORTS_LINK", "")
    annual_reports_text = annual_reports_text.format(
        ANNUAL_REPORTS_LINK=annual_reports_link
        )

    await message.reply_text(
        text=annual_reports_text,
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True,
        reply_markup=await annual_reports_markup(),
    )


async def annual_reports(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    '''Обработчик кнопки "Годовые отчеты".'''
    await send_annual_reports_message(update.message)


about_inline_handlers = {
    f'{ABOUT_PREFIX}more_info_mission': handle_mission_more_info,
    f'{ABOUT_PREFIX}more_info_path': handle_path_more_info,
    f'{ABOUT_PREFIX}more_info_processes': handle_process_anatomy_more_info,
    f'{ABOUT_PREFIX}more_info_projects': handle_projects_more_info,
}


def register_handlers(app: Application) -> None:
    response = requests.get('http://127.0.0.1:8000/about_fund_keyboards/3:8/')
    messages = response.json()
    about_fund_text = [text for key, text in messages.items()]
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
            filters.Text(about_fund_text), about_fund_menu_callback
        )
    )
