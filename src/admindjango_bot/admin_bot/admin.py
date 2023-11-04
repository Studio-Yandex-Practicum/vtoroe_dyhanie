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
from django.contrib import admin


class BaseModelAdminKeys(admin.ModelAdmin):
    list_display = ('keyboard_name', 'keyboard_text')
    empty_value_display = '-пусто-'
    # readonly_fields = ('keyboard_name',)

    class Meta:
        abstract = True


class BaseModelAdminConstant(admin.ModelAdmin):
    list_display = ('constant_name', 'constant_text')
    empty_value_display = '-пусто-'
    # readonly_fields = ('constant_name',)

    class Meta:
        abstract = True


myModelsKeys = [
    AboutFundKeyboard,
    BasicInfoKeyboard,
    Keyboard,
    OnboardingKeyboard,
    RulesKeyboard,
]
myModelsConstant = [
    AboutFundText,
    BasicInfoText,
    Button,
    ContactListtext,
    FaqText,
    Links,
    OnboardingText,
    QueryPatterns,
    RegFormsText,
    RulesText,
    State,
    Text,
]

admin.site.register(myModelsKeys, BaseModelAdminKeys)
admin.site.register(myModelsConstant, BaseModelAdminConstant)
