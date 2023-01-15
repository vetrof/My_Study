
import sqlite3


name = 'TIDE'
cost = 10.99


connect = sqlite3.connect('trash_db.db')
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Trash 
                 (Id INTEGER PRIMARY KEY NOT NULL,
                  Name TXT,
                  Cost REAL)
                    ''')


cursor.execute(''' INSERT INTO Trash
                    (Name, Cost) 
                    VALUES (?, ?)''', (name, cost))



connect.commit()
connect.close()
