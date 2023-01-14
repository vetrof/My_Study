import sqlite3

def main():
    # Подсоединиться к базе данных.
    conn = sqlite3.connect('chocolate.db')

    # Получить курсор.
    cur = conn.cursor()

    # Получить от пользователя ProductID.
    pid = int(input('Введите ID изделия: '))

    # Получить текущую цену для этого изделия.
    cur.execute('''SELECT Description, RetailPrice FROM Products
                   WHERE ProductID == ?''', (pid,))
    results = cur.fetchone()

    # Если ID изделия найден, то продолжить...
    if results != None:
        # Напечатать текущую цену.
        print(f'Текущая цена для {results[0]}: '
              f'${results[1]:.2f}')

        # Получить новую цену.
        new_price = float(input('Введите новую цену: '))

        # Обновить цену в таблице Products.
        cur.execute('''UPDATE Products
                       SET RetailPrice = ?
                       WHERE ProductID == ?''',
                       (new_price, pid))

        # Зафиксировать изменения.
        conn.commit()
        print('Цена была изменена.')
    else:
        # Сообщение об ошибке.
        print(f'ID изделия {pid} не найден.')

    # Закрыть соединение с базой данных.
    conn.close()

# Вызвать главную функцию.
if __name__ == '__main__':
    main()