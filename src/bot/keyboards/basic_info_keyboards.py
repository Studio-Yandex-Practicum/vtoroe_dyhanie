from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from bot.constants.query_patterns import INFO_PREFIX
from bot.utils.admin_api import get_django_json


# 1. Клавиатура для подраздела "основная информация"
async def basic_information_markup():
    messages = await get_django_json('/basic_info_keyboards/1:4/')
    result = [
        [
            InlineKeyboardButton(
                messages.get(
                    'basic_information_keyboard_organization_structure', ''
                ),
                callback_data=f'{INFO_PREFIX}organization_structure',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('basic_information_keyboard_our_team', ''),
                callback_data=f'{INFO_PREFIX}our_team',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('basic_information_keyboard_social_networks', ''),
                callback_data=f'{INFO_PREFIX}social_networks',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get(
                    'basic_information_keyboard_back_to_main_menu', ''
                ),
                callback_data='back_to_main_menu',
            )
        ],
    ]
    return InlineKeyboardMarkup(result)


# 2. Клавиатура для 'organization_structure'
async def org_structure_markup():
    messages = await get_django_json('/basic_info_keyboards/5:9/')
    org_structure_keyboard = [
        [
            InlineKeyboardButton(
                messages.get('org_structure_keyboard_council', ''),
                callback_data=f'{INFO_PREFIX}council',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('org_structure_keyboard_guardian_council', ''),
                callback_data=f'{INFO_PREFIX}guardian_council',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('org_structure_keyboard_about_departments', ''),
                callback_data=f'{INFO_PREFIX}about_departments',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get(
                    'org_structure_keyboard_basic_information_back', ''
                ),
                callback_data='basic_information_back',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('org_structure_keyboard_back_to_main_menu', ''),
                callback_data='back_to_main_menu',
            )
        ],
    ]
    return InlineKeyboardMarkup(org_structure_keyboard)


# 3. Клавиатура для "Наша команда"
async def our_team_markup():
    messages = await get_django_json('/basic_info_keyboards/10:13/')
    our_team_keyboard = [
        [
            InlineKeyboardButton(
                messages.get('our_team_keyboard_contact_list', ''),
                callback_data=f'{INFO_PREFIX}contact_list',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('our_team_keyboard_org_departmentss', ''),
                callback_data=f'{INFO_PREFIX}org_departmentss',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('our_team_keyboard_basic_information_back', ''),
                callback_data='basic_information_back',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('our_team_keyboard_back_to_main_menu', ''),
                callback_data='back_to_main_menu',
            )
        ],
    ]
    return InlineKeyboardMarkup(our_team_keyboard)


# 4. Клавиатура для "Соцсети Фонда"
async def social_networks_markup():
    messages = await get_django_json('/basic_info_keyboards/14:15/')
    social_networks_keyboard = [
        [
            InlineKeyboardButton(
                messages.get(
                    'social_networks_keyboard_basic_information_back', ''
                ),
                callback_data='basic_information_back',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('social_networks_keyboard_back_to_main_menu', ''),
                callback_data='back_to_main_menu',
            )
        ],
    ]
    return InlineKeyboardMarkup(social_networks_keyboard)


# 5. Клавиатура для "Совет Фонда"
async def council_markup():
    messages = await get_django_json('/basic_info_keyboards/16:23/')
    council_keyboard = [
        [
            InlineKeyboardButton(
                messages.get('council_keyboard_council_question_01', ''),
                callback_data=f'{INFO_PREFIX}council_question_01',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('council_keyboard_council_question_02', ''),
                callback_data=f'{INFO_PREFIX}council_question_02',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('council_keyboard_council_question_03', ''),
                callback_data=f'{INFO_PREFIX}council_question_03',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('council_keyboard_council_question_04', ''),
                callback_data=f'{INFO_PREFIX}council_question_04',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('council_keyboard_council_question_05', ''),
                callback_data=f'{INFO_PREFIX}council_question_05',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('council_keyboard_council_question_06', ''),
                callback_data=f'{INFO_PREFIX}council_question_06',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('council_keyboard_organization_structure', ''),
                callback_data=f'{INFO_PREFIX}organization_structure',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('council_keyboard_back_to_main_menu', ''),
                callback_data='back_to_main_menu',
            )
        ],
    ]
    return InlineKeyboardMarkup(council_keyboard)


