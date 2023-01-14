import sqlite3

def main():
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS Departments')
    cur.execute('DROP TABLE IF EXISTS Locations')
    cur.execute('DROP TABLE IF EXISTS Employees')

    cur.execute('''CREATE TABLE Departments(DepartmentID INTEGER PRIMARY KEY NOT NULL,
                                            DepartmentName TEXT)''')
    cur.execute('''CREATE TABLE Locations(LocationID INTEGER PRIMARY KEY NOT NULL,
                                          City TEXT)''')
    cur.execute('''CREATE TABLE Employees(EmployeeID INTEGER PRIMARY KEY NOT NULL,
                                          Name TEXT,
                                          Position TEXT,
                                          DepartmentID INTEGER,
                                          LocationID INTEGER,
                                          FOREIGN KEY(DepartmentID) REFERENCES Departments(DepartmentID),
                                          FOREIGN KEY(LocationID) REFERENCES Locations(LocationID))''')
    
    cur.execute('''INSERT INTO Departments (DepartmentID, DepartmentName)
                   VALUES (1, "Accounting"),
                          (2, "Manufacturing"),
                          (3, "Marketing"),
                          (4, "Research and Development")''')
    
    cur.execute('''INSERT INTO Locations (LocationID, City)
                   VALUES (1, "Austin"),
                          (2, "Boston"),
                          (3, "New York City"),
                          (4, "San Jose")''')

    cur.execute('''INSERT INTO Employees (EmployeeID, Name, Position, DepartmentID, LocationID)
                   VALUES (1, "Arlene Meyers", "Director", 4, 4),
                          (2, "Janelle Grant", "Engineer", 2, 1),
                          (3, "Jack Smith", "Manager", 3, 3),
                          (4, "Sonia Alvarado", "Auditor", 1, 2),
                          (5, "Renee Kincaid", "Designer", 3, 3),
                          (6, "Curt Green", "Supervisor", 2, 1)''')
    
    conn.commit()
    conn.close()

# Execute the main function.
if __name__ == '__main__':
    main()