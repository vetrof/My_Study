
import sqlite3

connect = sqlite3.connect('inventory.db')
cursor = connect.cursor()

# выводим все колонки из таблицы
cursor.execute('''SELECT * FROM Inventory''' )
all_row = cursor.fetchall()

# выводим только колонку с ItemName
cursor.execute('''SELECT ItemName FROM Inventory''' )
prdt_name = cursor.fetchall()

# выводим колонки ItemName и Price
cursor.execute('''SELECT ItemName, Price FROM Inventory''' )
name_n_price = cursor.fetchall()

# выводим name и cost из строк где цена меньше 17
cursor.execute('''SELECT ItemName, Price FROM Inventory WHERE Price > 17''' )
cost_17 = cursor.fetchall()

# выводим строки если в них есть буква 'a'
cursor.execute('''SELECT ItemName, Price FROM Inventory WHERE ItemName LIKE '%а%' ''' )
intem_winh_symbol_a = cursor.fetchall()


print('all rows: ', all_row)
print('product name: ', prdt_name)
print('Name abd Price: ', name_n_price)
print('Cost > 17: ', cost_17)
print('Symbol A: ', intem_winh_symbol_a)


