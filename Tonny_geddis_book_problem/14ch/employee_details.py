import tkinter
import tkinter.messagebox
import sqlite3

class EmployeeDetails:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Скомпоновать содержимое главного окна.
        self.__build_main_window()

        # Запустить главный цикл.
        tkinter.mainloop()

    # Скомпоновать главное окно.
    def __build_main_window(self):
        # Создать надпись с подсказкой для пользователя.
        self.__create_prompt_label()

        # Скомпоновать рамку виджета Listbox.
        self.__build_listbox_frame()

        # Создать кнопку Выйти.
        self.__create_quit_button()

    # Создать надпись с подсказкой для пользователя.
    def __create_prompt_label(self):
        self.employee_prompt_label = tkinter.Label(
            self.main_window, text='Выберите сотрудника')
        self.employee_prompt_label.pack(side='top', padx=5, pady=5)

    # Скомпоновать рамку, содержащую виджеты Listbox и Scrollbar
    def __build_listbox_frame(self):
        # Создать рамку для виджетов Listbox и Scrollbar.
        self.listbox_frame = tkinter.Frame(self.main_window)

        # Настроить виджет Listbox.
        self.__setup_listbox()

        # Создать полосу прокрутки для просмотра элементов в виджете Listbox.
        self.__create_scrollbar()

        # Заполнить виджет Listbox именами сотрудников.
        self.__populate_listbox()

        # Упаковать рамку виджета Listbox.
        self.listbox_frame.pack()

    # Создать виджет Listbox для вывода имен сотрудников на экран.
    def __setup_listbox(self):
        # Создать виджет Listbox.
        self.employee_listbox = tkinter.Listbox(
            self.listbox_frame, selectmode=tkinter.SINGLE, height=6)

        # Привязать виджет Listbox к функции обратного вызова.
        self.employee_listbox.bind(
            '<<ListboxSelect>>', self.__get_details)

        # Упаковать виджет Listbox.
        self.employee_listbox.pack(side='left', padx=5, pady=5)

    # Создать вертикальный виджет Scrollbar для использования с виджетом Listbox.
    def __create_scrollbar(self):
        self.scrollbar = tkinter.Scrollbar(self.listbox_frame,
                                            orient=tkinter.VERTICAL)
        self.scrollbar.config(command=self.employee_listbox.yview)
        self.employee_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side='right', fill=tkinter.Y)

    # Вывести на экран имена сотрудников в виджете Listbox.
    def __populate_listbox(self):
        for employee in self.__get_employees():
            self.employee_listbox.insert(tkinter.END, employee)

    # Создать кнопку выхода из программы.
    def __create_quit_button(self):
        self.quit_button = tkinter.Button(
                                    self.main_window,
                                    text='Выйти',
                                    command=self.main_window.destroy)
        self.quit_button.pack(side='top', padx=10, pady=5)

    # Получить список имен сотрудников из базы данных.
    def __get_employees(self):
        employee_list = []
        conn = None
        try:
            # Подсоединиться к базе данных и получить курсор.
            conn = sqlite3.connect('employees.db')
            cur = conn.cursor()

            # Исполнить запрос SELECT.
            cur.execute('SELECT Name FROM Employees')

            # Получить результаты запроса в виде списка.
            employee_list = [n[0] for n in cur.fetchall()]
        except sqlite3.Error as err:
            tkinter.messagebox.showinfo('Ошибка базы данных', err)
        finally:
            # Если соединение открыто, то закрыть его.
            if conn != None:
                conn.close()

            return employee_list

    # Получить подробную информацию по выбранному сотруднику.
    def __get_details(self, event):
        # Получить выбранное имя из виджета Listbox.
        listbox_index = self.employee_listbox.curselection()[0]
        selected_emp = self.employee_listbox.get(listbox_index)

        # Запросить в базе данных информацию о выбранном сотруднике.
        conn = None
        try:
            # Подсоединиться к базе данных и получить курсор.
            conn = sqlite3.connect('employees.db')
            cur = conn.cursor()

            # Исполнить запрос SELECT.
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

            # Получить результаты запроса.
            results = cur.fetchone()

            # Вывести на экран информацию о сотруднике.
            self.__display_details(name=results[0], position=results[1],
            department=results[2], location=results[3])
        except sqlite3.Error as err:
            tkinter.messagebox.showinfo('Ошибка базы данных', err)
        finally:
            # Если соединение открыто, то закрыть его.
            if conn != None:
                conn.close()

    # Вывести в диалоговом окне на экран информацию о сотруднике.
    def __display_details(self, name, position, department, location):
        tkinter.messagebox.showinfo('Информация о сотруднике',
                                    'Имя: ' + name +
                                    '\nДолжность: ' + position +
                                    '\nОтдел: ' + department +
                                    '\nМестоположение: ' + location)

# Создать экземпляр класса EmployeeDetails.
if __name__ == '__main__':
    employee_details = EmployeeDetails()