# NUMB3RS
# validate ip4 adress
# Harvard / cs50p / python
# problem set week 7  https://cs50.harvard.edu/python/2022/psets/7
# Vitaly Vetrof / vetrof@gmail.com  / vetrof.com

# import re
# import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    val = ip.split('.')

    if len(val) != 4:
        return False

    for digit in val:
        try:
            digit = int(digit)
        except ValueError:
            return False

        if 0 <= digit <= 255:
            pass
        else:
            return False

    return True


if __name__ == "__main__":
    main()
