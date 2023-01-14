print()
print('счетчики')
print()
print('список комнат')

flat = [
    5.55, 22.19, 7.78, 26.86, 5.55,
    29.84, 22.19, 5.55, 16.85, 4.52
]

# len(flat) подсчитает количество элементов в списке flat
# Сохраним это значение в переменную rooms_n
rooms_num = len(flat)

print('всего комнат ', rooms_num)

room_size = 22.19

count = 0

for room in flat:
    if room == room_size:
        count += 1

print('Комнат площадью', room_size, 'кв.м:', count)

sum_area = 0

for room in flat:
    sum_area = room + sum_area

print(sum_area)

print()
print('Depeche Mode XXI')

# Список годов, в которые Depeche Mode выпускала альбомы
years = [
    1981, 1982, 1983, 1984, 1986, 1987, 1990,
    1993, 1997, 2001, 2005, 2009, 2013, 2017
]

# В этой переменной будем подсчитывать количество альбомов.
# Пока что в ней ничего нет, она равна нулю.
count = 0

for year in years:
    if year > 2000:
        # Каждый раз загибаем по одному пальцу,
        # обнаружив альбом, выпущенный в 21 веке.
        count += 1   # Это то же самое, что count = count + 1

print('Выпущено альбомов в XXI веке:', count)

print()
print()
# Объявите функцию rooms_equal() с параметрами room_size и room_list
def rooms_equal(room_size, room_list):
    count = 0
    for room in room_list:
        if room == room_size:
            count = count + 1
    print('Комнат площадью', room_size, 'кв.м:', count)
flat = [5.55, 22.19, 7.78, 26.86, 5.55, 29.84, 22.19, 5.55, 16.85, 4.52]
hut = [9.2, 3.5, 8.1, 2.3, 9.2, 4.2, 6.9]
rooms_equal(5.55, flat)
# Добавьте ещё один вызов функции rooms_equal()
# Передайте в функцию искомую площадь - 9.2 кв.м и список hut
rooms_equal(9.2, hut)
print()
may_2017 = [24, 26, 15, 10, 15, 19, 10, 1, 4, 7, 7, 7, 12, 14, 17, 8, 9, 19, 21, 22, 11, 15, 19, 23, 15, 21, 16, 13, 25, 17, 19]
may_2018 = [20, 27, 23, 18, 24, 16, 20, 24, 18, 15, 19, 25, 24, 26, 19, 24, 25, 21, 17, 11, 20, 21, 22, 23, 18, 20, 23, 18, 22, 23, 11]
def comfort_count(temperatures):
    count = 0
    for day in temperatures:
        if 22 <= day <= 26:
            count += 1

    print('Количество тёплых дней в этом месяце: ', count)


# Дальше код не меняйте
comfort_count(may_2017)  # Узнаем, что было в мае 2017 г.
comfort_count(may_2018)  # Узнаем, что было в мае 2018 г.
