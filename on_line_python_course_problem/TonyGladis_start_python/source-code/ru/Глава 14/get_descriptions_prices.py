import sqlite3

def main():
    # Подсоединиться к базе данных.
    conn = sqlite3.connect('chocolate.db')

    # Получить курсор.
    cur = conn.cursor()

    # Получить описания и розничные цены.
    cur.execute('SELECT Description, RetailPrice FROM Products')

    # Извлечь результаты инструкции SELECT.
    results = cur.fetchall()

    # Перебрать строки и показать результаты.
    for row in results:
        print(f'{row[0]:35} {row[1]:5}')

    # Закрыть соединение в базой данных.
    conn.close()

# Вызвать главную функцию.
if __name__ == '__main__':
    main()