#упражнение 5:17


def simple_number_validator(x):
    n = 0
    for i in range(2, x):
        if x % i == 0:
            n += 1
    if n > 0:
        return False
    else:
        return True
def main():
    num = int(input('number - '))
    n = simple_number_validator(num)
    if n:
        print('number simple')
    else:
        print('number non simple')

main()












