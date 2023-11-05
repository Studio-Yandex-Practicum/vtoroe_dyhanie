# Generated by Django 4.2.7 on 2023-11-05 14:24

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='AboutFundKeyboard',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'keyboard_text',
                    models.CharField(
                        max_length=100, verbose_name='Текст внутри кнопки'
                    ),
                ),
                ('keyboard_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Модуль с реализацией клавиатур для блока "О Фонде"',
                'db_table': 'about_fund_keyboards',
            },
        ),
        migrations.CreateModel(
            name='AboutFundText',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('constant_name', models.CharField(max_length=100)),
                ('constant_text', models.TextField()),
            ],
            options={
                'db_table': 'about_fund_text',
            },
        ),
        migrations.CreateModel(
            name='BasicInfoKeyboard',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'keyboard_text',
                    models.CharField(
                        max_length=100, verbose_name='Текст внутри кнопки'
                    ),
                ),
                ('keyboard_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Базовые информационные кнопки',
                'db_table': 'basic_info_keyboards',
            },
        ),
        migrations.CreateModel(
            name='BasicInfoText',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('constant_name', models.CharField(max_length=100)),
                ('constant_text', models.TextField()),
            ],
            options={
                'db_table': 'basic_info_text',
            },
        ),
        migrations.CreateModel(
            name='Button',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('constant_name', models.CharField(max_length=100)),
                ('constant_text', models.TextField()),
            ],
            options={
                'db_table': 'button',
            },
        ),
        migrations.CreateModel(
            name='ContactListtext',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('constant_name', models.CharField(max_length=100)),
                ('constant_text', models.TextField()),
            ],
            options={
                'db_table': 'contact_list_text',
            },
        ),
        migrations.CreateModel(
            name='FaqText',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('constant_name', models.CharField(max_length=100)),
                ('constant_text', models.TextField()),
            ],
            options={
                'db_table': 'faq_text',
            },
        ),
        migrations.CreateModel(
            name='Keyboard',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'keyboard_text',
                    models.CharField(
                        max_length=100, verbose_name='Текст внутри кнопки'
                    ),
                ),
                ('keyboard_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Гл.Меню и FAQ кнопки',
                'db_table': 'keyboards',
            },
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('constant_name', models.CharField(max_length=100)),
                ('constant_text', models.TextField()),
            ],
            options={
                'db_table': 'links',
            },
        ),
        migrations.CreateModel(
            name='OnboardingKeyboard',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'keyboard_text',
                    models.CharField(
                        max_length=100, verbose_name='Текст внутри кнопки'
                    ),
                ),
                ('keyboard_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'onboarding_keyboards',
            },
        ),
        migrations.CreateModel(
            name='OnboardingText',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('constant_name', models.CharField(max_length=100)),
                ('constant_text', models.TextField()),
            ],
            options={
                'db_table': 'onboarding_text',
            },
        ),
        migrations.CreateModel(
            name='QueryPatterns',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('constant_name', models.CharField(max_length=100)),
                ('constant_text', models.TextField()),
            ],
            options={
                'db_table': 'query_patterns',
            },
        ),
        migrations.CreateModel(
            name='RegFormsText',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('constant_name', models.CharField(max_length=100)),
                ('constant_text', models.TextField()),
            ],
            options={
                'db_table': 'reg_forms_text',
            },
        ),
        migrations.CreateModel(
            name='RulesKeyboard',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'keyboard_text',
                    models.CharField(
                        max_length=100, verbose_name='Текст внутри кнопки'
                    ),
                ),
                ('keyboard_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'rules_keyboards',
            },
        ),
        migrations.CreateModel(
            name='RulesText',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('constant_name', models.CharField(max_length=100)),
                ('constant_text', models.TextField()),
            ],
            options={
                'db_table': 'rules_text',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('constant_name', models.CharField(max_length=100)),
                ('constant_text', models.TextField()),
            ],
            options={
                'db_table': 'state',
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('constant_name', models.CharField(max_length=100)),
                ('constant_text', models.TextField()),
            ],
            options={
                'db_table': 'text',
            },
        ),
    ]
