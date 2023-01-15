 # Fuel Gauge

def main():
    x, y = get_fuel()
    percent_fuel = round((100 / y) * x)

    if percent_fuel <= 1:
        print('E')
    elif percent_fuel >= 99:
        print('F')
    else:
        print(f'{percent_fuel}%')


def get_fuel():
    while True:
        usr_input = input('Fraction: ')
        try:
            a, b = usr_input.split("/")
            x = int(a)
            y = int(b)

        except ValueError:
            pass

        else:
            if x <= y != 0:
                return x, y


main()
