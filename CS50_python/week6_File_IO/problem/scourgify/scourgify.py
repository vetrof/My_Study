
# Scourgify
# Harvard / cs50p / python
# problem set week 6  https://cs50.harvard.edu/python/2022/psets/6/
# Vitaly Vetrof / vetrof@gmail.com  / vetrof.com

import csv
import sys


def main():
    path1, path2 = get_path()
    text = get_text_from_file(path1)
    new_text = reformat(text)
    record_to_csv(path2, new_text)


def get_path():

    if len(sys.argv) < 3:
        print('Too few command-line arguments')
        sys.exit(1)

    elif len(sys.argv) > 3:
        print('Too many command-line arguments')
        sys.exit(1)

    else:
        return sys.argv[1], sys.argv[2]


def get_text_from_file(path1):
    # print(path1)

    names = []

    try:
        with open(path1) as file:
            read = csv.DictReader(file)
            for i in read:
                names.append(i)

    except FileNotFoundError:
        print('Could not read', path1)
        sys.exit(1)

    return names


def reformat(names):
    new_list = []

    for row in names:
        last, first = row['name'].split(',')
        # print(first, last , i['house'])
        new_list.append({'first': first.lstrip(),
                         'last': last,
                         'house': row['house']})

    return new_list


def record_to_csv(path, text):

    print(text)

    with open(path, 'w') as file:
        write = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
        write.writeheader()
        for row in text:
            write.writerow(row)


if __name__ == '__main__':
    main()
