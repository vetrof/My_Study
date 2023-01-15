import sqlite3

def main():
    # Подсоединиться к базе данных.
    conn = sqlite3.connect('inventory2.db')

    # Получить курсор.
    cur = conn.cursor()

    # Добавить таблицу Inventor
    cur.execute('''CREATE TABLE Inventory (айдиди INTEGER PRIMARY KEY NOT NULL,
                                           звать TEXT,
                                           стоить REAL)''')

    # Зафиксировать изменения.
    conn.commit()

    # Закрыть соединение.
    conn.close()

# Вызвать главную функцию.
if __name__ == '__main__':
    main()