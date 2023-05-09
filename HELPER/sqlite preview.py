import sqlite3

# вывести названия всех таблиц
con = sqlite3.connect("django_senior_pomidor/db.sqlite3")
cursor = con.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

# вывести данные одной таблицы
con = sqlite3.connect("django_senior_pomidor/db.sqlite3")
cursor = con.cursor()
cursor.execute("SELECT * FROM order_salesorder")
print(cursor.fetchall())

