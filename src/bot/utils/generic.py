from datetime import datetime


def check_date_format(date_string):
    '''Проверка корректности введенной даты.'''
    try:
        datetime.strptime(date_string, '%d.%m.%Y')
        return True
    except ValueError:
        return False
