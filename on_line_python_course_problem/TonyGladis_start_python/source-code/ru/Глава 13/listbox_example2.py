# Эта программа демонстрирует простой виджет Listbox.
import tkinter

class ListboxExample:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать виджет Listbox.
        self.listbox = tkinter.Listbox(
        self.main_window, height=0, width=0)
        self.listbox.pack(padx=10, pady=10)

        # Создать список с днями недели.
        days = ['Понедельник', 'Вторник', 'Среда',
                'Четверг', 'Пятница', 'Суббота',
                'Воскресенье']

        # Заполнить виджет Listbox данными.
        for day in days:
            self.listbox.insert(tkinter.END, day)

        # Запустить главный цикл.
        tkinter.mainloop()

# Создать экземпляр класса ListboxExample.
if __name__ == '__main__':
    listbox_example = ListboxExample()