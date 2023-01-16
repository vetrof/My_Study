# Guessing Game
from random import randint
from sys import exit


def main():

    level = get_num('Level: ')
    random_num = random_n(level)
    game(random_num)


def get_num(ask):
    while True:
        try:
            user_input = int(input(ask))
            if user_input > 0:
                return user_input
        except ValueError:
            pass


def random_n(level):
    num = randint(1, level)
    return num


def game(num):

    while True:
        user_number = get_num('Guess: ')
        if user_number < num:
            print('Too small!')
        elif user_number > num:
            print('Too large!')
        else:
            print('Just right!')
            exit()


if __name__ == "__main__":
    main()
