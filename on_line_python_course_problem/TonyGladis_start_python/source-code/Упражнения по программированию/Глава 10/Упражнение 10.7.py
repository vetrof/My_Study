# Упражнение по программированию 10.7

# Система управления персоналом

# import emp
from objects import emp  # класс хранится в папке objects 
import pickle

# Глобальные константы для пунктов меню.
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Глобальная константа для имени файла.
# Файл находится в подпапке data.
FILENAME = r'data\employees.dat'

# Главная функция
def main():

    # Получить словарь сотрудников.
    employees = load_employees()

    # Инициализировать переменную для выбора пользователя.
    choice = 0

    # Обрабатывать запросы пользователя до тех пор,
    # пока пользователь не выйдет из программы.
    while choice != QUIT:

        choice = get_user_choice()

        if choice== LOOK_UP:
            look_up(employees)
        elif choice == ADD:
            add(employees)
        elif choice == CHANGE:
            change(employees)
        elif choice == DELETE:
            delete(employees)

    # Законсервировать результирующий словарь.
    save_employees(employees)
    
def load_employees():
    try:
        # Открыть файл.
        input_file = open(FILENAME, 'rb')

        # Расконсервировать словарь.
        employee_dict = pickle.load(input_file)

        # Закрыть файл.
        input_file.close()
    except IOError:
        # Не получилось открыть файл.
        # Создать пустой словарь.
        employee_dict = {}

    return employee_dict

def get_user_choice():
    # Показать меню, получить выбор пользователя и
	# проверить его допустимость.
    print()
    print('Меню')
    print('-------------------------------------')
    print('1. Найти сотрудника')
    print('2. Добавить нового сотрудника')
    print('3. Изменить существующего сотрудника')
    print('4. Удалить сотрудника')
    print('5. Выйти из программы')
    print()

    choice = int(input('Введите выбранный пункт меню: '))

    # Проерить выбор.
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Выбранный Вами пункт меню недопустимый.' \
                           ' Пожалуйста, введите пункт меню: '))

    # Вернуть выбор пользователя.
    return choice

def look_up(employees):
    # Получить идентификационный номер сотрудника для поиска.
    ID = input('Введите идентификационный номер сотрудника: ')

    # Отыскать идентификатор в словаре. Если найден, то
    # данные будут распечатаны с помощью метода employee __str__;
    # в противном случае распечатать указанное сообщение.
    print(employees.get(ID, "Указанный идентификатор не найден"))

def add(employees):
    # Получить информацию о сотруднике.
    name = input('Введите имя сотрудника: ')
    ID = input('Введите идентификатор сотрудника: ')
    department = input('Введите отдел сотрудника: ')
    title = input('Введите должность сотрудника: ')

    new_emp = emp.Employee(name, ID, department, title)

    # Добавить нового сотрудника, если идентификатор не существует.
    # В противном случае уведомить пользователя, что 
	# идентификатор существует.
    if ID not in employees:
        employees[ID] = new_emp
        print('Новый сотрудник был добавлен.')
    else:
        print('Сотрудник с этим идентификатором уже существует.')

def change(employees):
    # Получить обновленную информацию о сотруднике.
    ID = input('Введите идентификатор сотрудника: ')

    # Изменить информацию о сотруднике, если идентификатор существует.
    # В противном случае уведомить пользователя, что идентификатор
	# не существует.
    if ID in employees:
        name = input('Введите новое имя: ')
        department = input('Введите новый отдел: ')
        title = input('Введите новую должность: ')

        new_emp = emp.Employee(name, ID, department, title)

        employees[ID] = new_emp
        print('Информация о сотруднике обновлена.')
    # Идентификатор не найден.
    else: 
        print('Указанный идентификатор не найден.')

def delete(employees):
    # Получить обновленную информацию о сотруднике.
    ID = input('Введите идентификатор сотрудника: ')

    # Изменить информацию о сотруднике, если идентификатор существует.
    # В противном случае уведомить пользователя, что идентификатор
	# не существует.
    if ID in employees:
        del employees[ID]
        print('Информация о сотруднике удалена.')
    # Идентификатор не найден.
    else: 
        print('Указанный идентификатор не найден.')

# Функция консервирует указанный словарь и
# сохраняет его в файле с данными о сотрудниках.
def save_employees(employees):
    # Открыть файл для записи.
    output_file = open(FILENAME, 'wb')

    # Законсервировать словарь и сохранить его.
    pickle.dump(employees, output_file)

    # Закрыть файл.
    output_file.close()

# Вызвать главную функцию.
if __name__ == '__main__':
    main()
