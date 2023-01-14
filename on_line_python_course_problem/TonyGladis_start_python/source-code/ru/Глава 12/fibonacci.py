# Эта программа применяет рекурсию для печати чисел
# последовательности Фибоначчи.

def main():
    print('Первые 10 чисел')
    print('последовательности Фибоначчи:')

    for number in range(1, 11):
        print(fib(number))

# Функция fib возвращает n-ое число
# последовательности Фибоначчи.
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# Вызвать главную функцию.
if __name__ == '__main__':
    main()