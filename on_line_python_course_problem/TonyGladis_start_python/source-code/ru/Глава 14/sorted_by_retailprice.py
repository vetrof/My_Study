import sqlite3

def main():
    # Подсоединиться к базе данных.
    conn = sqlite3.connect('chocolate.db')

    # Получить курсор.
    cur = conn.cursor()

    # Выбрать все столбцы из каждой строки таблицы Products.
    cur.execute('''SELECT Description, RetailPrice FROM Products
                   ORDER BY RetailPrice''')

    # Извлечь результаты инструкции SELECT.
    results = cur.fetchall()

    # Показать результаты.
    for row in results:
        print(f'{row[0]:35} {row[1]:5}')

    # Закрыть соединение с базой данных.
    conn.close()

# Вызвать главную функцию.
if __name__ == '__main__':
    main()