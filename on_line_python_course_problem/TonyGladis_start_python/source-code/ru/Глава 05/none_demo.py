# Эта программа ключевое слово None.

def main():
    # Получить от пользователя два числа.
    num1 = int(input('Введите число: '))
    num2 = int(input('Введите еще одно число: '))

    # Вызвать функцию деления divide.
    quotient = divide(num1, num2)

    # Вывести результат на экран.
    if quotient is None:
        print('Деление на ноль невозможно.')
    else:
        print(f'{num1} поделить на {num2} равняется {quotient}.')

# Функция divide делит num1 на num2 и возвращает
# результат. Если num2 равно 0, то указанная функция
# возвращает None.
def divide(num1, num2):
    if num2 == 0:
        result = None
    else:
        result = num1 / num2
    return result

# Исполнить главную программу.
main()