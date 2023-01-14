
may_2017 = [24, 26, 15, 10, 15, 19, 10, 1, 4, 7, 7, 7, 12, 14, 17, 8, 9, 19, 21, 22, 11, 15, 19, 23, 15, 21, 16, 13, 25, 17, 19]

# Допишите эту функцию
def comfort_count(temperatures):
    count = 0
    for temp in temperatures:
        if 22 <= temp <= 26:
            count += 1
    # Функция должна вернуть значение переменной count
    return count

# Код ниже не изменяйте:
# вызовем функцию comfort_count(), передадим в неё список may_2017,
# результат работы сохраним в переменную nice_days
nice_days = comfort_count(may_2017)

# Напечатаем значение, сохранённое в nice_days
print('Количество тёплых дней в этом месяце:', nice_days)