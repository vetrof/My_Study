
import sqlite3

# глобальные переменные
# диапазон меню
MIN_MENU = 1
MAX_MENU = 6

# пункты меню
CREATE = 1
READ = 2
UPDATE = 3
DELETE = 4
SHOW_ALL = 5
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
        elif choise == SHOW_ALL:
            show_all()
        elif choise == EXIT:
            break

    print('end program')

def menu():

    choise = 0

    print('------Menu------')
    print('1 - Create')
    print('2 - Read')
    print('3 - Update')
    print('4 - Delete')
    print('5 - Show All')
    print('6 - Exit')
    print('----------------')

    while choise > MAX_MENU or choise < MIN_MENU:

        try:
            choise = int(input('You choise - '))
        except:
            print('You choise NOT digit, please repeat.')
            continue

        if choise > MAX_MENU or choise < MIN_MENU:
            print('You choise out of range, please choise in range 1 - 5')

    return choise

def create():
    print()
    print('-- Insert row -- ')
    description = input('Description: ')
    price = float(input('Price: '))
    insert_row(description, price)

def insert_row(description, price):
    conn = None
    try:
        conn = sqlite3.connect('inventory.db')
        cur = conn.cursor()

        cur.execute(''' INSERT INTO Inventory (ItemName, Price)
                        VALUES (?, ?) ''',
                        (description, price))
        conn.commit()

    except sqlite3.Error as err:
        print('database error', err)

    finally:
        if conn != None:
            conn.close()
    print('Done')
    print()

def read():
    search = input('search: ')
    show_row(search)

def show_row(search):

    conn = None
    search_result = []

    try:
        conn = sqlite3.connect('inventory.db')
        cur = conn.cursor()
        cur.execute(''' SELECT * FROM Inventory
                        WHERE ItemName == ?''', (search,))
        search_result = cur.fetchall()

        print('i finded', len(search_result), 'intem\n')

        for row in search_result:
            print(row[0], row[1], row[2], '\n')

    except sqlite3.Error as err:
        print('database error', err)
    finally:
        if conn != None:
            conn.close()

def update():

    read()

    id_change = int(input('Input change ID: '))
    description =input('Set description: ')
    price = float(input('Set price: '))

    conn = None

    try:
        conn = sqlite3.connect('inventory.db')
        cur = conn.cursor()
        cur.execute(''' UPDATE Inventory
                        SET ItemName = ?, Price = ? 
                        WHERE ItemID == ? ''',
                        (description, price, id_change))
        conn.commit()
        print('update intem:',cur.rowcount, '\n')

    except sqlite3.Error as err:
        print('database error', err)
    finally:
        if conn != None:
            conn.close()

def delete():

    read()

    id_for_delete = int(input('Input deleted ID: '))

    conn = None

    try:
        conn = sqlite3.connect('inventory.db')
        cur = conn.cursor()
        cur.execute(''' DELETE FROM Inventory
                        WHERE ItemID == ?''',
                        (id_for_delete,))
        conn.commit()
        print('delete intem:',cur.rowcount, '\n')

    except sqlite3.Error as err:
        print('database error', err)
    finally:
        if conn != None:
            conn.close()

def show_all():

    conn = None
    search_result = []

    try:
        conn = sqlite3.connect('inventory.db')
        cur = conn.cursor()
        cur.execute(''' SELECT * FROM Inventory ''')
        search_result = cur.fetchall()

        print('i finded', len(search_result), 'intem\n')

        for row in search_result:
            print(row[0], row[1], row[2])
        print()

    except sqlite3.Error as err:
        print('database error', err)
    finally:
        if conn != None:
            conn.close()

main()