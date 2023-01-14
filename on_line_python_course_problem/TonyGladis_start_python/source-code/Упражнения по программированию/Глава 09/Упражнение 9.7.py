# Упражнение по программированию 9.7

# Победители Мировой серии

# Глобальная константа для базового года.
BASE_YEAR = 1903

def main():
    # Локальные словарные переменные.
    year_dict = {}
    count_dict = {}
    
    # Открыть файл для чтения.
    # Файл находится в подпапке data.
    input_file = open(r'data\WorldSeriesWinners.txt', 'r')
    
    # Прочитать все строки из файла в список.
    winners = input_file.readlines()

    # Заполнить словари информацией о командах.
    for i in range(len(winners)):
        team = winners[i].rstrip('\n')

        # Выяснить, в каком году команда стала победителем 
        # (приняв в расчет пропущенные годы).
        year = BASE_YEAR + i
        if year >= 1904:
            year += 1
        if year >= 1994:
            year += 1

        # Добавить информацию в словарь year_dict.
        year_dict[str(year)] = team

        # Обновить словарь count_dict.
        if team in count_dict:
            count_dict[team] += 1
        else:
            count_dict[team] = 1

    # Получить от пользователя входные данные.
    year = input('Введите год в диапазоне 1903-2009: ')

    # Напечатать результаты.
    if year == '1904' or year == '1994':
        print(f'Мировая серия не проводилась в {year} году.')
    elif year<'1903' or year > '2009':
        print(f'Данные за {year} год не включены в базу данных.')
    else:
        winner = year_dict[year]
        wins = count_dict[winner]
        print('Командой, которая стала победителем Мировой серии в ', \
              year, ' году, была ', winner, '.', sep='')
        print('Они побеждали в Мировой серии', wins, 'раз.')

# Вызвать главную функцию.
main()