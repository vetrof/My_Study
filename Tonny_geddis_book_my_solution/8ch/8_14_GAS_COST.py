#анализ данных цен на бензин в сша за 1993 - 2013 годы
#получить средние значения стоимости по годам
#получить среднее значение цены для каждого месяца
#получить максимальную цену в году
#получить минимальную цену в году
#получить список цен по возрастанию с датами
#получить список цен по возрастанию с датами

def fileTo2dList():
    txt_file = open('data/GasPrices.txt', 'r')
    data_list = []

    for i in range(1,2000):

        line_temp = txt_file.readline()
        if line_temp == '':
            break
        line_temp1 = line_temp.split('-')
        line_temp2 = line_temp1[2].split(':')
        line_temp3 = line_temp1[0] + ' ' + line_temp1[1] + ' ' + line_temp2[0] + ' ' + line_temp2[1]
        line = line_temp3.split()
        data_list.append(line)

    return data_list

def averageCostInYear(data_list, year):
    meausurent_time = 0
    summ = 0

    for i in data_list:
        if int(i[2]) == year:
            summ += float(i[3])
            meausurent_time += 1

    average_year_cost = summ / meausurent_time
    return average_year_cost

def averageCostInMonth(data_list, year, monts):
    measure_time = 0
    summ = 0

    for i in data_list:
        if int(i[2]) == year and int(i[0]) == monts:
            summ += float(i[3])
            measure_time += 1

    if measure_time == 0:
        return 0
    else:
        average_month_cost = summ / measure_time
        return average_month_cost

def maxCostInYear(data_list, year):
    list_cost = []

    for i in data_list:
        if int(i[2]) == year:
            list_cost.append(float(i[3]))
    list_cost.sort()
    return list_cost[-1]

def minCostInYear(data_list, year):
    list_cost = []

    for i in data_list:
        if int(i[2]) == year:
            list_cost.append(float(i[3]))
    list_cost.sort()
    return list_cost[0]

def sortedCostMinToMax(data_list):

    sorted_gas_list = sorted(data_list, key=lambda item: 0 + float(item[3]))
    return sorted_gas_list

def sortedCostMaxToMin(data_list):
    pass

def main():
    year_start = 1993
    year_last = 2013
    #получить из текстового файла двумерный список с данными о дате и ценах
    data_2dlist = fileTo2dList()

    #получить средние значения стоимости по годам
    print('Average cost gas in years: ')
    for i in range(1993, 2014):
        average_year_cost = averageCostInYear(data_2dlist, i)
        print(f'{i} {average_year_cost:.2f}')

    #получить среднее значение цены для каждого месяца
    print()
    print('Average cost gas in monts: ')
    for year in range(1993, 2014):
        print(year, 'year')
        for moths in range(1, 13):
            average_moths = averageCostInMonth(data_2dlist, year, moths)
            print(f'{moths:3} {average_moths:.2f}')

    #получить максимальную цену в году
    print()
    print('Maximum cost in years: ')
    for year in range(1993, 2014):
        max = maxCostInYear(data_2dlist, year)
        print(f'{year} {max}')

    # получить минимальную цену в году
    print()
    print('Minimum cost in years: ')
    for year in range(1993, 2014):
        min = minCostInYear(data_2dlist, year)
        print(f'{year} {min}')

    # получить список цен по возрастанию с датами
    print()
    print('Cost min to max')
    list_sort_min_to_max = sortedCostMinToMax(data_2dlist)
    for i in list_sort_min_to_max:
        print(i)

    # получить список цен по возрастанию с датами
    print()
    print('Cost Max to min')
    list_sort_min_to_max.reverse()
    for i in list_sort_min_to_max:
        print(i)

if __name__ == '__main__':
    main()