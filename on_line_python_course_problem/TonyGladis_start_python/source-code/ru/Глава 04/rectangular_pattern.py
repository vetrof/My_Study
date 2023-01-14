# Эта программа выводит прямоугольную комбинацию 
# звездочек.
rows = int(input('Сколько строк? '))
cols = int(input('Сколько столбцов? '))

for r in range(rows):
    for c in range(cols):
        print('*', end='')
    print()