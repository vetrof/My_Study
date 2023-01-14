# Упражнение по программированию 6.6

# Среднее арифметическое чисел

def main():
    # Объявить переменные
    total = 0.0
    number = 0.0
    counter = 0
    
    # Открыть файл numbers.txt для чтения
	# Файл находится в подпапке data
    infile = open(r'data\numbers.txt', 'r')

    for line in infile:
        counter = counter + 1
        number = float(line)
        total += number
        
    # Закрыть файл
    infile.close()

    # Вычислить среднее арифметическое
    average = total / counter
    
    # Показать среднее арифметическое чисел в файле
    print('Среднее арифметическое: ', average)

# Вызвать главную функцию.
main()