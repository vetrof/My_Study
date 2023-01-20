
# Working 9 to 5
# am/pm converter time range to 24 hour format
# '9 AM to 5 PM'  >>>> '09:00 to 17:00'
# Harvard / cs50p / python
# problem set week 7  https://cs50.harvard.edu/python/2022/psets/7
# Vitaly Vetrof / vetrof@gmail.com  / vetrof.com

import re
import sys
# start_time = []
# start_hour = 0
# start_min = 0
# start_ampm = 0
#
# finish_time = []
# finish_hour = 0
# finish_min = 0
# finish_ampm = 0


def main():
    print(convert(input("Hours: ")))
    # time = convert('10:30 PM to 8:50 AM')
    # time = convert('10 PM to 8:50 AM')
    # time = convert('9 AM to 5 PM')
    # time = convert('9:00 AM to 5:00 PM')
    # time = convert('10 PM to 8 AM')

    # time = convert('9:60 AM to 5:60 PM')
    # time = convert('9 AM - 5 PM')
    # time = convert('09:00 AM - 17:00 PM')


def convert(s):

    # обьявим переменные
    start_min = 0
    finish_min = 0
    out_start_min = 0
    out_end_min = 0

    try:
        # если есть совпадение с шаблоном то разделяем ввод на 4ре группы
        if match := re.search(r'(.+)(AM|PM) to (.+)(AM|PM)', s):
            # print(match.group())
            # print(match.group(1).strip().split(':'))
            # print(match.group(2))
            # print(match.group(3).strip().split(':'))
            # print(match.group(4))
            # содержимое групп распределяем по переменным
            # группы 1 и 3 сохраняются списком с ч:м
            start_time = match.group(1).strip().split(':')
            start_ampm = match.group(2)
            finish_time = match.group(3).strip().split(':')
            finish_ampm = match.group(4)

            # получаем из списка начальный и конечный час
            start_hour = int(start_time[0])
            finish_hour = int(finish_time[0])

            # получаем минуты если есть
            # если время указано с минутами то присваиваем значения старта
            if len(start_time) == 2:
                start_min = int(start_time[1])  #интуем значение минут
                out_start_min = start_min       #переносим значение
                if start_min > 59:  # если минут больше 59 - то ValueError
                    raise ValueError

            # тоже самое минутами конца периода
            # если время указано с минутами то присваиваем значения финиша
            if len(finish_time) == 2:
                finish_min = int(finish_time[1])
                out_end_min = finish_min
                if finish_min > 59:  # если минут больше 59 - то ValueError
                    raise ValueError

        # если шаблон не совпал - то вызываем ошибку
        else:
            raise ValueError

    except ValueError:
        print('error -1')
        sys.exit(1)
    # print('start_time', start_time)
    # print('start_hour', start_hour)
    # print('start_min', start_min)
    # print('start_ampm', start_ampm)
    # print()
    # print('finish_time', finish_time)
    # print('finish_hour', finish_hour)
    # print('finish_min', finish_min)
    # print('finish_ampm', finish_ampm)

    # out_start_min = start_min
    # out_end_min = finish_min

    # print()
    # print('out_start_hour', out_start_hour)
    # print('out_start_min', out_start_min)
    # print()
    # print('out_end_hour', out_end_hour)
    # print('out_end_min', out_end_min)
    # print()


    # если указано PM то прибавляем 12
    if start_ampm == 'PM':
        out_start_hour = start_hour + 12
    else:
        out_start_hour = start_hour

    if finish_ampm == 'PM':
        out_end_hour = finish_hour + 12
    else:
        out_end_hour = finish_hour

    # если минуты не заданы - то присваеваем строку 00
    if out_start_min == 0:
        out_start_min = '00'

    if out_end_min == 0:
        out_end_min = '00'

    # форматируем строку
    return f'{out_start_hour}:{out_start_min} to {out_end_hour}:{out_end_min}'


if __name__ == "__main__":
    main()

