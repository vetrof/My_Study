# Упражнение по программированию 6.5

# Сумма чисел 

def main():
    # Объявить переменные
    line = ''
    total = 0.0
    number = 0.0

    # Открыть файл numbers.txt для чтения
	# Файл находится в подпапке data
    infile = open(r'data\numbers.txt', 'r')

    for line in infile:
        number = float(line)
        total += number
        
    # Закрыть файл
    infile.close()

    # Показать сумму чисел в файле
    print('Всего: ', total)

# Вызвать главную функцию.
main()