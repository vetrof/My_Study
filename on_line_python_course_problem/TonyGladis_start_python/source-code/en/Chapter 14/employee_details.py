import tkinter
import tkinter.messagebox
import sqlite3

class EmployeeDetails:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Build the contents of the main window.
        self.__build_main_window()

        # Start the main loop.
        tkinter.mainloop()

    # Build the main window.
    def __build_main_window(self):
        # Create a label to prompt the user.
        self.__create_prompt_label()
        
        # Build the Listbox frame.
        self.__build_listbox_frame()
        
        # Create a Quit button.
        self.__create_quit_button()

    # Create a label to prompt the user.
    def __create_prompt_label(self):
        self.employee_prompt_label = tkinter.Label(
            self.main_window, text='Select an employee')
        self.employee_prompt_label.pack(side='top', padx=5, pady=5)
    
    # Build a frame containing the Listbox and a Scrollbar
    def __build_listbox_frame(self):
        # Create a frame to hold the Listbox and scrollbar.
        self.listbox_frame = tkinter.Frame(self.main_window)

        # Set up the Listbox.
        self.__setup_listbox()

        # Create a scrollbar to scroll the Listbox.
        self.__create_scrollbar()
        
        # Populate the listbox with employee names.
        self.__populate_listbox()

        # Pack the Listbox frame.
        self.listbox_frame.pack()
    
    # Create the Listbox to display employee names.
    def __setup_listbox(self):
        # Create the Listbox widget.
        self.employee_listbox = tkinter.Listbox(
            self.listbox_frame, selectmode=tkinter.SINGLE, height=6)
        
        # Bind the Listbox to a callback function.
        self.employee_listbox.bind(
            '<<ListboxSelect>>', self.__get_details)

        # Pack the Listbox.
        self.employee_listbox.pack(side='left',padx=5, pady=5)
    
    # Create a vertical Scrollbar to use with the Listbox.
    def __create_scrollbar(self):
        self.scrollbar = tkinter.Scrollbar(self.listbox_frame,
                                           orient=tkinter.VERTICAL)
        self.scrollbar.config(command=self.employee_listbox.yview)
        self.employee_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side='right', fill=tkinter.Y)

    # Display employee names in the Listbox.
    def __populate_listbox(self):
        for employee in self.__get_employees():
            self.employee_listbox.insert(tkinter.END, employee)

    # Create a button to quit the program.
    def __create_quit_button(self):
        self.quit_button = tkinter.Button(
                            self.main_window,
                            text='Quit',
                            command=self.main_window.destroy)
        self.quit_button.pack(side='top', padx=10, pady=5)

    # Get a list of employee names from the database.
    def __get_employees(self):
        employee_list = []
        conn = None
        try:
            # Connect to the database and get a Cursor.
            conn = sqlite3.connect('employees.db')
            cur = conn.cursor()

            # Execute the SELECT query.
            cur.execute('SELECT Name FROM Employees')

            # Get the results of the query as a list.
            employee_list = [n[0] for n in cur.fetchall()]
        except sqlite3.Error as err:
            tkinter.messagebox.showinfo('Database Error', err)
        finally:
            # If the database connection is open, close it.
            if conn != None:
                conn.close()

        return employee_list
    
    # Get detailed information for the selected employee.
    def __get_details(self, event):
        # Get the selected name from the Listbox.
        listbox_index = self.employee_listbox.curselection()[0]
        selected_emp = self.employee_listbox.get(listbox_index)

        # Query the database for the selected employee's details.
        conn = None
        try:
            # Connect to the database and get a Cursor.
            conn = sqlite3.connect('employees.db')
            cur = conn.cursor()

            # Execute the SELECT query.
            cur.execute(
              '''SELECT
                   Employees.Name,
                   Employees.Position,
                   Departments.DepartmentName,
                   Locations.City
                 FROM
                   Employees, Departments, Locations
                 WHERE
                   Employees.Name == ? AND
                   Employees.DepartmentID == Departments.DepartmentID AND
                   Employees.LocationID == Locations.LocationID''',
              (selected_emp,))
            
            # Get the results of the query.
            results = cur.fetchone()

            # Display the employee details.
            self.__display_details(name=results[0], position=results[1],
                             department=results[2], location=results[3])
        except sqlite3.Error as err:
            tkinter.messagebox.showinfo('Database Error', err)
        finally:
            # If the database connection is open, close it.
            if conn != None:
                conn.close()

    # Display employee details in an info box.
    def __display_details(self, name, position, department, location):
        tkinter.messagebox.showinfo('Employee Details',
                                    'Name: ' + name +
                                    '\nPosition: ' + position +
                                    '\nDepartment: ' + department +
                                    '\nLocation: ' + location)

# Create an instance of the EmployeeDetails class.
if __name__ == '__main__':
    employee_details = EmployeeDetails()