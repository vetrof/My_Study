import sqlite3

def main():
    # Connect to the database.
    conn = sqlite3.connect('chocolate.db')
    
    # Get a cursor.
    cur = conn.cursor()

    # Get the minimum price from the user.
    min_price = float(input('Enter the minimum price: '))
    
    # Send the SELECT statement to the DBMS.
    cur.execute('''SELECT Description, RetailPrice FROM Products
                   WHERE RetailPrice >= ?''',
                   (min_price,))

    # Fetch the results of the SELECT statement.
    results = cur.fetchall()

    if len(results) > 0:
        # Display the results.
        print()
        print('Description                    Price')
        print('------------------------------------')
        for row in results:
            print(f'{row[0]:30} {row[1]:>5}')
    else:
        print('No products found.')
    
    # Close the database connection.
    conn.close()

# Execute the main function.
if __name__ == '__main__':
    main()