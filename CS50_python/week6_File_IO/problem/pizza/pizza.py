
# Pizza
# Harvard / cs50p / python
# problem set week 6  https://cs50.harvard.edu/python/2022/psets/6/
# Vitaly Vetrof / vetrof@gmail.com  / vetrof.com

import sys
import tabulate
import csv


def main():
    file_path = get_path()
    price_dict = get_menu(file_path)
    print_tabulate(price_dict)


def get_path():

    if len(sys.argv) == 2 and sys.argv[1][-4:] == '.csv':
        return sys.argv[1]
    else:
        print('No argument or file not .csv')
        sys.exit(1)


def get_menu(path):

    price_list_dicts = []

    try:
        with open(path) as file:
            reader = csv.DictReader(file)
            for row in reader:
                price_list_dicts.append(row)
    except FileNotFoundError:
        print('File non found')
        sys.exit(1)

    return price_list_dicts


def print_tabulate(d):
    print(tabulate.tabulate(d, headers='keys', tablefmt="grid"))


if __name__ == '__main__':
    main()
