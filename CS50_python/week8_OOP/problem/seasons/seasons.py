
# Seasons of Love (date life in minutes)
# Harvard / cs50p / python
# problem set week 8  https://cs50.harvard.edu/python/2022/psets/8
# Vitaly (Vetrof) / vetrof@gmail.com  / vetrof.com

import sys
from datetime import date
import inflect
p = inflect.engine()


def main():

    usr_input = input('Date of Birth: ')
    birth = get_date(usr_input)
    d_minutes = (date.today() - birth).days * 1440
    text = minutes_to_text(d_minutes).replace('and ', '').capitalize()
    print(text, 'minutes')


def get_date(usr):
    try:
        y, m, d = usr.split('-')
        y = int(y)
        m = int(m)
        d = int(d)
    except:
        print('Invalid date')
        sys.exit(1)

    return date(int(y), int(m), int(d))


def minutes_to_text(m):
    w = p.number_to_words(m)
    return w


if __name__ == "__main__":
    main()
