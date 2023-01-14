# Упражнение по программированию 5.18

# Список простых чисел

# Главная функция
def main():
    # Локальная переменная
    totalNumbers = 100
    print('число', '\t', 'простое или нет')
    print('------------------------')

    # Для каждого числа напечатать, является ли оно простым или нет
    for number in range(1, totalNumbers + 1):

        # Показать, является ли число простым
        if is_prime(number):
            print (format(number,'3'), '\t', 'простое')
        else:
            print (format(number,'3'), '\t', 'не простое')

# Функция is_prime получает в качестве аргумента число и
# возвращает True, если число простое, и False в противном случае. 
def is_prime(number):
    # Локальные переменные
    half = int(number / 2)
    status = True

    for count in range(2, half + 1):
        if number % count == 0:
            status = False
        
    return status

# Вызвать главную функцию.
main()