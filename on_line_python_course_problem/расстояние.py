# > python program.py 15
# > Расстояние: 15 км


import sys

# Не меняйте строки ниже.
distance = sys.argv[1]
distance_str = "Расстояние: N км"

# Исправьте код так, чтобы символ N в строке distance_str  был заменен на значение
# из переменной distance.
distance_str = distance_str[:11] + ' ' + distance + ' ' + distance_str[-2:]

# Вывод distance_str.
print(distance_str)