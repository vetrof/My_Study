#!/usr/bin/env python3
# Course project
#
# Harvard / cs50p / python
# problem set week 8  https://cs50.harvard.edu/python/2022/
# Vitaly (Vetrof) / vetrof@gmail.com  / vetrof.com

import time
import csv

from colorama import init, Fore, Style

# import class module
import weatherdata

# set global value range zone for color warning
WIND_RED_ZONE = 35
WIND_YELLOW_ZONE = 25
GUST_RED_ZONE = 35
GUST_YELLOW_ZONE = 25
PRESSURE_RED_ZONE = 770
PRESSURE_YELLOW_ZONE = 765
K_RED_ZONE = 5
K_YELLOW_ZONE = 3
M_RED_ZONE = 70
M_YELLOW_ZONE = 40
KP_FACTOR_IN_M_INDEX = 10
PRESSURE_NEUTRAL = 760
DATA_FILE = 'data_ml/selffeel_data_vetrof@gmail.com.csv'  # file for statistic

# todo найти поставщика форекаст k index
# todo в кслассе не разрезать приходящие словари
# todo добавить в классы методы которые будут красить текст
# todo конкатенировать все словари в один с момощью |


def main():
    wdata = None

    # get user location and scheck user input
    # create weather obj
    while True:
        try:
            usr_input = input('You location: ')
            location = check_input(usr_input)
            wdata = weatherdata.WeatherData(location)  # create weather obj
        except ValueError as err:
            print(err)
            continue
        else:
            break

    # create space weather oj
    swdata = weatherdata.SpaceWeather()

    # get current data
    w_current = wdata.load_current()
    k_current = swdata.load_kp_index_current()
    m_kurrent = m_index_now(w_current, k_current)

    # get forecast data
    w_forecast_today = wdata.load_forecast(0)
    w_forecast_tomorrow = wdata.load_forecast(1)
    k_forecast = swdata.load_kp_index_forecast()
    # print(k_forecast, '*************************************')

    # print to console
    print_now(w_current, k_current)
    print(print_m_now(m_kurrent))
    print_day_forecast(w_current, w_forecast_today)
    print_day_forecast(w_current, w_forecast_tomorrow)
    print_k_index_forecast(k_forecast)

    # input current user feel
    answer = None
    while True:
        try:
            user_input = input('Ваше самочувствие (0 - 5): ')
            feel = check_status_feel(user_input)
            info = input('Подробно: ')
            answer = {'self_feel': feel, 'self_info': info}
        except ValueError:
            print('Только цифры от 0 до 5ти')
            continue
        else:
            break

    # record user feel info to file
    new_data = w_current | k_current | answer  # соединяем все словари в один
    from_file = load_dict_from_csv()  # загружаем словари из csv файла
    from_file.append(new_data)  # добавляем новые данные к загруженным словарям
    save_dict_to_csv_file(from_file)  # сохраняем все данные в csv


def check_input(city):
    if city.isdigit():
        raise ValueError('is digit')
    if city == '':
        raise ValueError('is empy')
    return city


def print_now(w_current, k_kurrent):
    init(autoreset=True)
    color = ''
    print()
    print('-------------------------')
    print("Now:")

    # print and color weather
    for key in w_current:
        # color for wind
        if key == 'wind_kph' and w_current['wind_kph'] > WIND_RED_ZONE:
            color = Fore.RED
        elif key == 'wind_kph' and w_current['wind_kph'] > WIND_YELLOW_ZONE:
            color = Fore.YELLOW
        # color for gust
        if key == 'gust_kph' and w_current['gust_kph'] > GUST_RED_ZONE:
            color = Fore.RED
        elif key == 'gust_kph' and w_current['gust_kph'] > GUST_YELLOW_ZONE:
            color = Fore.YELLOW
        # color for pressure
        if key == 'pressure_mmHg' and w_current['pressure_mmHg'] >= \
                PRESSURE_RED_ZONE:
            color = Fore.RED
        elif key == 'pressure_mmHg' and w_current['pressure_mmHg'] \
                >= PRESSURE_YELLOW_ZONE:
            color = Fore.YELLOW

        print(f'{key:15} {color} {w_current[key]:>17}')
        color = ''

    # print and color K index
    color = ''
    for key in k_kurrent:
        if key == 'kp_index' and k_kurrent['kp_index'] >= K_RED_ZONE:
            color = Fore.RED
        elif key == 'kp_index' and k_kurrent['kp_index'] >= K_YELLOW_ZONE:
            color = Fore.YELLOW
        print(f'{key:15} {color} {k_kurrent[key]:>17}')
        color = ''


