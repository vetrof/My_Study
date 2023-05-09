
#программа которая вычисляет цвет сектора на рулетке в зависимости от его номера

#получаем номер сектора
import random

sector = random.randint(0, 36)

#создаем условия для секторов
if sector >= 1 and sector <= 10:     #ограничиваем сектор
    if sector % 2 == 0:              #четные
        color = 'black'
    else:                            #нечетные
        color = 'red'

if sector >= 11 and sector <= 18:     #ограничиваем сектор
    if sector % 2 == 0:              #четные
        color = 'red'
    else:                            #нечетные
        color = 'black'

if sector >= 19 and sector <= 28:     #ограничиваем сектор
    if sector % 2 == 0:              #четные
        color = 'black'
    else:                            #нечетные
        color = 'red'

if sector >= 29 and sector <= 36:     #ограничиваем сектор
    if sector % 2 == 0:              #четные
        color = 'red'
    else:                            #нечетные
        color = 'black'

if sector == 0:
    color = 'green'

if sector > 36:
    print('eror!!!')

print(sector, color)

