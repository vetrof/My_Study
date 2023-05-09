# https://www.weatherapi.com/api-explorer.aspx
# api key: df8a79d600db4388880121515232301

import tabulate
import requests
import json


class Weather():
    def __init__(self, location):
        weather_now = {}
        self.location = location
        self.weather_now_d = weather_now


    def weather_variable(self):

        loc = self.loc
        response = requests.get('https://api.weatherapi.com/v1/current.'
                                'json?key=df8a79d600db43888801215152323'
                                '01&q=astana&aqi=no').json()

        # create separate value
        self.name = response['location']['name']
        self.temp_c = response['current']['temp_c']
        self.wind_kph = response['current']['wind_kph']
        self.pressure_mb = response['current']['pressure_mb']
        self.feelslike_c = response['current']['feelslike_c']
        self.gust_kph = response['current']['gust_kph']
        self.localtime = response['location']['localtime']


    def weather_dict(self):
        response = requests.get(f'https://api.weatherapi.com/v1/current.json?key=df8a79d600db4388880121515232301&q={self.location}&aqi=no').json()

        # create dict with weather data
        self.weather_now_d['localtime'] = response['location']['localtime']
        self.weather_now_d['name'] = response['location']['name']
        self.weather_now_d['temp_c'] = response['current']['temp_c']
        self.weather_now_d['feelslike_c'] = response['current']['feelslike_c']
        self.weather_now_d['pressure_mb'] = response['current']['pressure_mb']
        self.weather_now_d['wind_kph'] = response['current']['wind_kph']
        self.weather_now_d['gust_kph'] = response['current']['gust_kph']
        return self.weather_now_d

weather = Weather('astana')
w_now = weather.weather_dict()

print('////////////////')
print()
for w in w_now:
    print(w, w_now[w])
print()
print('////////////////')
