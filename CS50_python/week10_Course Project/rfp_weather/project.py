# Course project
#
# Harvard / cs50p / python
# problem set week 8  https://cs50.harvard.edu/python/2022/
# Vitaly (Vetrof) / vetrof@gmail.com  / vetrof.com

import  weatherdata
from colorama import init, Fore, Back, Style
import time

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

# todo перенести формирование индексов в классы
# todo формировать два словаря уже с индексами
# todo оставить в этом файле только main и функции печати с colorrama

def main():

    # create obj and get API request for you city
    while True:
        try:
            usr_input = input('You location: ')
            location = check_input(usr_input)
            wdata = weatherdata.WeatherData(location)  # create weather data obj
            swdata = weatherdata.SpaceWeather()        # create space weather data obj
        except ValueError as err:
            print(err)
            continue
        else:
            break

    # get current data
    w_current = wdata.load_current()
    k_current = swdata.load_kp_index_current()
    m_kurrent = m_index_now(w_current, k_current)

    # get forecast data
    w_forecast_today = wdata.load_forecast(0)
    w_forecast_tomorrow = wdata.load_forecast(1)
    k_forecast = swdata.load_kp_index_forecast()

    # print to console
    print_now(w_current, k_current)
    print (print_m_now(m_kurrent))
    print_day_forecast(w_current, w_forecast_today)
    print_day_forecast(w_current, w_forecast_tomorrow)
    print_k_index_forecast(k_forecast)


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
        if key == 'pressure_mmHg' and w_current['pressure_mmHg'] > PRESSURE_RED_ZONE:
            color = Fore.RED
        elif key == 'pressure_mmHg' and w_current['pressure_mmHg'] > PRESSURE_YELLOW_ZONE:
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
        color_h = Style.RESET_ALL


        # color grade for forecast
        # for wind
        if w_forecast[i]['wind_kph'] > 35:
            color_w = Fore.RED
        elif w_forecast[i]['wind_kph'] > 25:
            color_w = Fore.YELLOW
        # for gust
        if w_forecast[i]['gust_kph'] > 35:
            color_g = Fore.RED
        elif w_forecast[i]['gust_kph'] > 25:
            color_g = Fore.YELLOW
        # for pressure
        if w_forecast[i]['pressure_mm'] > 770:
            color_p = Fore.RED
        elif w_forecast[i]['pressure_mm'] > 765:
            color_p = Fore.YELLOW

        # NOT print forecast data if current hour == forecast
        if loc_hour == w_forecast[i]['hour'] and w_forecast[i]['day'] == 0:
            pass

        else:
            print(
                f"{w_forecast[i]['hour']:3}   {round(w_forecast[i]['temp_c']):3} "
                f" {round(w_forecast[i]['feelslike_c']):3}  {w_forecast[i]['humidity']:3}  {color_w}{round(w_forecast[i]['wind_kph']):2} "
                f"  {color_g}{round(w_forecast[i]['gust_kph']):2}   {color_p}{w_forecast[i]['pressure_mm']:3} "
                f" ")

        # print current weather in forecast modile only today!!
        # if d[i]['hour'] <= loc_hour < ((d[i]['hour']) + 3) and d[i]['day'] == 0:
        if w_forecast[i]['hour'] <= loc_hour < (w_forecast[i]['hour'] + 3) and w_forecast[i]['day'] == 0:


            # color current
            # wind
            if w_current['wind_kph'] > 35:
                color_w = Fore.RED
            elif w_current['wind_kph'] > 25:
                color_w = Fore.YELLOW
            # gust
            if w_current['gust_kph'] > 35:
                color_g = Fore.RED
            elif w_current['gust_kph'] > 25:
                color_g = Fore.YELLOW
            # pressure
            if w_current['pressure_mmHg'] > 770:
                color_p = Fore.RED
            elif w_current['pressure_mmHg'] > 765:
                color_p = Fore.YELLOW

            # print current weather
            print('-----------------------------------')
            print(
                f"{w_current['localtime'][-5:]:5} {round(w_current['temp_c']):3} "
                f" {round(w_current['feelslike_c']):3}  {w_current['humidity']:3}  {color_w}{round(w_current['wind_kph']):2}"
                f"   {color_g}{round(w_current['gust_kph']):2}   {color_p}{w_current['pressure_mmHg']:3} "
                f"  ")
            print('-----------------------------------')


def print_k_index_forecast(k_forecast):
    init(autoreset=True)
    print('\nKP-Index:')
    print(f'TimeUTC     Today  Tomorrow  Aftmrw')

    for time in k_forecast:

        color_t = Style.RESET_ALL
        color_to = Style.RESET_ALL
        color_afto = Style.RESET_ALL

        # color for k-index
        if float(k_forecast[time]['today']) > K_RED_ZONE:
            color_t = Fore.RED
        elif float(k_forecast[time]['today']) > K_YELLOW_ZONE:
            color_t = Fore.YELLOW


        if float(k_forecast[time]['tomorrow']) > K_RED_ZONE:
            color_t = Fore.RED
        elif float(k_forecast[time]['tomorrow']) > K_YELLOW_ZONE:
            color_t = Fore.YELLOW


        if float(k_forecast[time]['aftertomorrow']) > K_RED_ZONE:
            color_t = Fore.RED
        elif float(k_forecast[time]['aftertomorrow']) > K_YELLOW_ZONE:
            color_t = Fore.YELLOW

        print(f"{time}     {color_t}{k_forecast[time]['today']}     {color_to}{k_forecast[time]['tomorrow']}     {color_afto}{k_forecast[time]['aftertomorrow']} ")
    print()


def m_index_now(w_current, k_current):
    temp_c = w_current['temp_c']
    feelslike_c = w_current['feelslike_c']
    wind_kph = w_current['wind_kph']
    gust_kph = w_current['gust_kph']
    pressure_mmHg = w_current['pressure_mmHg']
    kp_index = k_current['kp_index']
    m_index = abs(feelslike_c - temp_c) + max(wind_kph, gust_kph) + abs(PRESSURE_NEUTRAL - pressure_mmHg) + (kp_index * KP_FACTOR_IN_M_INDEX)
    return {'m_index': m_index}


if __name__ == '__main__':
    main()
