import sqlite3

def main():
    conn = None
    try:
        # Подсоединиться к базе данных и получить курсор.
        conn = sqlite3.connect('employees.db')
        cur = conn.cursor()

        # Задействовать поддержку внешнего ключа.
        cur.execute('PRAGMA foreign_keys=ON')

        # Извлечь имена сотрудников, отделы и города.
        cur.execute(
            '''SELECT
                   Employees.Name,
                   Departments.DepartmentName,
                   Locations.LocationName
                FROM
                   Employees, Departments, Locations
                WHERE
                   Employees.DepartmentID == Departments.DepartmentID AND
                   Employees.LocationID == Locations.LocationID''')
        results = cur.fetchall()
        for row in results:
            print(f'{row[0]:15} {row[1]:25} {row[2]}')
    except sqlite3.Error as err:
        # Если произошло исключение, то напечатать сообщение об ошибке.
        print(err)
    finally:
        # Если соединение открыто, то закрыть его.
        if conn != None:
            conn.close()

# Вызвать главную функцию.
if __name__ == '__main__':
    main()