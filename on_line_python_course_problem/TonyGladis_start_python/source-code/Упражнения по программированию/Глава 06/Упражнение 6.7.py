# Упражнение по программированию 6.7

# Программа записи файла со случайными числами

import random

def main():
    # Локальные переменные
    filename = ''
    numberOfRandoms = 0
    randomNumber = 0

    # Получить имя файла в качестве входного значения от пользователя.
    filename = input('Введите имя файла, в который ' \
                     'должны быть записаны результаты: ')

    # Получить количество значений, которые будут записаны в файл.
    numberOfRandoms = int(input('Введите количество ' \
                                'случайных чисел, которые ' \
                                'будут записаны в файл: '))

    # Открыть файл для вывода данных.
    # Файл будет находиться в подпапке data
    outputFile = open('data\\' + filename, 'w')

    # Записать указанное количество случайных чисел в файл.
    for counter in range (numberOfRandoms):

        randomNumber = random.randint(1, 500)
        outputFile.write(str(randomNumber) + '\n')

    # Закрыть файл.
    outputFile.close()
	
    print('Готово.')
	
# Вызвать главную функцию.
main()