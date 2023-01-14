# Упражнение по программированию 13.3

# Калькулятор миль на галлон бензина 

import tkinter
from tkinter.ttk import *

class MilesGUI:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать четыре рамки.
        self.gallons_frame = Frame(self.main_window)
        self.miles_frame = Frame(self.main_window)
        self.mpg_frame = Frame(self.main_window)
        self.bottom_frame = Frame(self.main_window)

        # Создать элементы интерфейса для рамки gallons_frame.
        self.gallons_label = Label(self.gallons_frame, 
                              text = 'Введите количество галлонов:')
        self.gallons_entry = Entry(self.gallons_frame, width = 10)

        # Упаковать элементы рамки gallons_frame.
        self.gallons_label.pack(side = 'left')
        self.gallons_entry.pack(side = 'left')

        # Упаковать элементы рамки miles_frame.
        self.miles_label = Label(self.miles_frame, 
                            text = 'Введите количество миль:')
        self.miles_entry = Entry(self.miles_frame, width = 10)                                 

        # Упаковать элементы рамки miles_frame.
        self.miles_label.pack(side ='left')
        self.miles_entry.pack(side = 'left')
        
        # Создать элементы интерфейса для поля result_label.
        self.result_label = Label(self.mpg_frame,
                             text = 'Мили на галлон (MPG) = ')
        
        # Создать пустое поле.
        self.mpg = tkinter.StringVar()
        self.mpg_label = Label(self.mpg_frame,
                               textvariable= self.mpg)
        # Упаковать элементы интерфейса для рамки.
        self.result_label.pack(side = 'left')
        self.mpg_label.pack(side = 'left')
                                                           
        # Создать две кнопки в нижней рамке.
        self.mpg_button = Button(self.bottom_frame, 
                                 text = 'Вычислить MPG', 
                                 command = self.calculate_mpg)
        self.quit_button = Button(self.bottom_frame,
                                  text = 'Выйти', 
                                  command = self.main_window.destroy)
              
        # Упаковать элементы интерфейса в нижней рамке.
        self.mpg_button.pack(side='left')
        self.quit_button.pack(side='left')
                
        # Упаковать рамки.
        self.gallons_frame.pack()
        self.miles_frame.pack()
        self.mpg_frame.pack()
        self.bottom_frame.pack()

        # Войти в главный цикл tkinter.
        tkinter.mainloop()

    # Определить функцию show_info.
    def calculate_mpg(self):
        # Получить введенные значения.
        self.gallons = float(self.gallons_entry.get())
        self.miles = float(self.miles_entry.get())

        # Вычислить MPG.
        self.miles_per_gallon = float(self.miles) / self.gallons

        # Обновить поле mpg_label.
        self.mpg.set(self.miles_per_gallon)

# Создать экземпляр MilesGUI.
mpg = MilesGUI()