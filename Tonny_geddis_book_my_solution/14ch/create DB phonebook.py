

import sqlite3

conn = sqlite3.connect('phonebook.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Etries
                (RowID INTEGER PRIMARY KEY,
                 Name TEXT,
                 Phone INTEGER)''')

conn.commit()
conn.close()


