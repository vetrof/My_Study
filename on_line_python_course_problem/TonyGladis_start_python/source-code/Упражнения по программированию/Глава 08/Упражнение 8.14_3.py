# Упражнение по программированию 8.14_3

# Цены на бензин - наибольшая и наименьшая цены в году

# Функция get_price принимает строковое значение, которое находится
# в формате ММ-ДД-ГГГГ:Цена. Она возвращает компонент с ценой
# в виде вещественного числа.
def get_price(str):
    # Разбить строковое значение по дефисам.
    items = str.split(':')
    # Вернуть цену как вещественное число.
    return float(items[1])

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

# Функция display_highest_per_year выполняет обход списка
# gas_list, показывая самую высокую цену в каждом году.
def display_highest_per_year(gas_list):
    current_year = get_year(gas_list[0])
    highest = get_price(gas_list[0])
    
	# Выполнить обход списка
    for e in gas_list:
        if get_year(e) == current_year:
            if get_price(e) > highest:
                highest = get_price(e)
        else:
            print('Самая высокая цена в ', current_year, ': $',
                  format(highest, '.2f'), sep='')
            current_year = get_year(e)
            highest = get_price(e)

    # Показать самую высокую цену для последнего года.
    print('Самая высокая цена в ', current_year, ': $',
          format(highest, '.2f'), sep='')

# Функция display_lowest_per_year выполняет обход списка 
# gas_list, показывая самую низкую цену в каждом году.
def display_lowest_per_year(gas_list):
    current_year = get_year(gas_list[0])
    lowest = get_price(gas_list[0])

    # Выполнить обход списка.
    for e in gas_list:
        if get_year(e) == current_year:
            if get_price(e) < lowest:
                lowest = get_price(e)
        else:
            print('Самая низкая цена в ', current_year, ': $',
                  format(lowest, '.2f'), sep='')
            current_year = get_year(e)
            lowest = get_price(e)

    # Показать самую низкую цену для последнего года.
    print('Самая низкая цена в ', current_year, ': $',
          format(lowest, '.2f'), sep='')

def main():
    # Открыть файл.
    # Файл находится в подпапке data
    gas_file = open(r'data\GasPrices.txt', 'r')

    # Прочитать содержимое файла в список.
    gas_list = gas_file.readlines()

    # Показать самые высокие цены в году.
    display_highest_per_year(gas_list)

    # Показать самые низкие цены в году.
    display_lowest_per_year(gas_list)

# Вызвать главную функцию
main()