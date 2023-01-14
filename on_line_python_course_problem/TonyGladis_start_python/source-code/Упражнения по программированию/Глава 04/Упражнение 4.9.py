# Упражнение по программированию 4.9

# Уровень океана

# Константа для подъема уровня в год.
RISE_PER_YEAR = 1.6

# Объявить переменную для хранения величины подъема.
rise = 0.0

# Вычислить и напечатать величину подъема в каждом году.
print ('Год\t\t Подъем (в миллиметрах)')
print ('---------------------------------------')

for year in range(25):
    rise += RISE_PER_YEAR
    print ((year + 1), '\t\t', format(rise, '.2f'))