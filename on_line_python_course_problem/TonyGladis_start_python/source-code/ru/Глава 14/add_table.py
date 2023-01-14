import sqlite3

def main():
    # Подсоединиться к базе данных.
    conn = sqlite3.connect('inventory.db')

    # Получить курсор.
    cur = conn.cursor()

    # Добавить таблицу Inventory.
    cur.execute('''CREATE TABLE Inventory (ItemID INTEGER PRIMARY KEY NOT NULL,
                                           ItemName TEXT,
                                           Price REAL)''')

    # Зафиксировать изменения.
    conn.commit()

    # Закрыть соединение.
    conn.close()

# Вызвать главную функцию.
if __name__ == '__main__':
    main()