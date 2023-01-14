
import sqlite3

# подключаемся к базе данных и получаем курсор
conn = sqlite3.connect('chocolate.db')
cur = conn.cursor()

# получаем от ползователя  ID номер товаря для изменения цены
id_product = int(input('Введите ID товара для измения цены: '))

# показать текущую цену товара с этим ID
cur.execute(''' SELECT ProductID, Description, RetailPrice 
                FROM Products
                WHERE ProductID == ?''', (id_product,))
curent_product = cur.fetchone()

# если введенный id корректен то выводим товар с этим айди
if curent_product != None:
    print(f'Текущая цена продукта: ID: {curent_product[0]} '
          f'{curent_product[1]} '
          f'- {curent_product[2]} ')

    # получаем новую цену от пользователи
    price_new = float(input('Новая цена: '))

    # вносим изменения в базу
    cur.execute(''' UPDATE Products
                    SET RetailPrice = ?
                    WHERE ProductID == ?''', (price_new, id_product))
    conn.commit()

    print('Стоимость изменена.')

else:
    print(f'ID товара {id_product} не найден.')

conn.close()






