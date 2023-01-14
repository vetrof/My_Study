import sqlite3

def main():
    # Подсоединиться к базе данных.
    conn = sqlite3.connect('chocolate.db')

    # Получить курсор.
    cur = conn.cursor()

    # Выбрать все столбцы из каждой строки таблицы Products.
    cur.execute('SELECT * FROM Products')

    # Излечь результаты инструкции SELECT.
    results = cur.fetchall()

    # Показать результаты.
    for row in results:
        print(f'{row[0]:2} {row[1]:35} {row[2]:5} {row[3]:6} {row[4]:5}')

    # Закрыть соединение с базой данных.
    conn.close()

# Вызвать главную функцию.
if __name__ == '__main__':
    main()