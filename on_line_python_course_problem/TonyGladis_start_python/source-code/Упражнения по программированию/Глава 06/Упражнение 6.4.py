# Упражнение по программированию 6.4

# Счетчик значений

def main():
    # Объявить переменные
    line = ''
    counter = 0

    # Открыть файл names.txt для чтения
	# Файл находится в подпапке data
    infile = open(r'data\names.txt', 'r')

    # Первичное чтение
    line = infile.readline()
      
    # Читать пока есть данные
    while line != '':
        counter += 1
        line = infile.readline()

    # Закрыть файл
    infile.close()

    # Показать количество имен в файле
    print('Прочитано', counter, 'имен.')

# Вызвать главную функцию.
main()