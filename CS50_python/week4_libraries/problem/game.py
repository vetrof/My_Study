# Guessing Game
from random import randint
from sys import exit

def main():

    level = get_level()
    random_num = random_n(level)
    game(random_num)


def get_level():
    pass


def random_n(l):
    pass


def ask_number():
    pass


def game(num):

    while True:
        user_ask = ask_number()
        if user_ask < num:
            print('Too small!')
        elif user_ask > num:
            print('Too large!')
        else:
            print('Just right!')
            sys.exit


# if __name__ == "__main__":
    # main()
