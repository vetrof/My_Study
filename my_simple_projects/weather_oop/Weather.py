
import requests
import json
import time

from colorama import init, Fore, Back, Style
init(autoreset=True)

class Weather:

    def __init__(self, loc):
        self.loc = loc
        self.search_link = (f'http://api.weatherapi.com/v1/forecast.json?key=df8a79d600db4388880121515232301&q={self.loc}&days=2&aqi=no&alerts=no')
        self.answer = requests.get(self.search_link).json()

    def now(self):

        # curent
        w_now = {}
        answer = self.answer
        w_now['localtime'] = answer['location']['localtime']
        w_now['city'] = answer['location']['name']
        w_now['temp_c'] = answer['current']['temp_c']
        w_now['feelslike_c'] = answer['current']['feelslike_c']
        w_now['humidity'] = answer['current']['humidity']
        w_now['wind_kph'] = answer['current']['wind_kph']
        w_now['gust_kph'] = answer['current']['gust_kph']
        w_now['pressure_mmHg'] = round(answer['current']['pressure_mb']* 0.75006375541921)
        return w_now

    def f_day(self, day):

        # forecast
        f_day = {}
        answer = self.answer

        for h in range(0, 24, 3):
            forecast = {}
            forecast['hour'] = h
            forecast['day'] = day
            forecast['time'] = \
                answer['forecast']['forecastday'][day]['hour'][h]['time']
            forecast['temp_c'] = \
                answer['forecast']['forecastday'][day]['hour'][h]['temp_c']
            forecast['feelslike_c'] = \
                answer['forecast']['forecastday'][day]['hour'][h]['feelslike_c']
            forecast['humidity'] = \
                answer['forecast']['forecastday'][day]['hour'][h]['humidity']
            forecast['wind_kph'] = \
                answer['forecast']['forecastday'][day]['hour'][h]['wind_kph']
            forecast['gust_kph'] = \
                answer['forecast']['forecastday'][day]['hour'][h]['gust_kph']
            forecast['pressure_mm'] = \
                round(answer['forecast']['forecastday'][day]['hour'][h]['pressure_mb'] * 0.75)
            f_day[h] = forecast

        return f_day

    @classmethod
    def print_now(cls, d):
        color = ''

        # todo сделать цветной вывод для ветра, порывов, давления.

        print()


        # print and color
        for key in d:
            # color for wind
            if key == 'wind_kph' and d['wind_kph'] > 35:
                color = Fore.RED
            elif key == 'wind_kph' and d['wind_kph'] > 25:
                color = Fore.YELLOW
            # color for gust
            if key == 'gust_kph' and d['gust_kph'] > 35:
                color = Fore.RED
            elif key == 'gust_kph' and d['gust_kph'] > 25:
                color = Fore.YELLOW
            # color for pressure
            if key == 'pressure_mmHg' and d['pressure_mmHg'] > 770:
                color = Fore.RED
            elif key == 'pressure_mmHg' and d['pressure_mmHg'] > 765:
                color = Fore.YELLOW

            # print current weather
            print(f'{key:15} {color} {d[key]:>20}')
            color = ''
        print()

    @classmethod
    def print_day_forecast(cls, now, d, index):
        list_dict = []

        if index == 0:
            print('Forecast Today')
        if index == 1:
            print('Forecast Tomorrow')

        for i in d:
            list_dict.append(d[i])
            loc_hour = time.localtime().tm_hour

            # print current weather into forecast range
            if d[i]['hour'] <= loc_hour < ((d[i]['hour']) + 3) and d[i]['day'] == 0:

                # color current
                # color for wind
                if now['wind_kph'] > 35:
                    color_w = Fore.RED
                elif now['wind_kph'] > 25:
                    color_w = Fore.YELLOW
                # color for gust
                if now['gust_kph'] > 35:
                    color_g = Fore.RED
                elif now['gust_kph'] > 25:
                    color_g = Fore.YELLOW
                # color for pressure
                if now['pressure_mmHg'] > 770:
                    color_p = Fore.RED
                elif now['pressure_mmHg'] > 765:
                    color_p = Fore.RED

                #print current weather
                print('---------------------------------------')
                print(
                    f"{now['localtime'][-5:]} {round(now['temp_c']):>3} "
                    f" {round(now['feelslike_c']):>3}{now['humidity']:>5} {color_w}{round(now['wind_kph']):>3}"
                    f"  {color_g}{round(now['gust_kph']):>3} {color_p}{now['pressure_mmHg']:>5} "
                    f"  ")
                print(f"Time  temp like hum wind gust press  ")
                print('---------------------------------------')
                continue

            color_w = Style.RESET_ALL
            color_g = Style.RESET_ALL
            color_p = Style.RESET_ALL
            color_h = Style.RESET_ALL

            # color for forecast
            # color for wind
            if d[i]['wind_kph'] > 35:
                color_w = Fore.RED
            elif d[i]['wind_kph'] > 25:
                color_w = Fore.YELLOW
            # color for gust
            if d[i]['gust_kph'] > 35:
                color_g = Fore.RED
            elif d[i]['gust_kph'] > 25:
                color_g = Fore.YELLOW
            # color for pressure
            if d[i]['pressure_mm'] > 770:
                color_p = Fore.RED
            elif d[i]['pressure_mm'] > 765:
                color_p = Fore.RED

            # print forecast data
            print(
                f"{d[i]['hour']:3}   {round(d[i]['temp_c']):3} "
                f" {round(d[i]['feelslike_c']):3}  {d[i]['humidity']:3}  {color_w}{round(d[i]['wind_kph'])} "
                f" {color_g}{round(d[i]['gust_kph']):3}   {color_p}{d[i]['pressure_mm']:3} "
                f" ")
        print()

    @classmethod
    def get_loc(cls, loc):
        # loc = 'astana'
        return Weather(loc)