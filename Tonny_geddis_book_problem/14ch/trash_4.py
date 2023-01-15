
import sqlite3

conn = sqlite3.connect('phonebook.db')
cur = conn.cursor()
data = cur.execute('SELECT * FROM Etries')

for i in data:
    print(i)
   


 

