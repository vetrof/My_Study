# Эта программа применяет словарь для хранения
# имен и дней рождения друзей.

# Глобальные константы для пунктов меню
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Главная функция
def main():
    # Создать пустой словарь.
    birthdays = {}

    # Инициализировать переменную для выбора пользователя.
    choice = 0

    while choice != QUIT:
        # Получить выбранный пользователем пункт меню.
        choice = get_menu_choice()

        # Обработать выбранный вариант действий.
        if choice == LOOK_UP:
            look_up(birthdays)
        elif choice == ADD:
            add(birthdays)
        elif choice == CHANGE:
            change(birthdays)
        elif choice == DELETE:
            delete(birthdays)
            
# Функция get_menu_choice выводит меню и получает 
# проверенный на допустимость выбранный пользователем пункт.
def get_menu_choice():
    print()
    print('Друзья и их дни рождения')
    print('------------------------')
    print('1. Найти день рождения')
    print('2. Добавить новый день рождения')
    print('3. Изменить день рождения')
    print('4. Удалить день рождения')
    print('5. Выйти из программы')
    print()

    # Получить выбранный пользователем пункт.
    choice = int(input('Введите выбранный пункт: '))

    # Проверить выбранный пункт на допустимость.
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Введите выбранный пункт: '))

    # Вернуть выбранный пользователем пункт.
    return choice

# Фукнция look_up отыскивает имя
# в словаре birthdays.
def look_up(birthdays):
    # Получить искомое имя.
    name = input('Введите имя: ')

    # Отыскать его в словаре.
    print(birthdays.get(name, 'Не найдено.'))

# Функция add добавляет новую запись
# в словарь birthdays.
def add(birthdays):
    # Получить имя и день рождения.
    name = input('Введите имя: ')
    bday = input('Введите день рождения: ')

    # Если имя не существует, то его добавить.
    if name not in birthdays:
        birthdays[name] = bday
    else:
        print('Эта запись уже существует.')

# Функция change изменяет существующую
# запись в словаре birthdays.
def change(birthdays):
    # Получить искомое имя.
    name = input('Введите имя: ')

    if name in birthdays:
        # Получить новый день рождения.
        bday = input('Введите новый день рождения: ')

        # Обновить запись.
        birthdays[name] = bday
    else:
        print('Это имя не найдено.')

# Функция delete удаляет запись из
# словаря birthdays.
def delete(birthdays):
    # Получить искомое имя.
    name = input('Введите имя: ')

    # Если имя найдено, то удалить эту запись.
    if name in birthdays:
        del birthdays[name]
    else:
        print('Это имя не найдено.')

# Вызвать главную функцию.
if __name__ == '__main__':
    main()