# 6. Клавиатура для возвратов из раздела о департаментах
async def departments_final_markup():
    messages = await get_django_json('/basic_info_keyboards/36:37/')
    departments_final_keyboard = [
        [
            InlineKeyboardButton(
                messages.get(
                    'departments_final_keyboard_back_to_main_menu', ''
                ),
                callback_data='back_to_main_menu',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get(
                    'departments_final_keyboard_about_departments', ''
                ),
                callback_data=f'{INFO_PREFIX}about_departments',
            )
        ],
    ]
    return InlineKeyboardMarkup(departments_final_keyboard)


# 7. Клавиатура для "Отделы Фонда"
async def func_departments_keyboard_base():
    messages = await get_django_json('/basic_info_keyboards/22:33/')
    departments_keyboard_base = [
        [
            InlineKeyboardButton(
                messages.get('departments_keyboard_base_department_01', ''),
                callback_data=f'{INFO_PREFIX}department_01',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('departments_keyboard_base_department_02', ''),
                callback_data=f'{INFO_PREFIX}department_02',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('departments_keyboard_base_department_03', ''),
                callback_data=f'{INFO_PREFIX}department_03',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('departments_keyboard_base_department_04', ''),
                callback_data=f'{INFO_PREFIX}department_04',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('departments_keyboard_base_department_05', ''),
                callback_data=f'{INFO_PREFIX}department_05',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('departments_keyboard_base_department_06', ''),
                callback_data=f'{INFO_PREFIX}department_06',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('departments_keyboard_base_department_07', ''),
                callback_data=f'{INFO_PREFIX}department_07',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('departments_keyboard_base_department_08', ''),
                callback_data=f'{INFO_PREFIX}department_08',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('departments_keyboard_base_department_09', ''),
                callback_data=f'{INFO_PREFIX}department_09',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('departments_keyboard_base_department_10', ''),
                callback_data=f'{INFO_PREFIX}department_10',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('council_keyboard_organization_structure', ''),
                callback_data=f'{INFO_PREFIX}organization_structure',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('council_keyboard_back_to_main_menu', ''),
                callback_data='back_to_main_menu',
            )
        ],
    ]
    return InlineKeyboardMarkup(departments_keyboard_base)


# 7.5. Клавиатура для 'departmentss'
async def departmentss_markup():
    messages = await get_django_json('/basic_info_keyboards/24:35/')
    departments_keyboard = [
        [
            InlineKeyboardButton(
                messages.get('departments_keyboard_base_department_01', ''),
                callback_data=f'{INFO_PREFIX}department_01',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('departments_keyboard_base_department_02', ''),
                callback_data=f'{INFO_PREFIX}department_02',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('departments_keyboard_base_department_03', ''),
                callback_data=f'{INFO_PREFIX}department_03',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('departments_keyboard_base_department_04', ''),
                callback_data=f'{INFO_PREFIX}department_04',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('departments_keyboard_base_department_05', ''),
                callback_data=f'{INFO_PREFIX}department_05',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('departments_keyboard_base_department_06', ''),
                callback_data=f'{INFO_PREFIX}department_06',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('departments_keyboard_base_department_07', ''),
                callback_data=f'{INFO_PREFIX}department_07',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('departments_keyboard_base_department_08', ''),
                callback_data=f'{INFO_PREFIX}department_08',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('departments_keyboard_base_department_09', ''),
                callback_data=f'{INFO_PREFIX}department_09',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('departments_keyboard_base_department_10', ''),
                callback_data=f'{INFO_PREFIX}department_10',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('departments_keyboard_our_team', ''),
                callback_data=f'{INFO_PREFIX}our_team',
            )
        ],
        [
            InlineKeyboardButton(
                messages.get('departments_keyboard_back_to_main_menu', ''),
                callback_data='back_to_main_menu',
            )
        ],
    ]
    return InlineKeyboardMarkup(departments_keyboard)


# 8. Клавиатура для 'guardian_council'
async def guardian_council_markup():
    messages = await get_django_json('/basic_info_keyboards/38/')
    guardian_council_keyboard = [
        [
            InlineKeyboardButton(
                messages.get('guardian_council_keyboard', ''),
                callback_data=f'{INFO_PREFIX}organization_structure',
            )
        ],
    ]
    return InlineKeyboardMarkup(guardian_council_keyboard)
