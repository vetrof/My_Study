import sqlite3

def main():
    # Подсоединиться к базе данных.
    conn = sqlite3.connect('chocolate.db')

    # Получить курсор.
    cur = conn.cursor()

    # Получить самую низкую цену цену.
    cur.execute('SELECT MIN(RetailPrice) FROM Products')
    lowest = cur.fetchone()[0]

    # Получить самую высокую цену.
    cur.execute('SELECT MAX(RetailPrice) FROM Products')
    highest = cur.fetchone()[0]

    # Получить среднюю цену.
    cur.execute('SELECT AVG(RetailPrice) FROM Products')
    average = cur.fetchone()[0]

    # Показать результаты.
    print(f'Минимальная цена: ${lowest:.2f}')
    print(f'Максимальная цена: ${highest:.2f}')
    print(f'Средняя цена: ${average:.2f}')

	# Закрыть соединение с базой данных.
    conn.close()

# Вызвать главную функцию.
if __name__ == '__main__':
    main()