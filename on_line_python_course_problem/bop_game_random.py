import random

random_number = random.randint(1, 5)

print('машина загадала', random_number)

user_number = input('введи число от 1 до 5 ти: ')

# мое решение игры
if random_number == int(user_number):
    print('ты угадал!!')
else:
    print('you LUSER!! ha ha ha')







