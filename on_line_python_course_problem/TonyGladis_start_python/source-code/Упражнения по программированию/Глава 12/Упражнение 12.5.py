# Упражнение по программированию 12.5

# Рекурсивная сумма списка

def main():
    # Инициализировать список значений от 1 до 10.
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Показать список.
    print('Список чисел:\n', number_list, sep='')

    # Вызвать функцию sum_list и показать сумму всех
    # чисел в списке.
    print('Сумма всех чисел в списке:', \
          sum_list(number_list))

# Функция sum_list принимает список чисел в качестве аргументов.
# Эта функция рекурсивно вычисляет сумму всех чисел в списке и
# возвращает значение.
def sum_list(numlist):
    n  = len(numlist)
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[n-1] + sum_list(numlist[0:n-1])

# Вызвать главную функцию.
main()