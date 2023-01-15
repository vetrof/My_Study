import sqlite3

def main():
    # Подсоединиться к базе данных.
    conn = sqlite3.connect('company.db')

    # Получить курсор.
    cur = conn.cursor()

    # Добавить таблицу Customers.
    cur.execute('''CREATE TABLE IF NOT EXISTS Customers (CustomerID INTEGER PRIMARY KEY NOT NULL,
                                           Name TEXT,
                                           Email TEXT)''')

    # Добавить таблицу Employees.
    cur.execute('''CREATE TABLE IF NOT EXISTS Employees (EmployeeID INTEGER PRIMARY KEY NOT NULL,
                                           Name TEXT,
                                           Position TEXT)''')

    # Зафиксировать изменения.
    conn.commit()

    # Закрыть соединение.
    conn.close()

# Вызвать главную функцию.
if __name__ == '__main__':
    main()