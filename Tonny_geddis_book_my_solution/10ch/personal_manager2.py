# програма - упражнение по ООП, менеджер персонала.
# программа умеет читать файл с диска, расконсервировать
# словарь который содержит обьекты класса Emploee
# такще ищем запись по id, добавляем, удаляем и записываем заново.

import pickle
import time
from objects import eployee

# глобальные переменные
# для удобства чтения присваиваем командам меню цифры
FIND = 1
ADD = 2
CHANGE = 3
DELETE = 4
ALL = 5
QUIT = 6


# файл для консервации
FILE = r'employees.dat'

def main():

    # открываем dat файл, и расконсервируем словарь в переменную
    dictonary = open_file()

    menu_choise = 0

    # вызываем меню по кругу пока пользователь не выеберет QUIT
    while menu_choise != QUIT:

        # вызываем функцию меню
        menu_choise = menu()

        # в зависимости от выбранного пункта меню запускаем функции
        if menu_choise == FIND:
            find(dictonary)
        elif menu_choise == ADD:
            add(dictonary)
        elif menu_choise == CHANGE:
            change(dictonary)
        elif menu_choise == DELETE:
            delete(dictonary)
        elif menu_choise == ALL:
            all(dictonary)

    # сохраняем данные словаря в файл
    save(dictonary)

    print('Программа завершена')

# открываем файл, расконсервируем данные
def open_file():
    # открывайм dat файл
    file = open(FILE, 'rb')

    #расконсервируем словарь из файла
    dictonary = pickle.load(file)

    # закрываем файл
    file.close()

    # возвращаем словарь
    return dictonary

# показываем меню, юзер выбирает пункт, возвращаем выбор
def menu():

    print('--------меню--------')
    print('1. Поиск по ID')
    print('2. Добавить сотрудника')
    print('3. Изменить данные сотрудника')
    print('4. Удалить сотрудника')
    print('5. Все записи')
    print('6. Выход')
    print('--------------------')
    choise = int(input('Ваш выбор> '))

    # Проверяем выбор юзера, если выбран не существующий пункт, просим повторить.

    while choise < 1 or choise > 6:
        print('Выбран не существующий пункт меню.')
        choise = int(input('Выберите верный пенкт меню: '))

    return choise

# функция поиска по ID в словаре
def find(dictonary):
    id = input('введите искомый ID - ')
    print()
    print(dictonary.get(id, 'id не найден'))
    print()
    time.sleep(2)

# функция добавляет новую запись в словарь
def add(dictonary):

    # принимаем у пользователя данные работника
    print('------Добавляем нового сотрудника-------')
    name = input('имя- ')
    id = input('id- ')
    dept = input('отдел- ')
    job = input('должность- ')

    # создаем обьект каласса Employee с аргументами
    new_info = eployee.Employee(name, id, dept, job)

    # добавляем в словарь созданый обьект в качетве значения ключа id
    dictonary[id] = new_info
    print('Запись добавлена!')
    print()
    time.sleep(2)

# функция изменения записи работника
def change(dictonary):

    # просим у пользователя ID и другую информацию для изменения
    id_for_change = input('введите id записи для изменения')
    name = input('имя- ')
    dept = input('отдел- ')
    job = input('должность- ')

    # создаем новый обьект класса Employee с новыми атрибутами
    replace_info = eployee.Employee(name, id_for_change, dept, job)

    # заменяем запись в словаре с данным ID
    dictonary[id_for_change] = replace_info

    print('Запись изменена.')

    print()
    time.sleep(2)

# функция удаляет запись из словаря
def delete(dictonary):

    # просим id записи для удаления
    id_for_delete = input('введите id для удаления записи - ')

    # удаляем запись из словаря по ID которое является ключем
    dictonary.pop(id_for_delete, 'eror delete')
    print('Запись удалена.')
    print()
    time.sleep(2)

# функция которая выводит на экран все записи
def all(dictonary):
    print('Записи отсортированы по возрастанию номера ID:')

    # создаем список для ключей словаря
    key_list = []

    # цикл который перемещает ключи из словаря в список
    for i in dictonary:
        key_list.append(i)

    # сортируем ключи в списке
    key_list.sort()


    # создаем цикл перебора по отсортированному списку ключей
    # и печатаем все записи с помощью метода класса __str__
    for i in key_list:
        print('--------------')
        print(dictonary.get(i, 'error'))
    print()
    time.sleep(2)

# функция консервации и сохранения в dat файл
def save(dictonary):

    # открываем файл для записи
    dat_file = open(FILE, 'wb')

    # консервируем и добавляем в dat файл
    pickle.dump(dictonary, dat_file)

    # закрываем файл
    dat_file.close()

if __name__ == '__main__':
    main()