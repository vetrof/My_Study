import sqlite3

MIN_CHOICE = 1
MAX_CHOICE = 5
CREATE = 1
READ = 2
UPDATE = 3
DELETE = 4
EXIT = 5

def main():
    choice = 0
    while choice != EXIT:
        display_menu()
        choice = get_menu_choice()

        if choice == CREATE:
            create()
        elif choice == READ:
            read()
        elif choice == UPDATE:
            update()
        elif choice == DELETE:
            delete()

# The display_menu function displays the main menu.
def display_menu():
    print('\n----- Inventory Menu -----')
    print('1. Create a new item')
    print('2. Read an item')
    print('3. Update an item')
    print('4. Delete an item')
    print('5. Exit the program')

# The get_menu_choice function gets the user's menu choice.
def get_menu_choice():
    # Get the user's choice.
    choice = int(input('Enter your choice: '))

    # Validate the input.
    while choice < MIN_CHOICE or choice > MAX_CHOICE:
        print(f'Valid choices are {MIN_CHOICE} through {MAX_CHOICE}.')
        choice = int(input('Enter your choice: '))
    
    return choice

# The create function creates a new item.
def create():
    print('Create New Item')
    name = input('Item Name: ')
    price = input('Price: ')
    insert_row(name, price)

# The read function reads an existing item.
def read():
    name = input('Enter an item name to search for: ')
    num_found = display_item(name)
    print(f'{num_found} row(s) found.')

# The update function updates an existing item's data.
def update():
    # First let the user search for the row.
    read()

    # Get the ID of the selected item.
    selected_id = int(input('Select an Item ID: '))

    # Get the new values for item name and price.
    name = input('Enter the new item name: ')
    price = input('Enter the new price: ')

    # Update the row.
    num_updated = update_row(selected_id, name, price)
    print(f'{num_updated} row(s) updated.')

# The delete function deletes an item.
def delete():
    # First let the user search for the row.
    read()

    # Get the ID of the selected item.
    selected_id = int(input('Select an Item ID to delete: '))

    # Confirm the deletion.
    sure = input('Are you sure you want to delete this item? (y/n) ')
    if sure.lower() == 'y':
        num_deleted = delete_row(selected_id)
        print(f'{num_deleted} row(s) deleted.')

# The insert_row function inserts a row into the Inventory table.
def insert_row(name, price):
    conn = None
    try:
        conn = sqlite3.connect('inventory.db')
        cur = conn.cursor()
        cur.execute('''INSERT INTO Inventory (ItemName, Price)
                       VALUES (?, ?)''',
                    (name, price))
        conn.commit()
    except sqlite3.Error as err:
        print('Database Error', err)
    finally:
        if conn != None:
            conn.close()

# The display_item function displays all items 
# with a matching ItemName.
def display_item(name):
    conn = None
    results = []
    try:
        conn = sqlite3.connect('inventory.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Inventory
                       WHERE lower(ItemName) == ?''',
                    (name,))
        results = cur.fetchall()

        for row in results:
            print(f'ID: {row[0]:<3} Name: {row[1]:<15} '
                  f'Price: {row[2]:<6}')
    except sqlite3.Error as err:
        print('Database Error', err)
    finally:
        if conn != None:
            conn.close()
    # Return the number of matching rows.
    return len(results)

# The update_row function updates an existing row with a new
# ItemName and Price. The number of rows updated is returned.
def update_row(id, name, price):
    conn = None
    try:
        conn = sqlite3.connect('inventory.db')
        cur = conn.cursor()
        cur.execute('''UPDATE Inventory
                       SET ItemName = ?, Price = ?
                       WHERE ItemID == ?''',
                    (name, price, id))
        conn.commit()
        num_updated = cur.rowcount
    except sqlite3.Error as err:
        print('Database Error', err)
    finally:
        if conn != None:
            conn.close()
    
    return num_updated

# The delete_row function deletes an existing item.
# The number of rows deleted is returned.
def delete_row(id):
    conn = None
    try:
        conn = sqlite3.connect('inventory.db')
        cur = conn.cursor()
        cur.execute('''DELETE FROM Inventory
                       WHERE ItemID == ?''',
                    (id,))
        conn.commit()
        num_deleted = cur.rowcount
    except sqlite3.Error as err:
        print('Database Error', err)
    finally:
        if conn != None:
            conn.close()

    return num_deleted

# Execute the main function.
if __name__ == '__main__':
    main()