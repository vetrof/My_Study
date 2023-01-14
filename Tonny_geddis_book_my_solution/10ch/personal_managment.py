from objects import eployee #импортируем файл с классом из папки
import pickle

# имя файла для консервации
FILENAME = 'data_emloyee.dat'

# глобальные константы для меню
FIND = 1
ADD = 2
EDIT = 3
DELETE = 4
EXIT = 5

def main():
    # load contacts from dat file and unpickle him
    contacts_dict = load_contacts()

    # view user menu and return user choise
    choise = user_choise()

    # run funcions after user choise
    if choise == FIND:
        find(contacts_dict)
    elif choise == ADD:
        add(contacts_dict)
    # elif choise == EDIT:
    #     edit(employee_data)
    # elif choise == DELETE:
    #     delete(employee_data)

    # save and pickle contacts
    # save_file(contacts)





# загружаем файл и из него расконсервируем список
# возвращаем contacts_dict
def load_contacts():
    try:
        # open dat file
        file = open(FILENAME, 'rb')

        # unpickle opened file
        contacts_dict = pickle.load(file)

        # close dat file
        file.close()

    except IOError:
        # if file not open - create empty dictonary
        contacts_dict = {}

    # return dictonary
    return contacts_dict

# wiev menu and return user choise
def user_choise():
    # user menu select
    print('-------menu------')
    print('1. find employee')
    print('2. add employee')
    print('3. edit info employee')
    print('4. delete employee')
    print('5. exit')

    # user input
    user_select = int(input('> - '))

    return user_select

# find data in dictonary
def find(mycontacts):
    # Получить искомое имя.
    id = input('Введите id: ')

    # Отыскать его в словаре.
    print(mycontacts.get(id, 'Это имя не найдено.'))








# ask name and other data and add to dictonary
def add(employee_data):
    name = input('enter name-')
    id = input('enter ID-')
    dept = input('enter dept-')
    job = input('enter job-')

    # create obj in Employee Class
    info = eployee.Employee(name, id, dept, job)

    # Если имя в словаре не существует, то
    # добавить его в качестве ключа со связанным с ним
    # значением в виде объекта.
    if name not in employee_data:
        employee_data[name] = info
        print('Запись добавлена.')
    else:
        print('Это имя уже существует.')















def edit():
    pass


def delete():
    pass


def save_file():
    pass


if __name__ == '__main__':
    main()
