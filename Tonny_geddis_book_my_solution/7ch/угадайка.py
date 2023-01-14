#упражнение 5:20
#игра угадайка
import random

def random_number():
    return random.randint(1, 100)

def main():
    print('я загадал число, угадаешь?')
    computer_number = random_number()
    user_number = int(input(': '))

    while user_number != computer_number:
        if user_number > computer_number:
            print('мое число меньше твоего')
        else:
            print('мое число больше твоего')
        user_number = int(input('попробуй еще: '))

    print('молодец')

main()







