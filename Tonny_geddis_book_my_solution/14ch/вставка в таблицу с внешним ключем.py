
import sqlite3

def main():


    conn = None
    try:
        conn = sqlite3.connect('employees_en.db')
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''INSERT INTO Employees 
                            (Name, Position, DepartmentID, LocationID)
                        VALUES
                            ("Хомяк Ежоф", "Директор", 70, 8)''')
        conn.commit()
        print('done')
    except sqlite3.Error as err:
        print('db err: ', err)
    finally:
        if conn != None:
            conn.close()
    read()

def read():
    con = sqlite3.connect('employees.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM Employees')
    data = cur.fetchall()

    for row in data:
        print(row[0],row[1],row[2],row[3],row[4])


if __name__ == '__main__':
    main()