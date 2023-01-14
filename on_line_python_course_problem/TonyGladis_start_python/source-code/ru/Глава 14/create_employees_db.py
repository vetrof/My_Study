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
                   VALUES (1, "Бухгалтерский учет"),
                          (2, "Производство"),
                          (3, "Маркетинг"),
                          (4, "Исследования и разработка")''')
    
    cur.execute('''INSERT INTO Locations (LocationID, City)
                   VALUES (1, "Остин"),
                          (2, "Бостон"),
                          (3, "Нью-Йорк"),
                          (4, "Сан-Хосе")''')

    cur.execute('''INSERT INTO Employees (EmployeeID, Name, Position, DepartmentID, LocationID)
                   VALUES (1, "Рлин Мейерс", "Директор", 4, 4),
                          (2, "Джанель Грант", "Инженер", 2, 1),
                          (3, "Джек Смит", "Менеджер", 3, 3),
                          (4, "Соня Альварадо", "Аудитор", 1, 2),
                          (5, "Рене Кинкейд", "Дизайнер", 3, 3),
                          (6, "Курт Грин", "Супервайзер", 2, 1)''')
    
    conn.commit()
    conn.close()

# Execute the main function.
if __name__ == '__main__':
    main()