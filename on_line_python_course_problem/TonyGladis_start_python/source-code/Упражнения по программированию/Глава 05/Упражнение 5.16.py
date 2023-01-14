# Упражнение по программированию 5.16

# Счетчик четных/нечетных чисел

import random

# Главная функция
def main():
    # Локальные переменные
    currentNumber = 0
    oddCounter = 0
    evenCounter = 0
    totalNumbers = 100

    for counter in range(totalNumbers):

        # Получить случайное число
        currentNumber = random.randint(1, 1000)

        # Проверить число на четность/нечетность
        if isEven(currentNumber):
            evenCounter+=1
        else:
            oddCounter+=1

    print ('Из', totalNumbers, 'случайных чисел,', oddCounter,\
           'были нечетными и', evenCounter, 'были четными.')

# Функция isEven возвращает True, если число четное, и
# False, если нечетное. 
def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Вызвать главную функцию.
main()