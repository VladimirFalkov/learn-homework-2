 
from datetime import datetime, date, timedelta
"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

def print_days():
    today_date = date.today()
    delta = timedelta(days=1)
    yeasterday_date = today_date - delta
    date_30_days_ago = today_date - 30*delta
    today_date.strftime("%d.%m.%Y")
    print(f'Сегодняшняя дата: {yeasterday_date.strftime("%d.%m.%Y")}')
    print(f'Сегодняшняя дата: {today_date.strftime("%d.%m.%Y")}')
    print(f'Дата 30 дней назад была: {date_30_days_ago.strftime("%d.%m.%Y")}')

def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    pass

if __name__ == "__main__":
    print_days()
    #print(str_2_datetime("01/01/20 12:10:03.234567"))
