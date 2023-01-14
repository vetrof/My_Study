import sqlite3

def main():
    conn = None
    try:
        # Подсоединиться к базе данных и получить курсор.
        conn = sqlite3.connect('employees.db')
        cur = conn.cursor()

        # Задействовать поддержку внешнего ключа.
        cur.execute('PRAGMA foreign_keys=ON')

        # Вставить новую строку в таблицу Employees.
        cur.execute('''INSERT INTO Employees
                            (Name, Position, DepartmentID, LocationID)
                        VALUES
                            ("Билл Свифт", "Стажер", 99, 1)''')
        conn.commit()
        print('Сотрудник успешно добавлен.')
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