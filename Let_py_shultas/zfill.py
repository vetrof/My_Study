
# ЗАПОЛНЯЕМ НУЛЯМИ
# В прошлом задании вы освоили метод rjust, а теперь самое время познакомится с zfill.
# Напишите программу, которая получает через аргументы командной строки три числа, а
# после выводит каждое число с правой стороны строки длиной 15 знаков.
# Слева от чисел должны быть проставлены нули.
#
# Пример использования:
# > python rjust.py 12 543 123
# > 000000000000012
# > 000000000000543
# > 000000000000123

import sys

n1 = sys.argv[1].zfill(15)
n2 = sys.argv[2].zfill(15)
n3 = sys.argv[3].zfill(15)

print(n1)
print(n2)
print(n3)
