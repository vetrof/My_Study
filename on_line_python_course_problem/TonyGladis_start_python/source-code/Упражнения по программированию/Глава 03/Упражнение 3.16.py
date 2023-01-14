# Упражнение по программированию 3.16

# Дни в феврале

# Эта программа определяет количество дней в
# феврале для того или иного года.

print('Введите год: ', end='')
year = int(input())
if year % 100 == 0:
    if year % 400 == 0:
        leap_year = True
    else:
        leap_year = False
else:
    if year % 4 == 0:
        leap_year = True
    else:
        leap_year = False
if leap_year:
    print('Это високосный год. В феврале 29 дней.')
else:
    print('Это не високосный год. В феврале 28 дней.')