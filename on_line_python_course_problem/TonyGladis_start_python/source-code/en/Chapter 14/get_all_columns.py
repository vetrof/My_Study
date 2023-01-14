import sqlite3

def main():
    # Connect to the database.
    conn = sqlite3.connect('chocolate.db')
    
    # Get a cursor.
    cur = conn.cursor()
    
    # Select all columns from each row from the Products table.
    cur.execute('SELECT * FROM Products')

    # Fetch the results of the SELECT statement.
    results = cur.fetchall()

    # Display the results.
    for row in results:
        print(f'{row[0]:2} {row[1]:30} {row[2]:5} {row[3]:5} {row[4]:5}')
    
    # Close the database connection.
    conn.close()

# Execute the main function.
if __name__ == '__main__':
    main()