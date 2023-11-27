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
    RegFormsText,
    RulesKeyboard,
    RulesText,
    Text,
)
from django import forms
from django.contrib import admin


class TextAdminForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = "__all__"
        widgets = {
            'constant_text': forms.Textarea(attrs={'rows': 10, 'cols': 80}),
        }


class TextAdmin(admin.ModelAdmin):
    list_display = ('constant_name', 'constant_text')
    empty_value_display = '-пусто-'
    form = TextAdminForm


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
    RegFormsText,
    RulesText,
    Text,
]

admin.site.register(myModelsKeys, TextAdmin)
admin.site.register(myModelsConstant, TextAdmin)
