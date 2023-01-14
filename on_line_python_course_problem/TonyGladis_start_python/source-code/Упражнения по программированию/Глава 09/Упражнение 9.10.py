# Упражнение по программированию 9.10

# Словарный индекс

# Функция get_word_dict возвращает словарь, содержащий
# слова из списка line_list в качестве ключей и 
# их номера строк в качестве значений.
def get_word_dict(line_list):
    # Создать счетчик строк.
    count = 0
    
    # Создать словарь для слов.
    word_dict = {}

    # Обойти в цикле список строк.
    for e in line_list:
        # Разбить строку на слова.
        words = e.split(' ')

        # Обойти в цикле список слов.
        for w in words:
            # Если слов есть словаре...
            if w in word_dict:
                # Обновить существующий элемент.
                word_dict[w].add(count + 1)
            else:
                # В противном случае сохранить слово в словаре.
                word_dict[w] = set([count + 1])

        # Обновить счетчик.
        count += 1

    # Вернуть словарь.
    return word_dict

# Функция write_index_file записывает индексный файл, 
# содержащий элементы словаря word_dict.
def write_index_file(word_dict):
    # Открыть файл.
	# Файл находится в подпапке data.
    outputfile = open(r'data\index.txt', 'w')

    # Записать элементы словаря.
    for key in word_dict:
        # Записать слово.
        outputfile.write(key + ': ')
        # Записать номера строк.
        for val in word_dict[key]:
            outputfile.write(str(val) + ' ')
        # Записать символ новой строки.
        outputfile.write('\n')

    # Закрыть файл.
    outputfile.close()
    
def main():
    # Открыть файл.
	# Файл находится в подпапке data.
    inputfile = open(r'data\Kennedy.txt', 'r')

    # Прочитать содержимое файла в список.
    line_list = inputfile.readlines()

    # Закрыть файл.
    inputfile.close()

    # Удалить символ новой строки из каждого элемента списка.
    for i in range(len(line_list)):
        line_list[i] = line_list[i].rstrip('\n')

    # Получить словарь, содержащий слова и их номера строк.
    word_dict = get_word_dict(line_list)

    # Записать индексный файл.
    write_index_file(word_dict)
 
# Вызвать главную функцию. 
main()