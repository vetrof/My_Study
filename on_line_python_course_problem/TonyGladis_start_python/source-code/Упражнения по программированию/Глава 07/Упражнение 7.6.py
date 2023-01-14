# Упражнение по программированию 7.6

# Больше числа n

def main():
    # Объявить локальные переменные
    number = 5
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Показать число.
    print('Число:', number)

    # Показать список чисел.
    print('Список чисел:\n', number_list, sep='')
    
    # Показать список чисел, которые больше этого числа.
    print('Список чисел, которые больше числа ', \
          number, ':', sep='')
    
    # Вызвать функцию display_larger_than_n_list, передав
    # число и список чисел в качестве аргументов.
    display_larger_than_n_list(number, number_list)

# Функция display_larger_than_n_list принимает два аргумента:
# список и число. Эта функция показывает все числа в списке,
# которые больше указанного числа.
def display_larger_than_n_list(n, n_list):
    # Объявить пустой список.
    larger_than_n_list = []

    # Перебрать значения в списке.
    for value in n_list:
        
        # Определить, является ли значение больше n.
        if value > n:
            
            # Если да, то добавить это значение в список.
            larger_than_n_list.append(value)

    # Display the list.
    print(larger_than_n_list)
        
# Вызвать главную функцию.
main()