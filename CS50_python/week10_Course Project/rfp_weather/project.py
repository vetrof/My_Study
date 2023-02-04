import  weatherdata
from colorama import init, Fore, Back, Style
import time

init(autoreset=True)

# todo написать глобальные переменные для границ желтой и зеленой зоны

def main():

    # todo сделать валидатор и конвертер в координаты
    location = 'astana'
    wdata = weatherdata.WeatherData(location)  # create weather data obj
    swdata = weatherdata.SpaceWeather()        # create space weather data obj

    # get data
    w_current = wdata.load_current()
    k_current = swdata.load_kp_index_current()
    w_forecast_today = wdata.load_forecast(0)
    w_forecast_tomorrow = wdata.load_forecast(1)
    k_forecast = swdata.load_kp_index_forecast()

    # print to console
    print_w_current(w_current)
    print_k_index_current(k_current)
    print_day_forecast(w_current, w_forecast_today)
    print_day_forecast(w_current, w_forecast_tomorrow)
    print_k_index_forecast(k_forecast)
#


# function area:

def print_w_current(w_current):
    color = ''
    print()

    # print and color
    for key in w_current:
        # color for wind
        if key == 'wind_kph' and w_current['wind_kph'] > 35:
            color = Fore.RED
        elif key == 'wind_kph' and w_current['wind_kph'] > 25:
            color = Fore.YELLOW
        # color for gust
        if key == 'gust_kph' and w_current['gust_kph'] > 35:
            color = Fore.RED
        elif key == 'gust_kph' and w_current['gust_kph'] > 25:
            color = Fore.YELLOW
        # color for pressure
        if key == 'pressure_mmHg' and w_current['pressure_mmHg'] > 770:
            color = Fore.RED
        elif key == 'pressure_mmHg' and w_current['pressure_mmHg'] > 765:
            color = Fore.YELLOW

        # print current weather
        print(f'{key:15} {color} {w_current[key]:>17}')
        color = ''


def print_k_index_current(k_kurrent):
    color = ''
    # print and color
    for key in k_kurrent:
        # color for k-index
        if key == 'kp_index' and k_kurrent['kp_index'] >= 5:
            color = Fore.RED
        elif key == 'kp_index' and k_kurrent['kp_index'] >= 3:
            color = Fore.YELLOW

        # print current weather
        print(f'{key:15} {color} {k_kurrent[key]:>17}')
        color = ''


def print_day_forecast(w_current, w_forecast):
    list_dict = []

    print()
    if w_forecast[0]['day'] == 0:
        print('Forecast Today')
    if w_forecast[0]['day'] == 1:
        print('Forecast Tomorrow')

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
                f" {round(w_forecast[i]['feelslike_c']):3}  {w_forecast[i]['humidity']:3}  {color_w}{round(w_forecast[i]['wind_kph'])} "
                f" {color_g}{round(w_forecast[i]['gust_kph']):3}   {color_p}{w_forecast[i]['pressure_mm']:3} "
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
                f"{w_current['localtime'][-5:]} {round(w_current['temp_c']):>3} "
                f" {round(w_current['feelslike_c']):>3}{w_current['humidity']:>5} {color_w}{round(w_current['wind_kph']):>3}"
                f"  {color_g}{round(w_current['gust_kph']):>3} {color_p}{w_current['pressure_mmHg']:>5} "
                f"  ")
            print('-----------------------------------')


def print_k_index_forecast(k_forecast):
    print('\nKP-Index forecast:')
    print(f'TimeUTC     Today  Tomorrow  Aftmrw')

    for time in k_forecast:

        color_t = Style.RESET_ALL
        color_to = Style.RESET_ALL
        color_afto = Style.RESET_ALL

        # color for k-index
        if float(k_forecast[time]['today']) > 5:
            color_t = Fore.RED
        elif float(k_forecast[time]['today']) > 3:
            color_t = Fore.YELLOW


        if float(k_forecast[time]['tomorrow']) > 5:
            color_t = Fore.RED
        elif float(k_forecast[time]['tomorrow']) > 3:
            color_t = Fore.YELLOW


        if float(k_forecast[time]['aftertomorrow']) > 5:
            color_t = Fore.RED
        elif float(k_forecast[time]['aftertomorrow']) > 3:
            color_t = Fore.YELLOW

        print(f"{time}     {color_t}{k_forecast[time]['today']}     {color_to}{k_forecast[time]['tomorrow']}     {color_afto}{k_forecast[time]['aftertomorrow']} ")



























if __name__ == '__main__':
    main()
