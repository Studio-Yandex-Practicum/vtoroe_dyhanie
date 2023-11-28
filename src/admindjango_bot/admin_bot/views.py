from admin_bot.models import (
    AboutFundKeyboard,
    AboutFundText,
    BasicInfoKeyboard,
    BasicInfoText,
    Button,
    ContactListKeyboard,
    ContactListText,
    FaqText,
    Keyboard,
    Links,
    OnboardingKeyboard,
    OnboardingText,
    RegFormsText,
    RulesKeyboard,
    RulesText,
    Text,
)
from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404


DICT_MODELS = {
    'about_fund_text': AboutFundText,
    'about_fund_keyboards': AboutFundKeyboard,
    'basic_info_text': BasicInfoText,
    'basic_info_keyboards': BasicInfoKeyboard,
    'button': Button,
    'contact_list_keyboards': ContactListKeyboard,
    'contact_list_text': ContactListText,
    'faq_text': FaqText,
    'keyboards': Keyboard,
    'links': Links,
    'onboarding_keyboards': OnboardingKeyboard,
    'onboarding_text': OnboardingText,
    'reg_forms_text': RegFormsText,
    'rules_keyboards': RulesKeyboard,
    'rules_text': RulesText,
    'text': Text,
}


def get_constants(request, model_name, start_id, end_id):
    constants = get_list_or_404(
        DICT_MODELS[model_name], pk__in=(range(start_id, end_id + 1))
    )
    constant_data = {}
    for constant in constants:
        constant_data.update(
            {
                constant.constant_name: constant.constant_text,
            }
        )
    return JsonResponse(constant_data, safe=False)


def get_constant(request, model_name, id):
    constant = get_object_or_404(DICT_MODELS[model_name], pk=id)
    constant_data = {constant.constant_name: constant.constant_text}
    return JsonResponse(constant_data, safe=False)


def list_constant(request, model_name):
    constant = DICT_MODELS[model_name].objects.values_list(
        'constant_name', 'constant_text'
    )
    new_result = dict(constant)
    return JsonResponse(new_result, safe=False)
