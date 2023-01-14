# Упражнение по программированию 6.2

# Вывод на экран верхней части файла

def main():
    # Объявить переменные
    line = ''
    counter = 0
    
    # Предложить ввести имя файла
    fileName = input('Введите имя файла: ')

    # Открыть указанный файл для чтения
	# Файл находится в подпапке data
    infile = open("data\\" + fileName, 'r')

    # Первичное чтение
    line = infile.readline()
    counter = 1
    
    # Прочитать и показать первые пять строк
    while line != '' and counter <= 5:
        # Отсечь символ '\n'
        line = line.rstrip('\n')
        print(line)
        line = infile.readline()
        # Обновить счетчик после прочтения строки
        counter +=1  

    # Закрыть файл
    infile.close()

# Вызвать главную функцию.
main()