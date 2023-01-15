import sqlite3

connect = sqlite3.connect('chocolate.db')
cursor = connect.cursor()

table_info = cursor.execute(''' SELECT Description, RetailPrice
                                FROM Products
                                WHERE RetailPrice > 9.0''')

list = table_info.fetchall()


for i in list:
    print(f'{i[0]:40} {i[1]:5}')



