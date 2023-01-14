import sqlite3
 
def main():
    conn = sqlite3.connect('contacts.db')
    cur = conn.cursor()

    # Здесь вставить код для выполнения операций с базой данных.

    conn.commit()
    conn.close()

# Вызвать главную функцию.
if __name__ == '__main__':
    main()