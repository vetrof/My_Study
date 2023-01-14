# Упражнение по программированию 13.4

# Из шкалы Цельсия в шкалу Фаренгейта

import tkinter
from tkinter.ttk import *

class CelsiusGUI:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать рамки.
        self.top_frame = Frame(self.main_window)
        self.mid_frame = Frame(self.main_window)
        self.bottom_frame = Frame(self.main_window)

        # Создать элементы интерфейса для верхней рамки.
        self.celsius_label = Label(self.top_frame,
                                   text = 'Введите температуру в градусах Цельсия:')
        self.celsius_entry = Entry(self.top_frame, width = 10)

        # Упаковать элементы верхней рамки.
        self.celsius_label.pack(side = 'left')
        self.celsius_entry.pack(side = 'left')

        # Создать элементы интерфейса для средней рамки.
        self.results_label = Label(self.mid_frame,
                                   text = 'Температура по шкале Фаренгейта: ')
                  
        # Создасть пустое поле.
        self.fahr = tkinter.StringVar()
        self.fahrenheit_label = Label(self.mid_frame, 
                                      textvariable= self.fahr)

        # Упаковать элементы средней рамки.
        self.results_label.pack(side = 'left')
        self.fahrenheit_label.pack(side = 'left')
                                                           
        # Создать две кнопки в нижней рамке.
        self.fahrenheit_button = Button(self.bottom_frame,
                                        text = 'Преобразовать в градусы Фаренгейта',
                                        command = self.convert)
        self.quit_button = Button(self.bottom_frame,
                                  text = 'Выйти',
                                  command = self.main_window.destroy)

        # Упаковать элементы нижней рамки.
        self.fahrenheit_button.pack(side='left')
        self.quit_button.pack(side='left')
                
        # Упаковать рамки.
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # Войти в главный цикл tkinter.
        tkinter.mainloop()

    # Определить функцию show_info.
    def convert(self):
        # Получить введенные значения.
        self.celsius = float(self.celsius_entry.get())

        # Вычислить градусы Фаренгейта.
        self.fahrenheit = 9.0 /5.0 * float(self.celsius) + 32

        # Обновить поле fahrenheit_label.
        self.fahr.set(self.fahrenheit)
        
# Создать экземпляр MilesGUI.
celsius = CelsiusGUI()