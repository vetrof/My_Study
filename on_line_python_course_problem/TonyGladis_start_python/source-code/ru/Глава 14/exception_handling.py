import sqlite3

def main():
    # Переменная управления циклом.
    again = 'д'

    while (again == 'д'):
        # Получить ID товара, название и цену.
        item_id = int(input('ID товара: '))
        item_name = input('Название товара: ')
        price = float(input('Цена: '))

        # Добавить товар в базу данных.
        add_item(item_id, item_name, price)

        # Добавить еще одну?
        again = input('Добавить еще одну позицию? (д/н): ')

# Функция add_item добавляет позицию в базу данных.
def add_item(item_id, name, price):
    # Инициализировать переменную соединения.
    conn = None

    try:
        # Подсоединиться к базе данных.
        conn = sqlite3.connect('inventory.db')

        # Получить курсор.
        cur = conn.cursor()

        # Добавить позицию в таблицу Inventory.
        cur.execute('''INSERT INTO Inventory (ItemID, ItemName, Price)
                       VALUES (?, ?, ?)''',
                    (item_id, name, price))

        # Зафиксировать изменения.
        conn.commit()

    except sqlite3.Error as err:
        print(err)

    finally:
        # Закрыть соединение.
        if conn != None:
            conn.close()

# Вызвать главную функцию.
if __name__ == '__main__':
    main()