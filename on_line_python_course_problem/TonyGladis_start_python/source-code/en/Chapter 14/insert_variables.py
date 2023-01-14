import sqlite3

def main():
    # Loop-control variable
    again = 'y'

    # Connect to the database.
    conn = sqlite3.connect('inventory.db')
    
    # Get a cursor.
    cur = conn.cursor()
    
    while again == 'y':
        # Get the item name and price.
        item_name = input('Item Name: ')
        price = float(input('Price: '))
        
        # Add the item to the Inventory table.
        cur.execute('''INSERT INTO Inventory (ItemName, Price)
                       VALUES (?, ?)''',
                       (item_name, price))

        # Add another?
        again = input('Add another item? (y/n): ')    
    
    # Commit the changes.
    conn.commit()
    
    # Close the connection.
    conn.close()

# Execute the main function.
if __name__ == '__main__':
    main()