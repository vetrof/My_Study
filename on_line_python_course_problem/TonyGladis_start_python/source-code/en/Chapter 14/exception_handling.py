import sqlite3

def main():
    # Loop-control variable
    again = 'y'

    while again == 'y':
        #Get the item ID, name and price.
        item_id = int(input('Item ID: '))
        item_name = input('Item Name: ')
        price = float(input('Price: '))
        
        # Add the item to the database.
        add_item(item_id, item_name, price)

        # Add another?
        again = input('Add another item? (y/n): ')    

# The add_item function adds an item to the database.
def add_item(item_id, name, price):
    # Initialize a connection variable.
    conn = None

    try:
        # Connect to the database
        conn = sqlite3.connect('inventory.db')

        # Get a cursor.
        cur = conn.cursor()

        # Add the item to the Inventory table.
        cur.execute('''INSERT INTO Inventory (ItemID, ItemName, Price)
                       VALUES (?, ?, ?)''',
                       (item_id, name, price))
        
        # Commit the changes.
        conn.commit()

    except sqlite3.Error as err:
        print(err)
    
    finally:
        # Close the connection.
        if conn != None:
            conn.close()

# Execute the main function.
if __name__ == '__main__':
    main()