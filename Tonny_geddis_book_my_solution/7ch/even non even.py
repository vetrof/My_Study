#упражнение 5:16
import random

even = 0
non_even = 0
number = 100

for i in range(number):
    x = random.randint(0, 10000)
    if x % 2 == 0:
        even += 1
    else:
        non_even += 1

print(f'even number {even} \nnoneven {non_even}')





