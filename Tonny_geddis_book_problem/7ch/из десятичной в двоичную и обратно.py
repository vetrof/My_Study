
bit = 128, 64, 32, 16, 8, 4, 2, 1

number = 111

while number > 0:                  #цикл пока остаток от деления не будет ноль
    for i in bit:
        if number // i == 1:       #если остаток равен 1 то рисуем 1
            print('1', end='')
            number %= i            # привсваиваем значение остатка от деления

        else:
            print('0', end='')     #если нет то 0

    print()
 