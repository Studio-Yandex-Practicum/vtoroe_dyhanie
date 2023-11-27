from django.db import models


class BasicModel(models.Model):
    constant_description = models.CharField(
        null=True,
        max_length=1600,
        verbose_name='Описание')
    constant_text = models.CharField(
        max_length=1600,
        verbose_name='Текст внутри кнопки')
    constant_name = models.CharField(unique=False, max_length=100)

    class Meta:
        abstract = True


class AboutFundKeyboard(BasicModel):
    class Meta:
        db_table = 'about_fund_keyboards'
        verbose_name_plural = ('Модуль с реализацией '
                               'клавиатур для блока "О Фонде"')


class BasicInfoKeyboard(BasicModel):
    class Meta:
        db_table = 'basic_info_keyboards'
        verbose_name_plural = ('Базовые информационные кнопки')


class Keyboard(BasicModel):
    class Meta:
        db_table = 'keyboards'
        verbose_name_plural = ('Гл.Меню и FAQ кнопки')


class OnboardingKeyboard(BasicModel):
    class Meta:
        db_table = 'onboarding_keyboards'
        verbose_name_plural = ('Онбординг кнопки')


class RulesKeyboard(BasicModel):
    class Meta:
        db_table = 'rules_keyboards'
        verbose_name_plural = ('Клавиатура для подраздела "Общие правила"')


class AboutFundText(BasicModel):
    class Meta:
        db_table = 'about_fund_text'
        verbose_name_plural = ('Тексты для подраздела "О Фонде"')

class BasicInfoText(BasicModel):
    class Meta:
        db_table = 'basic_info_text'
        verbose_name_plural = ('Тексты для подраздела "Основная иннформация"')


class Button(BasicModel):
    class Meta:
        db_table = 'button'
        verbose_name_plural = ('Названия кнопок меню')


class ContactListtext(BasicModel):
    class Meta:
        db_table = 'contact_list_text'
        verbose_name_plural = ('Тексты для подраздела "Список контактов"')


class FaqText(BasicModel):
    class Meta:
        db_table = 'faq_text'
        verbose_name_plural = ('Тексты для подраздела "FAQ"')


class Links(BasicModel):
    class Meta:
        db_table = 'links'
        verbose_name_plural = ('links')
        verbose_name_plural = ('Ссылки для подраздела "Обратнаня связь" и "База знаний"')


class OnboardingText(BasicModel):
    class Meta:
        db_table = 'onboarding_text'
        verbose_name_plural = ('Тексты для подраздела "Онбоардинг"')


class RegFormsText(BasicModel):
    class Meta:
        db_table = 'reg_forms_text'
        verbose_name_plural = ('Тексты для подраздела "Регламенннты и формы"')


class RulesText(BasicModel):
    class Meta:
        db_table = 'rules_text'
        verbose_name_plural = ('Тексты для подраздела "Общие правила"')


class Text(BasicModel):
    class Meta:
        db_table = 'text'
        verbose_name_plural = ('Базовые сообщения бота')
