# Упражнение по программированию 4.5

# Средняя толщина дождевых осадков

# Объявить переменные для суммарной толщины дождевых осадков,
# ежемесячной толщины дождевых осадков, среднемесячной толщины дождевых осадков,
# количества лет и общего количества месяцев.
totalRainfall = 0.0
monthRainfall = 0.0
averageRainfall = 0.0
years = 0
totalMonths = 0

# Получить количество лет
years = int(input('Введите количество лет: '))

# Получить толщину дождевых осадков помесячно
for year in range(years):
    print ('Для года ', year + 1, ':')
    for month in range(12):
        monthRainfall = float(input( \
        'Введите толщину дождевых осадков для месяца: '))
        # Прибавить к общему количеству месяцев
        totalMonths += 1
        # Прибавить к общему количеству дождевых осадков
        totalRainfall += monthRainfall
			
# Вычислить среднюю толщину дождевых осадков
averageRainfall = totalRainfall / totalMonths

print('Для ', totalMonths, 'месяцев')
print('Суммарная толщина дождевых осадков: ', format(totalRainfall, '.2f'), 'см')
print('Среднемесячная толщина дождевых осадков: ', \
      format(averageRainfall, '.2f'), 'см')