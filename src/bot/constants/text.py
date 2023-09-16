from links import (
    CNTRCT_LINK, BILLS_LINK, ACC_PERSONS_LINK, REG_VACATION_LINK,
    TEMP_VACATION_LINK, REG_BUSINESS_TRIP_LINK, TEMP_BUSINESS_TRIP_LINK,
    REG_OFFER_LINK, TEMP_OFFER_LINK, REG_OTHR_OFFER_LINK, TEMP_OTHR_OFFER_LINK,
    REG_FIRING_LINK, TEMP_FIRING_LINK, REG_WEEKEND_LINK, REG_SALARY_LINK
)

STOP_MESSAGE = 'Работа приложения остановлена.'
HELP_MESSAGE = 'Написать в поддержку'
START_MESSAGE = (
    'Привет! Меня зовут Втордыш,'
    'и я помощник сотрудников фонда ВТОРОЕ ДЫХАНИЕ. '
    'Я создан для того, чтобы помочь новеньким адаптироваться, '
    'но также буду полезен и опытным сотрудникам.\n'
    'Чтобы продолжить, введи секретное слово.'
)

REG_FORM_MESSAGE = f'''
Здесь собраны основные регламенты оформления договоров и документов,
а также шаблоны кадровых заявлений\.

*Финансы*

1\. [Регламент подготовки, согласования и подписания договоров]({CNTRCT_LINK})
2\. [Регламент согласования счетов]({BILLS_LINK})
3\. [Положение по подотчетным лицам]({ACC_PERSONS_LINK})

*HR*

1\. [Регламент по отпускам]({REG_VACATION_LINK})
2\. [Шаблоны заявлений по отпускам]({TEMP_VACATION_LINK})
3\. [Регламент по командировкам]({REG_BUSINESS_TRIP_LINK})
4\. [Шаблоны заявлений по командировкам]({TEMP_BUSINESS_TRIP_LINK})
5\. [Регламент по приему на работу]({REG_OFFER_LINK})
6\. [Шаблоны заявлений по приему на работу]({TEMP_OFFER_LINK})
7\. [Регламент по переводу на другую работу]({REG_OTHR_OFFER_LINK})
8\. [Шаблоны заявлений по переводу на другую должность]({TEMP_OTHR_OFFER_LINK})
9\. [Регламент по увольнению]({REG_FIRING_LINK})
10\. [Шаблоны заявлений по увольнению]({TEMP_FIRING_LINK})
11\. [Регламент оформления работы в выходной]({REG_WEEKEND_LINK})
12\. [Регламент по изменению оклада/должности]({REG_SALARY_LINK})
'''
