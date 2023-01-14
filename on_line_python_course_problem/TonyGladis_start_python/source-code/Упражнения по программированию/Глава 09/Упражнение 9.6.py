# Упражнение по программированию 9.6

# Анализ файла

def main():
    # Получить входной текст первого файла и создать множество, 
    # содержащее его уникальные слова
    input_name = input('Введите имя первого входного файла: ')
    # Файл находится в подпапке data
    file1 = open('data\\' + input_name, 'r')
    text1 = file1.read()
    file1.close()
    words1 = text1.split()
    set1 = set(words1)

    # Получить входной текст второго файла и создать множество, 
    # содержащее его уникальные слова
    input_name = input('Введите имя второго входного файла: ')
    # Файл находится в подпапке data
    file2 = open('data\\' + input_name, 'r')
    text2 = file2.read()
    file2.close()
    words2 = text2.split()
    set2 = set(words2)

    # Получить объединение множеств и напечатать его значения.
    union = set1.union(set2)
    print('Эти уникальные слова теперь содержатся в обоих файлах:')
    for item in union:
        print(item)
    print()

    # Получить пересечение множеств и напечатать его значения
    intersection = set1.intersection(set2)
    print('Эти слова встречаются в обоих файлах:')
    for item in intersection:
        print(item)
    print()

    # Получить разность между множеством set1 и множеством set2 и
    # напечатать его значения 
    difference1 = set1.difference(set2)
    print('Эти слова встречаются в первом файле и ' \
          'не встречаются во втором файле:')
    for item in difference1:
        print(item)
    print()

    # Получить разность между множеством set2 и множеством set1 и
    # напечатать его значения 
    difference2 = set2.difference(set1)
    print('Эти слова встречаются во втором файле и ' \
          'не встречаются во первом файле:')
    for item in difference2:
        print(item)
    print()

    # Получить симметрическую разность между множеством set1 и 
    # множеством set2 и напечатать его значения 
    sym_diff = set1.symmetric_difference(set2)
    print('Эти слова встречаются в первом файле или ' \
          'втором файле и не встречаются в ' \
          'обоих файлах:')
    for item in sym_diff:
        print(item)
    print()

# Вызвать главную функцию.
main()