import requests
import tabulate


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
        w_current = {}
        w_current['localtime'] = self.api_resp_w['location']['localtime']
        w_current['city'] = self.api_resp_w['location']['name']
        w_current['temp_c'] = self.api_resp_w['current']['temp_c']
        w_current['feelslike_c'] = self.api_resp_w['current']['feelslike_c']
        w_current['humidity'] = self.api_resp_w['current']['humidity']
        w_current['wind_kph'] = self.api_resp_w['current']['wind_kph']
        w_current['gust_kph'] = self.api_resp_w['current']['gust_kph']
        w_current['pressure_mmHg'] = round(self.api_resp_w['current']['pressure_mb'] * 0.75)
        return w_current

    def load_forecast(self, day):
        f_day = {}
        for h in range(0, 24, 3):  # 0 - 24 hour and step 3 hour
            w_forecast = {}
            w_forecast['hour'] = h
            w_forecast['day'] = day
            w_forecast['time'] = \
                self.api_resp_w['forecast']['forecastday'][day]['hour'][h]['time']
            w_forecast['temp_c'] = \
                self.api_resp_w['forecast']['forecastday'][day]['hour'][h]['temp_c']
            w_forecast['feelslike_c'] = \
                self.api_resp_w['forecast']['forecastday'][day]['hour'][h][
                    'feelslike_c']
            w_forecast['humidity'] = \
                self.api_resp_w['forecast']['forecastday'][day]['hour'][h]['humidity']
            w_forecast['wind_kph'] = \
                self.api_resp_w['forecast']['forecastday'][day]['hour'][h]['wind_kph']
            w_forecast['gust_kph'] = \
                self.api_resp_w['forecast']['forecastday'][day]['hour'][h]['gust_kph']
            w_forecast['pressure_mm'] = \
                round(self.api_resp_w['forecast']['forecastday'][day]['hour'][h][
                          'pressure_mb'] * 0.75)
            f_day[h] = w_forecast

        return f_day


class SpaceWeather:
    @staticmethod
    def load_kp_index_current():
        link = "https://services.swpc.noaa.gov/json/planetary_k_index_1m.json"
        api_resp_sw = requests.get(link).json()

        k_index_current = {}
        k_index_current['kp_index'] = api_resp_sw[357]['kp_index']
        return k_index_current

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
    sw = SpaceWeather()
    k_forecast = sw.load_kp_index_forecast()

    print(k_forecast)
    print()

    for time in k_forecast:
        print(f"{time}   {k_forecast[time]['today']}   {k_forecast[time]['tomorrow']}   {k_forecast[time]['aftertomorrow']} ")







if __name__ == '__main__':
    main()

