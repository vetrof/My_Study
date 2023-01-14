
import sqlite3

conn = sqlite3.connect('phonebooc.db')
cur = conn.cursor
print(cur)
# data = conn.execute('SELECT * FROM Etries')

# for i in data:
#     print(i)


