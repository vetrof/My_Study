# Эта программа демонстрирует виджет Listbox с вертикальной прокруткой.
import tkinter

class VerticalScrollbarExample:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать рамку для виджета Listbox и вертикальную прокрутку.
        self.listbox_frame = tkinter.Frame(self.main_window)
        self.listbox_frame.pack(padx=20, pady=20)

        # Создать виджет Listbox в рамке listbox_frame.
        self.listbox = tkinter.Listbox(
            self.listbox_frame, height=6, width=0)
        self.listbox.pack(side='left')

        # Создать вертикальный виджет Scrollbar в рамке listbox_frame.
        self.scrollbar = tkinter.Scrollbar(
            self.listbox_frame, orient=tkinter.VERTICAL)
        self.scrollbar.pack(side='right', fill=tkinter.Y)

        # Сконфигурировать виджеты Scrollbar и Listbox для совместной работы.
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        # Создать список названий месяцев.
        months = ['Январь', 'Февраль', 'Март', 'Апрель',
                'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь',
                'Октябрь', 'Ноябрь', 'Декабрь']

        # Заполнить виджет Listbox данными.
        for month in months:
            self.listbox.insert(tkinter.END, month)

        # Запустить главный цикл.
        tkinter.mainloop()

# Создать экземпляр класса VerticalScrollbarExample.
if __name__ == '__main__':
    scrollbar_example = VerticalScrollbarExample()