import sqlite3

MIN_MENU = 1
MAX_MENU = 6
CREATE = 1
READ = 2
UPDATE = 3
DELETE = 4
ALL = 5
EXIT = 6


def main():

    while True:

        choise = menu()
        if choise == CREATE:
            create()
        elif choise == READ:
            read()
        elif choise == UPDATE:
            update()
        elif choise == DELETE:
            delete()
        elif choise == ALL:
            printall()
        else:
            print('Program end')
            break


def menu():

    print()
    print('* CRUD Menu *')
    print('1 - Create')
    print('2 - Read')
    print('3 - Update')
    print('4 - Delete')
    print('5 - Show All')
    print('6 - Exit')

    while True:

        choise = input('\nYou choise - ')

        try:
            choise = int(choise)
        except ValueError:
            print('Input not digit')
            continue
        if choise < MIN_MENU or choise > MAX_MENU:
            print('Input out of range')
            continue
        else:
            break
    return choise


def create():

    name = input('Name: ')

    while True:
        try:
            number = int(input('Number: '))

        except ValueError:
            print('error input number')
            continue
        else:
            break

    conn = None

    try:
        conn = sqlite3.connect('phonebook.db')
        cur = conn.cursor()
        cur.execute('''INSERT INTO Etries (Name, Phone)
                        VALUES (?, ?)''', (name, number))

    except sqlite3.Error as err:
        print('Dtabase error', err)

    conn.commit()
    conn.close()
    print('Done!')


def read():

    search = input('Input search name: ')

    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM Etries
                    WHERE Name LIKE ? ''', ('%' + search + '%',))
    data = cur.fetchall()

    print('\n i found', len(data), 'name')
    for i in data:
        print(f'{i[0]} {i[1]} {i[2]}')


def update():

    print()
    printall()

    id = input('\nchoise ID for update: ')
    name = input('Enter name: ')

    while True:

        try:
            phone = int(input('Enter numper phone: '))
        except:
            print('error input number')
            continue
        else:
            break

    conn = None

    try:
        conn = sqlite3.connect('phonebook.db')
        cur = conn.cursor()
        cur.execute("""UPDATE Etries 
                        SET Name = ?, Phone = ?
                        WHERE RowID = ?
                        """, (name, phone, id))

    except sqlite3.Error as err:
        print('Dtabase error', err)

    conn.commit()
    conn.close()
    print('Done!')


def delete():

    print()
    printall()

    id_del = input('\nEnter ID for delete: ')

    conn = None

    try:
        conn = sqlite3.connect('phonebook.db')
        cur = conn.cursor()
        cur.execute("""DELETE FROM Etries 
                        WHERE RowID == ?""",(id_del,))

    except sqlite3.Error as err:
        print('Dtabase error', err)

    conn.commit()
    conn.close()
    print('Done!')


def printall():

    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM Etries''')
    data = cur.fetchall()

    print()
    for i in data:
        print(f'{i[0]:2} {i[1]:12} {i[2]}')

    conn.close()


if __name__ == '__main__':
    main()
