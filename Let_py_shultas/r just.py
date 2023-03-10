# ВЫРАВНИВАНИЕ ПО ПРАВОМУ КРАЮ, ЧАСТЬ 2
# Напишите программу, которая получает через аргументы командной строки три числа
# , а после выводит каждое число с правой стороны строки длиной 15 знаков.
# Слева от чисел должны быть проставлены точки.
#
# Пример использования:
# > python rjust.py 12 543 123
# > .............12
# > ............543
# > ............123
# Подсказка:
# Используйте метод rjust.

import sys

n1 = sys.argv[1].rjust(15, '.')
n2 = sys.argv[2].rjust(15, '.')
n3 = sys.argv[3].rjust(15, '.')

print(n1)
print(n2)
print(n3)
