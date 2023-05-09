
import sqlite3

def main():

    while True:

        id = input('id - ')
        info = input('info - ')
        cost = input('cost - ')

        insert_to_db(id, info, cost)

        flag = input('repeat? y/n -  ')
        if flag != 'y':
            break


def insert_to_db(id, info, cost):

    conn = None

    try:
        conn = sqlite3.connect('trash_6.db')
        cur = conn.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS test_1
                        (id INTEGER PRIMARY KEY,
                         info TEXT,
                         cost REAL)''')

        cur.execute(''' INSERT INTO test_1 (id, info, cost)
                        VALUES (?, ?, ?)''',
                        (id, info, cost))

        conn.commit()
        print('done')


    except sqlite3.Error as err:
        print(err)

    finally:
        if conn != None:
            conn.close()




if __name__ == '__main__':
    main()






















