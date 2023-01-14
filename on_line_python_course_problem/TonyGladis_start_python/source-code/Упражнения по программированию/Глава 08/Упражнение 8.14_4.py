# Упражнение по программированию 8.14_4

# Цены на бензин - список цен, упорядоченный по возрастанию

# Функция get_price принимает строковое значение, которое находится
# в формате ММ-ДД-ГГГГ:Цена. Она возвращает компонент с ценой
# в виде вещественного числа.
def get_price(str):
    # Разбить строковое значение по дефисам.
    items = str.split(':')
    # Вернуть цену как вещественное число.
    return float(items[1])

# Функция get_date принимает строковое значение, которое находится
# в формате ММ-ДД-ГГГГ:Цена. Она возвращает компонент ММ-ДД-ГГГГ
# в виде строкового значения.	
def get_date(str):
    # Разбить строковое значение по двоеточию.
    items = str.split(':')
    # Разбить строковое значение по дефисам.
    return str(items[0])

# Функция lowest_element_position возвращает позицию
# элемента в списке g_list с самым низким значением.
def lowest_element_position(g_list):
    lowest = get_price(g_list[0])
    position = 0
    for i in range(1, len(g_list)):
        if get_price(g_list[i]) < lowest:
            lowest = get_price(g_list[i])
            position = i

    # Вернуть позицию самого низкого значения.
    return position

# Функция create_low_to_high_file создает файл с именем
# low_to_high.txt, содержащий элементы списка gas_list,
# отсортированные в порядке возрастания цены.
def create_low_to_high_file(gas_list):
    # Сделать копию списка gas_list.
    temp_list = []
    for e in gas_list:
        temp_list.append(e)
    
    # Открыть файл для записи.
    # Файл будет находиться в подпапке data.
    outputfile = open(r'data\low_to_high.txt', 'w')

    while (len(temp_list) > 0):
        # Получить индекс элемента с самой низкой ценой.
        lowest_index = lowest_element_position(temp_list)

        # Получить этот элемент.
        lowest_line = temp_list[lowest_index]

        # Записать этот элемент в файл.
        outputfile.write(lowest_line)

        # Удалить этот элемент из списка.
        del temp_list[lowest_index]

    # Закрыть файл.
    outputfile.close()

def main():
    # Открыть файл.
    # Файл находится в подпапке data
    gas_file = open(r'data\GasPrices.txt', 'r')

    # Прочитать содержимое файла в список.
    gas_list = gas_file.readlines()

    # Создать файл с элементами, отсортированными
    # по цене в порядке возрастания.
    create_low_to_high_file(gas_list)

# Вызвать главную функцию
main()