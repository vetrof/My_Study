 mport sqlite3
 
def main():
    # Подсоединиться к базе данных.
    conn = sqlite3.connect('inventory.db')

    # Получить курсор.
    cur = conn.cursor()

    # Добавить строку в таблицу Inventory.
    cur.execute('''INSERT INTO Inventory (ItemName, Price)
                   VALUES ("Отвертка", 4.99)''')

    # Добавить еще одну строку в таблицу Inventory.
    cur.execute('''INSERT INTO Inventory (ItemName, Price)
                   VALUES ("Молоток", 12.99)''')

    # Добавить еще одну строку в таблицу Inventory.
    cur.execute('''INSERT INTO Inventory (ItemName, Price)
                   VALUES ("Плоскогубцы", 14.99)''')

    # Зафиксировать изменения.
    conn.commit()

    # Закрыть соединение.
    conn.close()

# Вызвать главную функцию.
if __name__ == '__main__':
    main()