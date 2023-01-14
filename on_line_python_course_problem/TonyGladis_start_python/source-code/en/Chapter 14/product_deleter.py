import sqlite3

def main():
    # Connect to the database.
    conn = sqlite3.connect('chocolate.db')
    
    # Get a cursor.
    cur = conn.cursor()

    # Get a ProductID from the user.
    pid = int(input('Enter a product ID to delete: '))

    # Get the description for that product.
    cur.execute('''SELECT Description From Products
                   WHERE ProductID == ?''', (pid,))
    results = cur.fetchone()

    # If the Product ID was found, continue...
    if results != None:
        # Confirm that the user wants to delete.
        sure = input(f'Are you sure you want to delete '
                     f'{results[0]}? (y/n) ')
        
        # If so, delete the product.
        if sure.lower() == 'y':
            cur.execute('''DELETE FROM Products
                           WHERE ProductID == ?''',
                           (pid,))
            
            # Commit the changes
            conn.commit()
            print('The product was deleted.')
    else:
        # Error message.
        print(f'Product ID {pid} not found.')
    
    # Close the database connection.
    conn.close()

# Execute the main function.
if __name__ == '__main__':
    main()