import random
number = random.randint(0, 10)

print(number)

for i in range(3):
    print('попытка', i + 1,)
    x1 = int(input())
    if x1 == number:
        print('Вы выиграли')
        break
    if x1 > number:
        print('Загаданное число меньше')
    if x1 < number:
        print('Загаданное число больше')

if x1 != number:
    print('Вы проиграли')

