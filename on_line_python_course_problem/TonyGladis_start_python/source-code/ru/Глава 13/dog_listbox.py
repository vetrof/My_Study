# Эта программа получает выбранный пользователем вариант из виджета Listbox.
import tkinter
import tkinter.messagebox

class ListBoxSelection:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать виджет Listbox.
        self.dog_listbox = tkinter.Listbox(
            self.main_window, width=0, height=0)
        self.dog_listbox.pack(padx=10, pady=5)

        # Создать список с названиями пород собак.
        dogs = ['Лабрадор', 'Пудель', 'Дог', 'Терьер']

        # Заполнить виджет Listbox содержимым списка.
        for dog in dogs:
            self.dog_listbox.insert(tkinter.END, dog)

        # Создать кнопку, чтобы получать выбранный элемент.
        self.get_button = tkinter.Button(
            self.main_window, text='Получить элемент',
            command=self.__retrieve_dog)
        self.get_button.pack(padx=10, pady=5)

        # Запустить главный цикл.
        tkinter.mainloop()

    def __retrieve_dog(self):
        # Получить индекс выбранного элемента.
        indexes = self.dog_listbox.curselection()

        # Если элемент был выбран, то показать его.
        if (len(indexes) > 0):
            tkinter.messagebox.showinfo(
                message=self.dog_listbox.get(indexes[0]))
        else:
            tkinter.messagebox.showinfo(
                message='Ни один элемент не выбран.')

# Создать экземпляр класса ListBoxSelection.
if __name__ == '__main__':
    listbox_selection = ListBoxSelection()