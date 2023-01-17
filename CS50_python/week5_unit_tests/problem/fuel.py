# Fuel Gauge
# Harvard / cs50p / python
# problem set week 5  https://cs50.harvard.edu/python/2022/psets/5/
# Vitaly Vetrof / vetrof@gmail.com  / vetrof.com

def main():

    usr_input = input('Fraction: ')
    percentage = convert(usr_input)
    print(gauge(percentage))


def convert(fraction):

        try:
            a, b = fraction.split("/")
            x = int(a)
            y = int(b)

            if y == 0:
                raise ZeroDivisionError

            if x > y:
                raise ValueError

        except ValueError:
            raise ValueError

        except ZeroDivisionError:
            raise ZeroDivisionError

        else:
            return round((100 / y) * x)


def gauge(percentage):

    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f'{percentage}%'


if __name__ == "__main__":
    main()
