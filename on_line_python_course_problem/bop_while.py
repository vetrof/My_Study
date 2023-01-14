number = 23
running = True

while running:
    guess = int(input('введите цело число: '))

    if guess == number:
        print('вы угадали')
        running = False #останавливаем цикл while
    elif guess < number:
        print('загадонное число больше')

    else:
        print('загадоное число меньше этого')

#else:
 #   print(' цикл while finish')

print('завершение')