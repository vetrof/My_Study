import random

tasks = []

print('\nвведите список дел')
while True:
    x = input()
    if x == "":
        break
    tasks.append(x)

random.shuffle(tasks)

for x in tasks:
    print(x)

print()