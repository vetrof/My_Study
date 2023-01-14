# Упражнение по программированию 12.4

# Максимальное значение в списке

def main():
    # Инициализировать список значений от 1 до 10.
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Показать список.
    print('Список чисел:\n', number_list, sep='')

    # Вызвать функцию find_largest и показать
    # максимальное число в спике.
    print('Максимальное число в списке: ', find_largest(number_list))

# Функция find_largest принимает список в качестве аргумента и
# возвращает максимальное значение в списке.
# Для нахождения максимального значения эта функция использует рекурсию.
def find_largest(numlist):
    n  = len(numlist)
    if n == 1:
        return numlist[0]
    else:
        temp = find_largest(numlist[0:n-1])
        if numlist[n-1] > temp:
            return numlist[n-1]
        else:
            return temp

# Вызвать главную функцию.
main()