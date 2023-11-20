import json

from admin_bot.admin import myModels
from admin_bot.models import (
    AboutFundKeyboard,
    AboutFundText,
    BasicInfoKeyboard,
    BasicInfoText,
    Button,
    ContactListtext,
    FaqText,
    Keyboard,
    Links,
    OnboardingKeyboard,
    OnboardingText,
    QueryPatterns,
    RegFormsText,
    RulesKeyboard,
    RulesText,
    State,
    Text,
)
from django.core.management.base import BaseCommand


RES = {}


class Command(BaseCommand):
    help = 'Try parsing db'

    def handle(self, *args, **options):
        for one_model in myModels:
            result = one_model.objects.values_list(
                'constant_name', 'constant_text', 'constant_description')
            new_result = dict(result)
            RES.update({one_model.__name__: new_result})
        with open('data.json', 'w', encoding='UTF-8') as outfile:
            json.dump(RES, outfile, ensure_ascii=False)
        # result = AboutFundText.objects.values_list('constant_name', 'constant_text')
        # new_result = dict(result)
        # string = (new_result['test'].format(PROCESSES_LINK=PROCESSES_LINK)).replace("\\n", "\n")
        # print(string)
