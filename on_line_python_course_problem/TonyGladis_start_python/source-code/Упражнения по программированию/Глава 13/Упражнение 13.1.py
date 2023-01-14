# Упражнение по программированию 13.1

# ФИО и адрес

import tkinter
from tkinter.ttk import *

class ShowInfoGUI:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать две рамки.
        self.top_frame = Frame(self.main_window)
        self.bottom_frame = Frame(self.main_window)
        
        # Создать пустое поле в верхней рамке.
        self.value = tkinter.StringVar()
        self.address_label = Label(self.top_frame, 
                             textvariable= self.value)
                       
        # Создать две кнопки в нижней рамке.
        self.address_button = Button(self.bottom_frame, 
                                     text = 'Показать инфо', 
                                     command = self.show_info)
        self.quit_button = Button(self.bottom_frame, 
                                  text = 'Выйти', 
                                  command = self.main_window.destroy)

        # Упаковать элемент Label.
        self.address_label.pack()
        
        # Упаковать элементы Button.
        self.address_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        # Упаковать элементы Frame.
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Войти в главный цикл tkinter.
        tkinter.mainloop()

    # Определить функцию show_info.
    def show_info(self):
        self.value.set('Стивен Маркус\n274 Бейли\n' \
                       'Уэйнзвилль, Северная Каролина 27999')

# Создать экземпляр ShowInfoGUI
show_info = ShowInfoGUI()