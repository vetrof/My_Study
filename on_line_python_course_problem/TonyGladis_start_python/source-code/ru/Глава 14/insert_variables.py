import sqlite3

def main():
    # Переменная управления циклом.
    again = 'д'

    # Подсоединиться к базе данных.
    conn = sqlite3.connect('inventory.db')

    # Получить курсор.
    cur = conn.cursor()

    while again == 'д':
        # Получить название и цену позиции.
        item_name = input('Название: ')
        price = float(input('Цена: '))

        # Добавить позицию в таблицу Inventory.
        cur.execute('''INSERT INTO Inventory (ItemName, Price)
                       VALUES (?, ?)''',
                       (item_name, price))

        # Добавить еще?
        again = input('Добавить еще одну позицию? (д/н): ')

    # Зафиксировать изменения.
    conn.commit()

    # Закрыть соединение.
    conn.close()

# Вызвать главную функцию.
if __name__ == '__main__':
    main()