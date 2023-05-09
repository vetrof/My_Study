import requests

# Загрузим содержимое файла
url = 'https://services.swpc.noaa.gov/text/3-day-forecast.txt'
response = requests.get(url)
data = response.content.decode()

# Преобразуем текстовые данные в таблицу
table = [[cell for cell in line.split()] for line in StringIO(data).readlines()]

# Получим даты из первой строки
dates = table[0][1:]

# Извлечем прогнозы из оставшейся части таблицы
forecast = {}
for line in table[2:]:
    timeslot, *row = line
    forecast_times = [timeslot[:2] + '-' + timeslot[2:] + ' UT']
    forecast_values = [float(value) for value in row]
    forecast.update(dict(zip(forecast_times, forecast_values)))

# Выведем полученные данные
for date in dates:
    print(date)
    for timeslot, value in forecast.items():
        print(timeslot, value)
    print()