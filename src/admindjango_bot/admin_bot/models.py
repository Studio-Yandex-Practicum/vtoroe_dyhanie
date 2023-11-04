from django.db import models


class BasicModelKeyboard(models.Model):
    keyboard_text = models.CharField(
        max_length=100,
        verbose_name='Текст внутри кнопки')
    keyboard_name = models.CharField(unique=False, max_length=100)

    class Meta:
        abstract = True


class AboutFundKeyboard(BasicModelKeyboard):
    class Meta:
        db_table = 'about_fund_keyboards'
        verbose_name_plural = ('Модуль с реализацией '
                               'клавиатур для блока "О Фонде"')


class BasicInfoKeyboard(BasicModelKeyboard):
    class Meta:
        db_table = 'basic_info_keyboards'
        verbose_name_plural = ('Базовые информационные кнопки')


class Keyboard(BasicModelKeyboard):
    class Meta:
        db_table = 'keyboards'
        verbose_name_plural = ('Гл.Меню и FAQ кнопки')


class OnboardingKeyboard(BasicModelKeyboard):
    class Meta:
        db_table = 'onboarding_keyboards'


class RulesKeyboard(BasicModelKeyboard):
    class Meta:
        db_table = 'rules_keyboards'


class BasicModelConstant(models.Model):
    constant_name = models.CharField(unique=False, max_length=100)
    constant_text = models.TextField()

    class Meta:
        abstract = True


class AboutFundText(BasicModelConstant):
    class Meta:
        db_table = 'about_fund_text'


class BasicInfoText(BasicModelConstant):
    class Meta:
        db_table = 'basic_info_text'


class Button(BasicModelConstant):
    class Meta:
        db_table = 'button'


class ContactListtext(BasicModelConstant):
    class Meta:
        db_table = 'contact_list_text'


class FaqText(BasicModelConstant):
    class Meta:
        db_table = 'faq_text'


class Links(BasicModelConstant):
    class Meta:
        db_table = 'links'


class OnboardingText(BasicModelConstant):
    class Meta:
        db_table = 'onboarding_text'


class QueryPatterns(BasicModelConstant):
    class Meta:
        db_table = 'query_patterns'


class RegFormsText(BasicModelConstant):
    class Meta:
        db_table = 'reg_forms_text'


class RulesText(BasicModelConstant):
    class Meta:
        db_table = 'rules_text'


class State(BasicModelConstant):
    class Meta:
        db_table = 'state'


class Text(BasicModelConstant):
    class Meta:
        db_table = 'text'
