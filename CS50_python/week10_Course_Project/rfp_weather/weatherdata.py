#  file with classes for

import requests


# class for get weather data from api
class WeatherData:
    def __init__(self, loc):
        self.location = loc
        self.search_link = (f'http://api.weatherapi.com/v1/forecast.'
                            f'json?key=df8a79d600db4388880121515232301'
                            f'&q={self.location}&days=2&aqi=no&alerts=no')

        self.api_resp_w = requests.get(self.search_link).json()

        if 'error' in self.api_resp_w:
            raise ValueError('No matching location found.')

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, loc):
        self._location = loc

    def load_current(self):

        w_current = {'localtime': self.api_resp_w['location']['localtime'],
                     'city': self.api_resp_w['location']['name'],
                     'temp_c': self.api_resp_w['current']['temp_c'],
                     'feelslike_c': self.api_resp_w['current']['feelslike_c'],
                     'humidity': self.api_resp_w['current']['humidity'],
                     'wind_kph': self.api_resp_w['current']['wind_kph'],
                     'gust_kph': self.api_resp_w['current']['gust_kph'],
                     'pressure_mmHg': round(
                         self.api_resp_w['current']['pressure_mb'] * 0.75)}
        return w_current

    def load_forecast(self, day):
        f_day = {}
        for h in range(0, 24, 3):  # 0 - 24 hour and step 3 hour
            w_forecast = {'hour': h, 'day': day, 'time':
                self.api_resp_w['forecast']['forecastday'][day]['hour'][h][
                    'time'], 'temp_c':
                              self.api_resp_w['forecast']['forecastday'][day][
                                  'hour'][h]['temp_c'], 'feelslike_c':
                              self.api_resp_w['forecast']['forecastday'][day][
                                  'hour'][h][
                                  'feelslike_c'], 'humidity':
                              self.api_resp_w['forecast']['forecastday'][day][
                                  'hour'][h]['humidity'], 'wind_kph':
                              self.api_resp_w['forecast']['forecastday'][day][
                                  'hour'][h]['wind_kph'], 'gust_kph':
                              self.api_resp_w['forecast']['forecastday'][day][
                                  'hour'][h]['gust_kph'], 'pressure_mm': round(
                self.api_resp_w['forecast']['forecastday'][day]['hour'][h][
                    'pressure_mb'] * 0.75)}
            f_day[h] = w_forecast

        return f_day


# class for get space weather data from site services.swpc.noaa.gov
class SpaceWeather:

    # get current K- index
    @staticmethod
    def load_kp_index_current():
        link = "https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json"
        api_resp_sw = requests.get(link).json()
        l = len(api_resp_sw) - 1

        k_index_current = {'kp_index': float(api_resp_sw[l][1])}
        return k_index_current

    # get 2 day forecast K- index from txt file
    @staticmethod
    def load_kp_index_forecast():
        text = ''
        resp = requests.get(
            'https://services.swpc.noaa.gov/text/3-day-forecast.txt')
        open('sw_k_for.txt', 'wb').write(resp.content)

        file = open('sw_k_for.txt')
        n = file.readlines()
        kp_forecast = {}

        flag = 0
        x = 1
        for i in n:
            i = i.strip().split()
            if '00-03UT' in i:
                flag = 1
            if flag == 1 and x < 9:
                # print(i[0])
                x += 1
                kp_forecast[i[0]] = {'today': i[1], 'tomorrow': i[2],
                                     'aftertomorrow': i[3]}

        return kp_forecast


def main():
    ...


if __name__ == '__main__':
    main()
