import sqlite3

def main():
    # Connect to the database.
    conn = sqlite3.connect('company.db')
    
    # Get a cursor.
    cur = conn.cursor()
    
    # Add the Customer table.
    cur.execute('''CREATE TABLE Customer (CustomerID INTEGER PRIMARY KEY,
                                          Name TEXT,
                                          Email TEXT)''')
    
    # Add the Employee table.
    cur.execute('''CREATE TABLE Employee (EmployeeID INTEGER PRIMARY KEY,
                                          Name TEXT,
                                          Position TEXT)''')
    
    # Commit the changes.
    conn.commit()
    
    # Close the connection.
    conn.close()

# Execute the main function.
if __name__ == '__main__':
    main()