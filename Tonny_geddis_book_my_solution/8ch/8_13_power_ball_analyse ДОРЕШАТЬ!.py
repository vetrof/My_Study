#анализируем данные лотореи суперболл из текстового файла data/pbnumbers.txt

def fileToList():
    # преобразуем цифры в файле в список
    txt_file = open('data/pbnumbers.txt', 'r')              # создаем файловый обьект
    list_number = []                                        # создаем пустой список
    while True:                                             # создаем бесконечный цикл
        line = txt_file.readline()                          # читаем первуюстроку
        if line == '':                                      # если сторока пустая
            break                                           # то выходим из цикла
        for i in line.split():                              # режем строку и пробегаемся цифрам циклом
            list_number.append(int(i))                      # интуем строки и добавляем числа в список
    return list_number

def mostTimeDigit(list_digit):
# создаем списки для удобной работы по анализу
# count_list = список в котором индекс является числом а значение - частотой выпадения числа
# count_list_sort = список в котором частота отсортирована от малой до большой
    count_list = [0] * 70                               #создаем пустой список
    for number in range(1, 70):                         #создаем цикл  от 1 до 69
        for i in list_digit:                           #проверяем цифры из цикла в списке
            if number == i:                             #если есть совпадения
                count_list[number] += 1                 #то пишем эту цифру в такойже индекс а значения плюсуем
                                                        #по сути индексы являются числами, а значения частотой
    count_list_sort = count_list.copy()                 #копируем список в новый
    count_list_sort.sort()                              #новый список сортируем по частоте
    return count_list

def most_common(freq_list):
    # Функция most_common принимает частотный список freq_list и возвращает
    # другой список, в котором элемент 0 содержит позицию самого большого
    # значения в списке freq_list, элемент 1 содержит позицию второго
    # самого большого значения в списке freq_list, и т.д.

    # Создать пустой список для позиций самых распространенных значений.
    common_sorted = []

    # Сделать копию списка freq_list.
    temp_list = []
    for item in freq_list:
        temp_list.append(item)

    for i in range(len(temp_list)):
        position = position_of_highest_value(temp_list)
        common_sorted.append(position)
        temp_list[position] = -1

    # Вернуть список common_sorted.
    return common_sorted

def position_of_highest_value(num_list):
    # Функция position_of_highest_value возвращает позицию
    # самого большого значения в списке num_list.
    highest = 0
    highest_position = 0
    for i in range(len(num_list)):
        if num_list[i] > highest:
            highest = num_list[i]
            highest_position = i
    return highest_position

def main():

    list_number = fileToList()
    freq_digit = mostTimeDigit(list_number)
    sort_freq_digit = most_common(freq_digit)

























if __name__ == '__main__':
    main()