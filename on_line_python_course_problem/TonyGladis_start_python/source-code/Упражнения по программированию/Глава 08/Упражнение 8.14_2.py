# Упражнение по программированию 8.14_2

# Цены на бензин - средняя цена за месяц

# Функция get_price принимает строковое значение, которое находится
# в формате ММ-ДД-ГГГГ:Цена. Она возвращает компонент с ценой
# в виде вещественного числа.
def get_price(str):
    # Разбить строковое значение по дефисам.
    items = str.split(':')
    # Вернуть цену как вещественное число.
    return float(items[1])

# Функция get_month принимает строковое значение, которое находится
# в формате ММ-ДД-ГГГГ:Цена. Она возвращает компонент ММ
# в виде целого числа.
def get_month(str):
    # Разбить строковое значение по дефисам.
    items = str.split('-')
    # Вернуть месяц как целое число.
    return int(items[0])

# Функция get_year принимает строковое значение, которое находится
# в формате ММ-ДД-ГГГГ:Цена. Она возвращает компонент ГГГГ
# в виде целого числа.
def get_year(str):
    # Разбить строковое значение по двоеточию.
    items = str.split(':')
    # Разбить строковое значение по дефисам.
    date_items = items[0].split('-')
    # Вернуть год как целое число.
    return int(date_items[2])

# Функция display_monthly_averages выполняет обход списка gas_list,
# вычисляя и показывая среднемесячную цену.
def display_monthly_averages(gas_list):
    month_names = ['январь', 'февраль', 'март', 'апрель', 'май',
                   'июнь', 'июль', 'август', 'сентябрь', 'октябрь',
                   'ноябрь', 'декабрь']
    current_month = get_month(gas_list[0])
    current_year = get_year(gas_list[0])
    total = 0
    count = 0
    average = 0

    # Выполнить обход списка.
    for e in gas_list:
        if (get_month(e) == current_month) and (get_year(e) == current_year):
            total += get_price(e)
            count += 1
        else:
            average = total / count
            print('Средняя цена за ', month_names[current_month-1],
                  ', ', current_year, ': $',
                  format(average, '.2f'), sep='')
            current_month = get_month(e)
            current_year = get_year(e)
            total = 0
            count = 0

    # Показать среднее значение за последний месяц.
    print('Средняя цена за ', month_names[current_month-1],
          ', ', current_year, ': $',
          format(average, '.2f'), sep='')

def main():
    # Открыть файл.
    # Файл находится в подпапке data
    gas_file = open(r'data\GasPrices.txt', 'r')

    # Прочитать содержимое файла в список.
    gas_list = gas_file.readlines()

    # Показать среднемесячные цены.
    display_monthly_averages(gas_list)

# Вызвать главную функцию
main()