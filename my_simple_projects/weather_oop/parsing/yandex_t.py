
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
url = 'https://yandex.com.am/weather/?lat=55.75581741&lon=37.61764526' # moscow

# проверяем ответ сервера
response = requests.get(url)
print(response)

# получаем исходный код
bs = BeautifulSoup(response.text,"lxml")
# print(bs)

# ищем по тегу и классу
temp = bs.find('span', 'temp__value temp__value_with-unit')
print(temp)
print(temp.text)

