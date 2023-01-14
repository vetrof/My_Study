import sqlite3

def main():
    # Connect to the database.
    conn = sqlite3.connect('chocolate.db')
    
    # Get a cursor.
    cur = conn.cursor()
    
    # Get the lowest price.
    cur.execute('SELECT MIN(RetailPrice) FROM Products')
    lowest = cur.fetchone()[0]

    # Get the highest price.
    cur.execute('SELECT MAX(RetailPrice) FROM Products')
    highest = cur.fetchone()[0]

    # Get the average price.
    cur.execute('SELECT AVG(RetailPrice) FROM Products')
    average = cur.fetchone()[0]

    # Display the results.
    print(f'Lowest Price:  ${lowest:.2f}')
    print(f'Highest Price: ${highest:.2f}')
    print(f'Average Price: ${average:.2f}')
    
    # Close the database connection.
    conn.close()

# Execute the main function.
if __name__ == '__main__':
    main()