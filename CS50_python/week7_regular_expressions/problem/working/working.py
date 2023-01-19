
# Working 9 to 5
# am/pm converter time range to 24 hour format
# '9 AM to 5 PM'  >>>> '09:00 to 17:00'
# Harvard / cs50p / python
# problem set week 7  https://cs50.harvard.edu/python/2022/psets/7
# Vitaly Vetrof / vetrof@gmail.com  / vetrof.com

import re
import sys


def main():
    # print(convert(input("Hours: ")))
    # time = convert('10:30 PM to 8:50 AM')
    time = convert('10:30 PM to 8:50 AM')


def convert(s):
    print(s)
    # '9 AM to 5 PM'  >>>> '09:00 to 17:00'
    # '10:30 PM to 8:50 AM'  >>>> '22:30 to 08:50'

    if match := re.search(r'(.+)(AM|PM) to (.+)(AM|PM)', s):
        print(match.group())
        print(match.group(1).strip().split(':'))
        print(match.group(2))
        print(match.group(3).strip().split(':'))
        print(match.group(4))
        # print(match.group(5))
        # print(match.group(6))


























if __name__ == "__main__":
    main()

