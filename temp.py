# https://services.swpc.noaa.gov/text/3-day-forecast.txt

import requests
import re

def load_kp_index_forecast():
    text = ''
    resp = requests.get('https://services.swpc.noaa.gov/text/3-day-forecast.txt')
    open('sw_k_for.txt', 'wb').write(resp.content)

    file = open('sw_k_for.txt')
    n = file.readlines()
    kp_for = {}

    flag = 0
    x = 1
    for i in n:
        i = i.strip().split()
        if '00-03UT' in i:
            flag = 1
        if flag == 1 and x < 9:
            # print(i[0])
            x += 1
            kp_for[i[0]] = {'today': i[1], 'tomorrow': i[2], 'aftertomorrow': i[3]}

    return kp_forecast

load_kp_index_forecast()