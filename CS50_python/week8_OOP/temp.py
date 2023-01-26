import requests
import json


search_link = (f'http://api.weatherapi.com/v1/forecast.json?key=df8a79d600db4388880121515232301&q=astana&days=2&aqi=no&alerts=no')


responce = requests.get(search_link).json()

# print(json.dumps(responce, indent=2))

# file = open('weather.json', 'w')
# file.write(json.dumps(responce, indent=2))

for h in range(0, 24):
    wind = responce['forecast']['forecastday'][1]['hour'][h]['wind_kph']
    press = responce['forecast']['forecastday'][1]['hour'][h]['pressure_mb'] * 0.75
    print(h, round(press), wind)





# /forecast/forecastday/1/day/maxtemp_c
# /forecast/forecastday/0/hour/3/pressure_mb