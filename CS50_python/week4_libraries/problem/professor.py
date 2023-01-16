# Little Professor
# Harvard / cs50p / python
# problem set week 4  https://cs50.harvard.edu/python/2022/psets/4/
# Vitaly Vetrof / vetrof@gmail.com  / vetrof.com

from random import randint


def main():

    level = get_level()  # get num for digits
    score = 0            # set user score
    user_answer = 0

    for _ in range(10):  # create loop for 10 rounds game

        x, y = generate_integer(level)  # get random digits fo x and y

        for _ in range(3):  # set 3 loop for try 3 time for one answer

            try:
                user_answer = int(input(f'{x} + {y} = '))

            except ValueError:
                pass

            else:
                if user_answer == x + y:  # if user right score ++
                    score += 1
                    break
                else:
                    pass

            print('EEE')
            continue

        if user_answer != (x + y):
            print(f"{x} + {y} = {x + y}")

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

    n1 = 0
    n2 = 0

    if digit == 1:
        n1 = randint(0, 9)
        n2 = randint(0, 9)
    elif digit == 2:
        n1 = randint(10, 99)
        n2 = randint(10, 99)
    elif digit == 3:
        n1 = randint(100, 999)
        n2 = randint(100, 999)
    return n1, n2


if __name__ == '__main__':
    main()
