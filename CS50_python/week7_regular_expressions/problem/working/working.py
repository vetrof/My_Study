
# Working 9 to 5
# am/pm converter time range to 24 hour format
# '9 AM to 5 PM'  >>>> '09:00 to 17:00'
# Harvard / cs50p / python
# problem set week 7  https://cs50.harvard.edu/python/2022/psets/7
# Vitaly Vetrof / vetrof@gmail.com  / vetrof.com
import re


def main():
    print(convert(input("Hours: ")))
    # print(convert('9 AM to 5:20 PM'))


def convert(s):

    out_start_min = 0
    out_end_min = 0

    # если есть совпадение с шаблоном то разделяем ввод на 4ре группы
    if match := re.search(r'(.+) (AM|PM) to (.+) (AM|PM)', s):
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
        # делим по модулю чтоб получалось что 12 AM == 00:00
        start_hour = int(start_time[0]) % 12
        finish_hour = int(finish_time[0]) % 12

        # получаем минуты если есть
        # если время указано с минутами то присваиваем значения старта
        if len(start_time) == 2:
            start_min = int(start_time[1])  # интуем значение минут
            out_start_min = start_min       # переносим значение
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

    # создадим формат отображения часа в двузначном виде
    # типа '09' а не просто '9'
    if out_start_hour < 10:
        out_start_hour = f'0{out_start_hour}'

    if out_end_hour < 10:
        out_end_hour = f'0{out_end_hour}'

    # форматируем строку
    return f'{out_start_hour}:{out_start_min} to {out_end_hour}:{out_end_min}'


if __name__ == "__main__":
    main()
