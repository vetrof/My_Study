import re

tx = ''
file = open('sw_k_for.txt')
n = file.readlines()


flag = 0
for i in n:
    if 'NOAA Kp' in i:
        flag = 1

    if 'Rationale' in i:
        flag = 0

    if flag == 1:
        print(i.strip())


def load_kp_index_forecast():
    ...



