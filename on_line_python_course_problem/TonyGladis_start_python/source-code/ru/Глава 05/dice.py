# Эта программа "бросает" кубики.
import random

# Константы для минимального и максимального случайных чисел
MIN = 1
MAX = 6

def main():
    # Создать переменную, которая управляет циклом.
    again = 'д'

    # Имитировать бросание кубиков.
    while again == 'д' or again == 'Д':
        print('Бросаем кубики...')
        print('Значения граней:')
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))

        # Сделать еще один бросок кубиков?
        again = input('Бросить кубики еще раз? (д = да): ')

# Вызвать функцию main.
main()