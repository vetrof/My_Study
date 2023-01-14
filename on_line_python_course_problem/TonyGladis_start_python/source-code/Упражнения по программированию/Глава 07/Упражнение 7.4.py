# Упражнение по программированию 7.4

# Программа анализа чисел

def main():
    # Список для хранения чисел
    number_list = []

    # Переменные
    low = 0.0
    high = 0.0
    total = 0.0
    average = 0.0
    number = 0

    # Предложить ввести числа 
    for i in range(20):
        number = float(input('Введите число ' + \
                             str(i + 1) + \
                             ' из 20: '))
        number_list.append(number)

    low = min(number_list)
    high = max(number_list)
    total = sum(number_list)
    average = total / 20.0

    print ('Минимальное:', low)
    print ('Максимальное:', high)
    print ('Сумма:', format(total, ',.2f'))
    print ('Среднее:', format(average, ',.2f'))

# Вызвать главную функцию.
main()