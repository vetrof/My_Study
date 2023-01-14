import sqlite3

def main():
    # Connect to the database.
    conn = sqlite3.connect('chocolate.db')
    
    # Get a cursor.
    cur = conn.cursor()

    # Get a ProductID from the user.
    pid = int(input('Enter a product ID: '))

    # Get the current price for that product.
    cur.execute('''SELECT Description, RetailPrice From Products
                   WHERE ProductID == ?''', (pid,))
    results = cur.fetchone()

    # If the Product ID was found, continue...
    if results != None:
        # Print the current price.
        print(f'The current price for {results[0]} '
              f'is ${results[1]:.2f}')

        # Get the new price.
        new_price = float(input('Enter the new price: '))

        # Update the price in the Products table.
        cur.execute('''UPDATE Products
                       SET RetailPrice = ?
                       WHERE ProductID == ?''',
                       (new_price, pid))

        # Commit the changes
        conn.commit()
        print('The price was changed.')
    else:
        # Error message.
        print(f'Product ID {pid} not found.')
    
    # Close the database connection.
    conn.close()

# Execute the main function.
if __name__ == '__main__':
    main()