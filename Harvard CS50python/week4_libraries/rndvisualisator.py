import random
import randomv

# random visualisator 100

dict_num = {}

# use my random time
for _ in range(1000):
    x = randomv.timernd()
    if x in dict_num:
        dict_num[x] = dict_num[x] + 1
    else:
        dict_num[x] = 1


# use standart random library
# for _ in range(1000):
#     x = random.randint(0, 98)
#     if x in dict_num:
#         dict_num[x] = dict_num[x] + 1
#     else:
#          dict_num[x] = 1


# visualisation
for key in range(100):
    if key in dict_num:
        n = dict_num[key]
    else:
        n = 0
    print(key, n, '*' * n)
