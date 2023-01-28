
import requests
from bs4 import BeautifulSoup

#
# https://yandex.com.am/weather/
# https://yandex.com.am/weather/?lat=55.75581741&lon=37.61764526
# temp fact__temp fact__temp_size_s
# <div class="temp fact__temp fact__temp_size_s" role="text"><span class="temp__value temp__value_with-unit">−13</span></div>
#


# parsing:
# привсваиваем переменной ссылку на страницу с погодой
url = 'https://yandex.com.am/weather/?lat=55.75581741&lon=37.61764526' # astana
# url = 'https://yandex.com.am/weather/astana' # astana
# url = 'https://yandex.com.am/weather/astana?lat=51.143974&lon=71.435806' # astana

# проверяем ответ сервера
response = requests.get(url)
print(response)

# получаем исходный код
bs = BeautifulSoup(response.text,"lxml")
# print(bs)

# ищем по тегу и классу
temp = bs.find_all('div', 'sun-card__info-item')
# print(temp)
print(temp[1].text)

# ----------------------------

# url = f'https://yandex.com.am/weather/astana?lat=51.143974&lon=71.435806'
#
# # проверяем ответ сервера
# response = requests.get(url)
# print(response)
#
# # получаем исходный код
# bs = BeautifulSoup(response.text, "lxml")
# print(bs.prettify())
#
# # ищем по тегу и классу
# temp = bs.find_all('div', 'sun-card__info-item')
# print('find rult', temp)
# # self.sun_act = temp[1].text
# # return temp[1].text