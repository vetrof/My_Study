# Эта программа позволяет пользователю изменять количество
# в записи файла coffee.txt.

import os # Это модуль нужен для функций remove и rename

def main():
    # Создать булеву переменную для использования ее в качестве флага.
    found = False

    # Получить искомое значение и новое количество.
    search = input('Введите искомое описание: ')
    new_qty = int(input('Введите новое количество: '))

    # Открыть исходный файл coffee.txt.
    coffee_file = open('coffee.txt', 'r')

    # Открыть временный файл.
    temp_file = open('temp.txt', 'w')

    # Прочитать поле с описанием первой записи.
    descr = coffee_file.readline()

    # Прочитать остаток файла.
    while descr != '':
        # Прочитать поле с количеством.
        qty = float(coffee_file.readline())

        # Удалить \n из описания.
        descr = descr.rstrip('\n')

        # Записать во временный файл либо эту запись,
        # либо новую запись, если эта запись 
        # подлежит изменению.
        if descr == search:
            # Записать измененную запись во временный файл.
            temp_file.write(f'{descr}\n')
            temp_file.write(f'{new_qty}\n')

            # Назначить флагу found значение True.
            found = True
        else:
            # Записать изначальну запись во временный файл.
            temp_file.write(f'{descr}\n')
            temp_file.write(f'{qty}\n')

        # Прочитать следующее описание.
        descr = coffee_file.readline()

    # Закрыть файл с данными о кофе и временный файл.
    coffee_file.close()
    temp_file.close()

    # Удалить исходный файл coffee.txt.
    os.remove('coffee.txt')

    # Переименовать временный файл.
    os.rename('temp.txt', 'coffee.txt')

    # Если искомое значение в файле не найдено,
    # то показать сообщение.
    if found:
        print('Файл обновлен.')
    else:
        print('Это значение в файле не найдено.')

# Вызвать главную функцию.
if __name__ == '__main__':
    main()