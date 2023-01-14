# Эта программа демонстрирует виджет Listbox с горизонтальной прокруткой.
import tkinter

class HorizontalScrollbarExample:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать рамку для виджета Listbox и вертикальную прокрутку.
        self.listbox_frame = tkinter.Frame(self.main_window)
        self.listbox_frame.pack(padx=20, pady=20)

        # Создать виджет Listbox в рамке listbox_frame.
        self.listbox = tkinter.Listbox(
            self.listbox_frame, height=0, width=30)
        self.listbox.pack(side='top')

        # Создать горизонтальный виджет Scrollbar в рамке listbox_frame.
        self.scrollbar = tkinter.Scrollbar(
            self.listbox_frame, orient=tkinter.HORIZONTAL)
        self.scrollbar.pack(side='bottom', fill=tkinter.X)

        # Сконфигурировать виджеты Scrollbar и Listbox для совместной работы.
        self.scrollbar.config(command=self.listbox.xview)
        self.listbox.config(xscrollcommand=self.scrollbar.set)

        # Создать список.
        data = [
            ' Небоскреб Бурдж-Халифа имеет высоту 2717 футов.',
            ' Шанхайская башня имеет высоту 2073 фута.',
            ' Часовая башня Абрадж аль-Бейт имеет высоту 1971 фут.',
            ' Финансовый центр Пинань имеет высоту 1965 футов.']

        # Заполнить виджет Listbox данными.
        for element in data:
            self.listbox.insert(tkinter.END, element)

        # Запустить главный цикл.
        tkinter.mainloop()

# Создать экземпляр класса HorizontalScrollbarExample.
if __name__ == '__main__':
    scrollbar_example = HorizontalScrollbarExample()