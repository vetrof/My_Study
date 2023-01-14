# Эта программа демонстрирует простой виджет Listbox.
import tkinter

class ListboxExample:
    def __init__(self):
    # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать виджет Listbox.
        self.listbox = tkinter.Listbox(self.main_window)
        self.listbox.pack(padx=10, pady=10)

        # Заполнить виджет Listbox данными.
        self.listbox.insert(0, 'Понедельник')
        self.listbox.insert(1, 'Вторник')
        self.listbox.insert(2, 'Среда')
        self.listbox.insert(3, 'Четверг')
        self.listbox.insert(4, 'Пятница')
        self.listbox.insert(5, 'Суббота')
        self.listbox.insert(6, 'Воскресенье')

		# Запустить главный цикл.
        tkinter.mainloop()

# Создать экземпляр класса ListboxExample.
if __name__ == '__main__':
    listbox_example = ListboxExample()