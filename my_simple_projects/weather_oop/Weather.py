
import requests
import json
import time

from colorama import init, Fore, Back, Style
init(autoreset=True)

class Weather:

    def __init__(self, loc):
        self.loc = loc
        self.search_link = (f'http://api.weatherapi.com/v1/forecast.json?key=df8a79d600db4388880121515232301&q=astana&days=2&aqi=no&alerts=no')
        self.answer = requests.get(self.search_link).json()

    def now(self):

        # curent
        w_now = {}
        answer = self.answer
        w_now['localtime'] = answer['location']['localtime']
        w_now['city'] = answer['location']['name']
        w_now['temp_c'] = answer['current']['temp_c']
        w_now['feelslike_c'] = answer['current']['feelslike_c']
        w_now['wind_kph'] = answer['current']['wind_kph']
        w_now['gust_kph'] = answer['current']['gust_kph']
        w_now['pressure_mmHg'] = round(answer['current']['pressure_mb']* 0.75006375541921)
        w_now['humidity'] = answer['current']['humidity']
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


        # colorama area
        for key in d:

            if key == 'wind_kph' and d['wind_kph'] > 35:
                color = Fore.RED
            elif key == 'wind_kph' and d['wind_kph'] > 25:
                color = Fore.YELLOW

            if key == 'gust_kph' and d['gust_kph'] > 35:
                color = Fore.RED
            elif key == 'gust_kph' and d['gust_kph'] > 25:
                color = Fore.YELLOW

            if key == 'pressure_mmHg' and d['pressure_mmHg'] > 770:
                color = Fore.RED
            elif key == 'pressure_mmHg' and d['pressure_mmHg'] > 765:
                color = Fore.YELLOW

            # print current weather
            print(f'{key:15} {color} {d[key]:>20}')
            color = ''

    @classmethod
    def print_day_forecast(cls, now, d, index):

        list_dict = []

        if index == 0:
            print('\nForecast Today')
        if index == 1:
            print('\nForecast Tomorrow')

        for i in d:
            list_dict.append(d[i])
            loc_hour = time.localtime().tm_hour

            # print(f"(( {d[i]['hour']} {loc_hour}  {d[i]['day']} ))")

            if d[i]['hour'] <= loc_hour < ((d[i]['hour']) + 3) and d[i]['day'] == 0:
                print('---------------------------------------')
                print(
                    f"{now['localtime'][-5:]} {round(now['temp_c'])}  {round(now['feelslike_c'])}   {round(now['wind_kph'])}   {round(now['gust_kph'])}   {now['pressure_mmHg']}   {now['humidity']}")
                print(f"Time  temp like wind gust press  hum")
                print('---------------------------------------')
                continue

            print(
                f"{d[i]['hour']:3}   {round(d[i]['temp_c']):3}  {round(d[i]['feelslike_c']):3}   {round(d[i]['wind_kph'])}  {round(d[i]['gust_kph']):3}   {d[i]['pressure_mm']:3}  {d[i]['humidity']:3}")

            if d[i]['hour'] < loc_hour < ((d[i]['hour']) + 3) and d[i][
                'day'] == 0:
                print(f"Time temp like wind gust press  hum")
                print('---------------------------------------')

        print()

    @classmethod
    def get_loc(cls):
        loc = 'astana'
        return Weather(loc)