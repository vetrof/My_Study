
import sqlite3

MIN_MENU = 1
MAX_MENU = 8

ORDER = 1
ORDER_DESC = 2
ORDER_NAME = 3
SUMM_ALL = 4
AVERAGE = 5
MAX = 6
MIN = 7
EXIT = 8


def main():

    while True:

        choise = menu()
        print()

        if choise == 1:
            order_population()
        elif choise == 2:
            order_population_desc()
        elif choise == 3:
            order_cities_name()
        elif choise == 4:
            population_summ_all_cities()
        elif choise == 5:
            population_average_all_cities()
        elif choise == 6:
            population_max()
        elif choise == 7:
            population_min()
        elif choise == 8:
            print('Exit')
            break

        flag = input('\nRepeat? Y/N: ')
        if flag == 'n' or flag == 'N':
            print('Exit')
            break


def menu():

    print('\n----- Menu -----')
    print('1 - Poulation order low to hi')
    print('2 - Poulation order hi to low')
    print('3 - Poulation order name cities')
    print('4 - Summ population all cities')
    print('5 - Average population in all cities')
    print('6 - City have maximum population')
    print('7 - City have minimum population')
    print('8 - Exit')
    print()

    while True:

        try:
            choise = int(input('You choise - '))

        except ValueError:
            print('\nYou input not integer')

        else:
            if choise < MIN_MENU or choise > MAX_MENU:
                print('\nYou input out of range 1 - 7')
            else:
                break

    return choise


def order_population():

    conn = sqlite3.connect('cities.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM Cities
                    ORDER BY Population''')
    data = cur.fetchall()
    conn.close()

    for i in data:
        print(f'{i[1]:15} {i[2]:,.0f}')

    conn.close()


def order_population_desc():

    conn = sqlite3.connect('cities.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM Cities
                    ORDER BY Population DESC''')
    data = cur.fetchall()
    conn.close()

    for i in data:
        print(f'{i[1]:15} {i[2]:,.0f}')

    conn.close()


def order_cities_name():

    conn = sqlite3.connect('cities.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM Cities
                    ORDER BY CityName''')
    data = cur.fetchall()
    conn.close()

    for i in data:
        print(f'{i[1]:15} {i[2]:,.0f}')

    conn.close()


def population_summ_all_cities():

    conn = sqlite3.connect('cities.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM Cities
                    ORDER BY Population''')
    data = cur.fetchall()

    for i in data:
        print(f'{i[1]:18} {i[2]:,.0f}')

    cur.execute('''SELECT SUM(Population)
                    FROM Cities''')
    data = cur.fetchone()

    for i in data:
        print('---------------------------')
        print(f'Summ population:  {i:,.0f}')

    conn.close()

    conn.close()


def population_average_all_cities():
    conn = sqlite3.connect('cities.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM Cities
                    ORDER BY Population''')
    data = cur.fetchall()

    for i in data:
        print(f'{i[1]:18} {i[2]:,.0f}')

    cur.execute('''SELECT AVG(Population)
                    FROM Cities''')
    data = cur.fetchone()

    for i in data:
        print('-----------------------------')
        print(f'Average population {i:,.0f}')

    conn.close()


def population_max():

    conn = sqlite3.connect('cities.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM Cities
                    ORDER BY Population''')
    data = cur.fetchall()

    for i in data:
        print(f'{i[1]:18} {i[2]:,.0f}')

    cur.execute('''SELECT MAX(Population)
                    FROM Cities''')
    data = cur.fetchone()

    for i in data:
        print('-----------------------------')
        print(f'Maximum population {i:,.0f}')

    conn.close()


def population_min():

    conn = sqlite3.connect('cities.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM Cities
                    ORDER BY Population''')
    data = cur.fetchall()

    for i in data:
        print(f'{i[1]:18} {i[2]:,.0f}')

    cur.execute('''SELECT MIN(Population)
                    FROM Cities''')
    data = cur.fetchone()

    for i in data:
        print('-----------------------------')
        print(f'Minimum population {i:,.0f}')

    conn.close()


if __name__ == '__main__':
    main()
