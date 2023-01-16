# Little Professor
# Harvard / cs50p / python
# problem set week 4  https://cs50.harvard.edu/python/2022/psets/4/
# Vitaly Vetrof / vetrof@gmail.com  / vetrof.com

# --------------------
# raise ValueError

from random import randint


def main():

    level = get_level()  # get num for digits
    score = 0            # set user score

    for i in range(10):  # create loop for 10 rounds game

        x, y = generate_integer(level)  # get random dogots fo x and y

        for i in range(3):  # set 3 loop for try 3 time for answer
            user_answer = get_answer(x, y)  # get snwer and validate wit func

            if user_answer == x + y:  # if user right score ++
                score += 1
                break
            else:
                print('EEE')
                continue

    print('score:', score)


def get_level():
    while True:
        try:
            level = int(input('Level: '))
        except ValueError:
            pass
        else:
            if 1 <= level <= 3:
                return level


def generate_integer(digit):

    if digit == 1:
        x = randint(1, 9)
        y = randint(1, 9)
    elif digit == 2:
        x = randint(10, 99)
        y = randint(10, 99)
    elif digit == 3:
        x = randint(100, 999)
        y = randint(100, 999)
    return x, y


def get_answer(x, y):
    while True:
        try:
            n = int(input(f'{x} + {y} = '))
        except ValueError:
            pass
        else:
            return n


if __name__ == '__main__':
    main()
