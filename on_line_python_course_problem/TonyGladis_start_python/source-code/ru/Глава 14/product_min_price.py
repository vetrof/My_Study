import sqlite3

def main():
    # Подсоединиться к базе данных.
    conn = sqlite3.connect('chocolate.db')

    # Получить курсор.
    cur = conn.cursor()

    # Получить от пользователя минимальную цену.
    min_price = float(input('Введите минимальную цену: '))

    # Отправить инструкцию SELECT в СУБД.
    cur.execute('''SELECT Description, RetailPrice FROM Products
                   WHERE RetailPrice >= ?''',
                (min_price,))

    # Извлечь результаты инструкции SELECT.
    results = cur.fetchall()

    if len(results) > 0:
        # Показать результаты.
        print('Вот результаты:')
        print()
        print('Описание                            Цена')
        print('----------------------------------------')
        for row in results:
            print(f'{row[0]:35} {row[1]:>5}')
    else:
        print('Ни одно изделие не найдено.')

    # Закрыть соединение с базой данных.
    conn.close()

# Вызвать главную функцию.
if __name__ == '__main__':
    main()