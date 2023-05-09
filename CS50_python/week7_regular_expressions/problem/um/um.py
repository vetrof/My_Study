# um
# Harvard / cs50p / python
# problem set week 7  https://cs50.harvard.edu/python/2022/psets/7
# Vitaly Vetrof / vetrof@gmail.com  / vetrof.com

import re


def main():
    # print(count(input("Text: ")))
    print(count('Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?'))


def count(s):
    match_list = re.findall(r'(^um\W)|(um$)|( um\W)', s, flags=re.IGNORECASE)
    print(match_list)
    return len(match_list)


if __name__ == "__main__":
    main()
