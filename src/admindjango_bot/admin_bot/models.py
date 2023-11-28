from django.db import models


class BasicModel(models.Model):
    constant_description = models.CharField(
        null=True, max_length=1600, verbose_name='Описание'
    )
    constant_text = models.CharField(
        max_length=1600, verbose_name='Текст внутри кнопки'
    )
    constant_name = models.CharField(unique=False, max_length=100)

    class Meta:
        abstract = True


class Keyboard(BasicModel):
    class Meta:
        db_table = 'keyboards'
        verbose_name_plural = 'Клавиатуры основного меню и раздела "FAQ"'


class AboutFundKeyboard(BasicModel):
    class Meta:
        db_table = 'about_fund_keyboards'
        verbose_name_plural = 'Клавиатуры раздела "О Фонде"'


class OnboardingKeyboard(BasicModel):
    class Meta:
        db_table = 'onboarding_keyboards'
        verbose_name_plural = 'Клавиатуры раздела "Онбординг"'


class BasicInfoKeyboard(BasicModel):
    class Meta:
        db_table = 'basic_info_keyboards'
        verbose_name_plural = 'Клавиатуры раздела "Основная информация"'


class RulesKeyboard(BasicModel):
    class Meta:
        db_table = 'rules_keyboards'
        verbose_name_plural = 'Клавиатуры раздела "Общие правила"'


class ContactListKeyboard(BasicModel):
    class Meta:
        db_table = 'contact_list_keyboards'
        verbose_name_plural = 'Клавиатуры раздела "Список контактов"'


class AboutFundText(BasicModel):
    class Meta:
        db_table = 'about_fund_text'
        verbose_name_plural = 'Тексты раздела "О Фонде"'


class OnboardingText(BasicModel):
    class Meta:
        db_table = 'onboarding_text'
        verbose_name_plural = 'Тексты раздела "Онбоардинг"'


class BasicInfoText(BasicModel):
    class Meta:
        db_table = 'basic_info_text'
        verbose_name_plural = 'Тексты раздела "Основная информация"'


class RulesText(BasicModel):
    class Meta:
        db_table = 'rules_text'
        verbose_name_plural = 'Тексты раздела "Общие правила"'


class RegFormsText(BasicModel):
    class Meta:
        db_table = 'reg_forms_text'
        verbose_name_plural = 'Тексты раздела "Регламенты и формы"'


class FaqText(BasicModel):
    class Meta:
        db_table = 'faq_text'
        verbose_name_plural = 'Тексты раздела "FAQ"'


class ContactListText(BasicModel):
    class Meta:
        db_table = 'contact_list_text'
        verbose_name_plural = 'Тексты раздела "Список контактов"'


class Button(BasicModel):
    class Meta:
        db_table = 'button'
        verbose_name_plural = 'Названия кнопок меню'


class Links(BasicModel):
    class Meta:
        db_table = 'links'
        verbose_name_plural = (
            'Ссылки для подраздела "Обратнаня связь" и "База знаний"'
        )


class Text(BasicModel):
    class Meta:
        db_table = 'text'
        verbose_name_plural = 'Базовые сообщения бота'