def print_m_now(m_kurrent):
    # print and color M index
    color = ''
    for key in m_kurrent:
        if key == 'm_index' and m_kurrent['m_index'] >= M_RED_ZONE:
            color = Fore.RED
        elif key == 'm_index' and m_kurrent['m_index'] >= M_YELLOW_ZONE:
            color = Fore.YELLOW
        return f'{key:15} {color} {round(m_kurrent[key]):>17}'


def print_day_forecast(w_current, w_forecast):
    init(autoreset=True)
    list_dict = []

    print()
    if w_forecast[0]['day'] == 0:
        print('Today:')
    if w_forecast[0]['day'] == 1:
        print('Tomorrow:')

    print(f"Time  temp like hum wind gust press  ")

    for i in w_forecast:
        list_dict.append(w_forecast[i])
        loc_hour = time.localtime().tm_hour

        # create reset style for colorama lib
        color_w = Style.RESET_ALL
        color_g = Style.RESET_ALL
        color_p = Style.RESET_ALL

        # color grade for forecast
        # for wind
        if w_forecast[i]['wind_kph'] > WIND_RED_ZONE:
            color_w = Fore.RED
        elif w_forecast[i]['wind_kph'] > WIND_YELLOW_ZONE:
            color_w = Fore.YELLOW
        # for gust
        if w_forecast[i]['gust_kph'] > GUST_RED_ZONE:
            color_g = Fore.RED
        elif w_forecast[i]['gust_kph'] > GUST_YELLOW_ZONE:
            color_g = Fore.YELLOW
        # for pressure
        if w_forecast[i]['pressure_mm'] >= PRESSURE_RED_ZONE:
            color_p = Fore.RED
        elif w_forecast[i]['pressure_mm'] >= PRESSURE_YELLOW_ZONE:
            color_p = Fore.YELLOW

        # NOT print forecast data if current hour == forecast
        if loc_hour == w_forecast[i]['hour'] and w_forecast[i]['day'] == 0:
            pass

        else:
            print(
                f"{w_forecast[i]['hour']:3} "
                f"  {round(w_forecast[i]['temp_c']):3} "
                f" {round(w_forecast[i]['feelslike_c']):3} "
                f" {w_forecast[i]['humidity']:3}  {color_w}"
                f"{round(w_forecast[i]['wind_kph']):2} "
                f"  {color_g}{round(w_forecast[i]['gust_kph']):2}  "
                f" {color_p}{w_forecast[i]['pressure_mm']:3} "
                f" ")

        # print current weather in forecast modile only today!!
        if w_forecast[i]['hour'] <= loc_hour < (w_forecast[i]['hour'] + 3)\
                and w_forecast[i]['day'] == 0:

            color_w = Style.RESET_ALL
            color_g = Style.RESET_ALL
            color_p = Style.RESET_ALL

            # color current
            # wind
            if w_current['wind_kph'] > WIND_RED_ZONE:
                color_w = Fore.RED
            elif w_current['wind_kph'] > WIND_YELLOW_ZONE:
                color_w = Fore.YELLOW
            # gust
            if w_current['gust_kph'] > GUST_RED_ZONE:
                color_g = Fore.RED
            elif w_current['gust_kph'] > GUST_YELLOW_ZONE:
                color_g = Fore.YELLOW
            # pressure
            if w_current['pressure_mmHg'] >= PRESSURE_RED_ZONE:
                color_p = Fore.RED
            elif w_current['pressure_mmHg'] >= PRESSURE_YELLOW_ZONE:
                color_p = Fore.YELLOW

            # print current weather
            print('-----------------------------------')
            print(
                f"{w_current['localtime'][-5:]:5} "
                f"{round(w_current['temp_c']):3} "
                f" {round(w_current['feelslike_c']):3} "
                f" {w_current['humidity']:3}  "
                f"{color_w}{round(w_current['wind_kph']):2}"
                f"   {color_g}{round(w_current['gust_kph']):2} "
                f" {color_p}{w_current['pressure_mmHg']:3} "
                f"  ")
            print('-----------------------------------')


