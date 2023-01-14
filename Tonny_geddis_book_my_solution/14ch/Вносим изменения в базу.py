

import sqlite3

conn = sqlite3.connect('chocolate.db')
cur = conn.cursor()

# просим юзера ввести клюевое слово для более удобного поиска нужной позиции
user_input_name = input('Введите слово для поиска изменяемой позиции: ')
# user_input_name = 'Плитка'
user_input_name = f'%{user_input_name}%'


# выводим названия продуктов с ключевым словом
cur.execute(''' SELECT ProductID, Description, RetailPrice 
                FROM Products 
                WHERE Description LIKE ? ''', (user_input_name,))
all_match_position = cur.fetchall()



# если ключевое слово есть в товарах то выводим список, если нет - то пишем ошибку
if len(all_match_position) > 0:
    print('Надено позиций: ', len(all_match_position))
    for i in all_match_position:
        print(i)
else:
    print('Совпадений по ключевому слову не найдено, попробуйте ввести ID')


# просим юзера ввести айди товара дл изменения цены
print('----------')
id_for_change = input('Введите ID для изменения цены: ')

# просим ввести новую цену
cost_new = input('Введите новую стоимость: ')


# выводим сначала старую стоимость
old_cost = cur.execute(''' SELECT ProductID, Description, RetailPrice 
                           FROM Products
                           WHERE ProductID == ? ''', (id_for_change,))
print()
print('Старая цена: ', old_cost.fetchone())

# вносим изменения в базу данных
cur.execute(''' UPDATE Products
                SET RetailPrice = ?
                WHERE ProductID == ?

                ''', (cost_new, id_for_change,))

# вносим изменения в базу
conn.commit()

# выводим обновленную цену
new_cost = cur.execute(''' SELECT ProductID, Description, RetailPrice
                           FROM Products
                           WHERE ProductID == ? ''', (id_for_change,))
print('Новая цена: ', new_cost.fetchone())







