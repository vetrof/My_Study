# Упражнение по программированию 6.1

# Вывод файла на экран

def main():
    # Объявить локальные переменные
    contents = ''
    
    # Открыть файл numbers.txt для чтения
	# Файл находится в подпапке data
    infile = open(r'data\numbers.txt', 'r')

    # Прочитать данные и сохранить его содержимое в contents
    contents = infile.read()

    # Закрыть файл
    infile.close()

    # Напечатать содержимое
    print(contents)

# Вызвать главную функцию.
main()