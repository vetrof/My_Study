import sys

# Получаем слово из первого аргумента командной строки.
word = sys.argv[1]

# Напишите ваш код тут.

l = len(word)
x = round(l / 2)

print(word[x - 1])