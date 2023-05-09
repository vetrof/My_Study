
import sqlite3

# подсоединится к базе данных
connect = sqlite3.connect('contacts.db')

# получить курсор
cursor = connect.cursor()

# операции с базой данных
# -------
cursor.execute('''CREATE TABLE Contacts (
                  ContactID INTEGER PRIMARY KEY NOT NULL,
                  Name TEXT,
                  Email TEXT
                  )''')