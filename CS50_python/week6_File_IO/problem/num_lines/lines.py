# True num lines of code
# Harvard / cs50p / python
# problem set week 6  https://cs50.harvard.edu/python/2022/psets/6/
# Vitaly Vetrof / vetrof@gmail.com  / vetrof.com
import sys


def main():
    file_path = get_file_path()
    n_line = get_line_list(file_path)
    print(n_line)


def get_file_path():
    if len(sys.argv) == 2 and sys.argv[1][-3:] == '.py':
        return sys.argv[1]
    else:
        sys.exit(1)


def get_line_list(path):
    new_list = []
    prefix_tuple = ('#', '\n')

    try:
        with open(path) as file:
            all_lines = file.readlines()
    except FileNotFoundError:
        sys.exit(1)

    for line in all_lines:

        if line.lstrip(' ').startswith(prefix_tuple):
            continue
        else:
            new_list.append(line)

    return len(new_list)


if __name__ == '__main__':
    main()
