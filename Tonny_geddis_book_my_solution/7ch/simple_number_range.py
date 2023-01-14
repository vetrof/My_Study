#упражнение 5:18
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
    for i in range(1, 1000):
        status = simple_number_validator(i)
        if status:
            print(f'{i}', end=', ')

main()












