# Упражнение по программированию 6.8

# Программа чтения файлов со случайными числами

def main():
    # Локальные переменные
    counter = 0
    total = 0
    number = 0    

    # Открыть входной файл
	# Файл находится в подпапке data
    inputFile = open(r'data\random_numbers.txt', 'r')

    # Прочитать числа из файла, ведя учет их количества 
    # и промежуточной суммы нарастающим итогом
    for line in inputFile:
        number = int(line)
        total += number
        counter += 1

    # Закрыть файл
    inputFile.close()

    print('Итого:', format(total, ','))
    print('из файла было прочитано', counter, 'чисел.')

# Вызвать главную функцию.
main()