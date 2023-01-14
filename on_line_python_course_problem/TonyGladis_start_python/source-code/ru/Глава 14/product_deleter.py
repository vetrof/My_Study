import sqlite3

def main():
    # Подсоединиться к базе данных.
    conn = sqlite3.connect('chocolate.db')

    # Получить курсор.
    cur = conn.cursor()

    # Получить от пользователя ID изделия.
    pid = int(input('Введите ID изделия для его удаления: '))

    # Получить описание этого изделия.
    cur.execute('''SELECT Description FROM Products
                   WHERE ProductID == ?''', (pid,))
    results = cur.fetchone()

    # Если ID изделия найден, то продолжить...
    if results != None:
        # Подтвердить желание удалить изделие.
        sure = input(f'Вы уверены, что хотите удалить '
                     f'{results[0]}? (д/н): ')

        # Если да, то удалить изделие.
        if sure.lower() == 'д':
            cur.execute('''DELETE FROM Products
                           WHERE ProductID == ?''',
                        (pid,))

            # Зафиксировать изменения.
            conn.commit()
            print('Изделие было удалено.')
        else:
            # Сообщение об ошибке.
            print(f'ID изделия {pid} не найден.')

    # Закрыть соединение с базой данных.
    conn.close()

# Вызвать главную функцию.
if __name__ == '__main__':
    main()