def print_k_index_forecast(k_forecast):
    # print forecast k index
    init(autoreset=True)
    print('\nKP-Index:')
    print(f'TimeUTC     Today  Tomorrow  Aftmrw')

    for times in k_forecast:
        color_t = Style.RESET_ALL
        color_to = Style.RESET_ALL
        color_afto = Style.RESET_ALL

        # color for k-index
        if float(k_forecast[times]['today']) >= K_RED_ZONE:
            color_t = Fore.RED
        elif float(k_forecast[times]['today']) >= K_YELLOW_ZONE:
            color_t = Fore.YELLOW

        if float(k_forecast[times]['tomorrow']) >= K_RED_ZONE:
            color_to = Fore.RED
        elif float(k_forecast[times]['tomorrow']) >= K_YELLOW_ZONE:
            color_to = Fore.YELLOW

        if float(k_forecast[times]['aftertomorrow']) >= K_RED_ZONE:
            color_afto = Fore.RED
        elif float(k_forecast[times]['aftertomorrow']) >= K_YELLOW_ZONE:
            color_afto = Fore.YELLOW

        print(
            f"{times}     {color_t}{k_forecast[times]['today']}   "
            f"  {color_to}{k_forecast[times]['tomorrow']}  "
            f"   {color_afto}{k_forecast[times]['aftertomorrow']} ")
    print()


def m_index_now(w_current, k_current):
    # create value
    temp_c = w_current['temp_c']
    feelslike_c = w_current['feelslike_c']
    wind_kph = w_current['wind_kph']
    gust_kph = w_current['gust_kph']
    pressure_mmhg = w_current['pressure_mmHg']
    kp_index = k_current['kp_index']

    # calculate M - index
    m_index = abs(feelslike_c - temp_c) + max(wind_kph, gust_kph) + abs(
        PRESSURE_NEUTRAL - pressure_mmhg) + (kp_index * KP_FACTOR_IN_M_INDEX)
    return {'m_index': m_index}


# func for record user self feel data to file
def check_status_feel(self_feel):
    self_feel = int(self_feel)
    if self_feel < 0 or self_feel > 5:
        raise ValueError
    return self_feel


def load_dict_from_csv():
    create_file = open(DATA_FILE, 'a')
    create_file.close()

    dict_from_file = []
    with open(DATA_FILE) as csvfile:
        file = csv.DictReader(csvfile)

        for i in file:
            dict_from_file.append(i)
    return dict_from_file


def save_dict_to_csv_file(d):
    keys_names = ['localtime',
                  'city',
                  'temp_c',
                  'feelslike_c',
                  'humidity',
                  'wind_kph',
                  'gust_kph',
                  'pressure_mmHg',
                  'kp_index',
                  'self_feel',
                  'self_info', ]
    # write to file
    with open(DATA_FILE, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys_names)
        writer.writeheader()
        writer.writerows(d)

    print('Спасибо! Данные записаны.')
    print('-------------------------')
    print()


if __name__ == '__main__':
    main()
