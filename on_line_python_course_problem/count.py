# КОЛИЧЕСТВО ПОВТОРЕНИЙ
# Напишите программу, которая получает из первого аргумента командной строки слово,
# а из второго букву и выводит сколько раз эта буква встречается в переданном слове.
#
# Пример использования:
# > python count.py programming r
# > 2
# Подсказка:
# Используйте метод count.

import sys

w1 = sys.argv[1]
w2 = sys.argv[2]

x = w1.count(w2)

print(x)
