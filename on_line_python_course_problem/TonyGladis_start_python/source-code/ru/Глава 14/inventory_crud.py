import sqlite3

MIN_CHOICE = 1
MAX_CHOICE = 5
CREATE = 1
READ = 2
UPDATE = 3
DELETE = 4
EXIT = 5

def main():
    choice = 0
    while choice != EXIT:
        display_menu()
        choice = get_menu_choice()

        if choice == CREATE:
            create()
        elif choice == READ:
            read()
        elif choice == UPDATE:
            update()
        elif choice == DELETE:
            delete()

# Функция display_menu выводит на экран главное меню.
def display_menu():
    print('\n----- Меню ведения учета инструментов -----')
    print('1. Создать новую позицию')
    print('2. Прочитать позицию')
    print('3. Обновить позицию')
    print('4. Удалить позицию')
    print('5. Выйти из программы')

# Функция get_menu_choice получает от пользователя пункт меню.
def get_menu_choice():
    # Получить от пользователя вариант действия.
    choice = int(input('Введите ваш вариант: '))

    # Проведить входные данные.
    while choice < MIN_CHOICE or choice > MAX_CHOICE:
        print(f'Допустимые варианты таковы: {MIN_CHOICE} - {MAX_CHOICE}.')
        choice = int(input('Введите ваш вариант: '))

    return choice

# Функция create создает новую позицию.
def create():
    print('Создать новую позицию')
    name = input('Название позиции: ')
    price = input('Цена: ')
    insert_row(name, price)

# Функция read читает существующую позицию.
def read():
    name = input('Введите название искомой позиции: ')
    num_found = display_item(name)
    print(f'{num_found} строк(а) найдено.')

# Функция update обновляет данные существующей позиции.
def update():
    # Сначала показать пользователю найденные строки.
    read()

    # Получить ID выбранной позиции.
    selected_id = int(input('Выберите ID обновляемой позиции: '))

    # Получить новые значения для названия и цены.
    name = input('Введите новое название позиции: ')
    price = input('Введите новую цену: ')

    # Обновить строку.
    num_updated = update_row(selected_id, name, price)
    print(f'{num_updated} строк(а) обновлено.')

# Функция delete удаляет позицию.
def delete():
    # Сначала показать пользователю найденные строки.
     read()

    # Получить ID выбранной позиции.
    selected_id = int(input('Выберите ID удаляемой позиции: '))

    # Подтвердить удаление.
    sure = input('Вы уверены, что хотите удалить эту позицию? (д/н): ')
    if sure.lower() == 'д':
        num_deleted = delete_row(selected_id)
        print(f'{num_deleted} строк(а) удалено.')

# Функция insert_row вставляет строку в таблицу Inventory.
def insert_row(name, price):
    conn = None
    try:
        conn = sqlite3.connect('inventory.db')
        cur = conn.cursor()
        cur.execute('''INSERT INTO Inventory (ItemName, Price)
                       VALUES (?, ?)''',
                       (name, price))
        conn.commit()
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn != None:
            conn.close()

# Функция display_item выводит на экран все позиции
# с совпадающими названиями позиций.
def display_item(name):
    conn = None
    results = []
    try:
        conn = sqlite3.connect('inventory.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Inventory
                       WHERE ItemName == ?''',
                       (name,))
        results = cur.fetchall()

        for row in results:
            print(f'ID: {row[0]:<3} Название: {row[1]:<15} '
                  f'Цена: {row[2]:<6}')
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn != None:
            conn.close()
        # Вернуть число совпавших строк.
        return len(results)

# Функция update_row обновляет существующую строку новыми
# названием и ценой. Возвращается обновленное число строк.
def update_row(id, name, price):
    conn = None
    try:
        conn = sqlite3.connect('inventory.db')
        cur = conn.cursor()
        cur.execute('''UPDATE Inventory
                       SET ItemName = ?, Price = ?
                       WHERE ItemID == ?''',
                       (name, price, id))
        conn.commit()
        num_updated = cur.rowcount
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn != None:
            conn.close()

        return num_updated

# Функция delete_row удаляет существующую позицию.
# Возвращается число удаленных строк.
def delete_row(id):
    conn = None
    try:
        conn = sqlite3.connect('inventory.db')
        cur = conn.cursor()
        cur.execute('''DELETE FROM Inventory
                       WHERE ItemID == ?''',
                       (id,))
        conn.commit()
        num_deleted = cur.rowcount
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn != None:
            conn.close()

        return num_deleted

# Вызвать главную функцию.
if __name__ == '__main__':
    main()