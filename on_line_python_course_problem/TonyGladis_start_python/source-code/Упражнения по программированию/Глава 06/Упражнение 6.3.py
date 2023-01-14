# Упражнение по программированию 6.3

# Номера строк

def main():
    # Объявить переменные
    line = ''
    counter = 0
    
    # Предложить ввести имя файла
    fileName = input('Введите имя файла: ')

    # Открыть указанный файл для чтения
	# Файл находится в подпапке data
    infile = open("data\\" + fileName, 'r')

    for line in infile:
        counter += 1
        print(counter, end='')
        print(':', end=' ')
        
        # Отсечь символ '\n' с конца строки
        line = line.rstrip('\n')
        print(line)

    # Закрыть файл
    infile.close()

# Вызвать главную функцию.
main()