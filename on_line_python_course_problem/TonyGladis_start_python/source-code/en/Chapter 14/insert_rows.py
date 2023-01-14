import sqlite3

def main():
    # Connect to the database.
    conn = sqlite3.connect('inventory.db')
    
    # Get a cursor.
    cur = conn.cursor()
    
    # Add a row to the Inventory table.
    cur.execute('''INSERT INTO Inventory (ItemName, Price)
                   VALUES ("Screwdriver", 4.99)''')
    
    # Add another row to the Inventory table.
    cur.execute('''INSERT INTO Inventory (ItemName, Price)
                   VALUES ("Hammer", 12.99)''')
    
    # Add another row to the Inventory table.
    cur.execute('''INSERT INTO Inventory (ItemName, Price)
                   VALUES ("Vice Grips", 14.99)''')
    
    # Commit the changes.
    conn.commit()
    
    # Close the connection.
    conn.close()

# Execute the main function.
if __name__ == '__main__':
    main()