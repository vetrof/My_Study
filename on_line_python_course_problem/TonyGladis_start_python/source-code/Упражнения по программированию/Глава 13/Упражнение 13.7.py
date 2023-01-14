# Упражнение по программированию 13.7

# Междугородные звонки

import tkinter
from tkinter.ttk import *
import tkinter.messagebox

class LongDistanceGUI:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать рамки.
        self.top_frame = Frame(self.main_window)
        self.mid_frame = Frame(self.main_window)
        self.bottom_frame = Frame(self.main_window)

        # Создать переменную для использования с радиокнопками.
        self.rb_var = tkinter.IntVar()
       
        # Присвоить переменной 1.
        self.rb_var.set(1)
        
        # Создать элементы Radiobutton в верхней рамке.
        self.rb1 = Radiobutton(self.top_frame, 
                               text = 'Дневное время (6:00 - 17:59)',
                               variable = self.rb_var, value = 1)
        self.rb2 = Radiobutton(self.top_frame,
                               text = 'Вечернее время (18:00 - 23:59)', 
                               variable = self.rb_var, value = 2)
        self.rb3 = Radiobutton(self.top_frame, 
                               text = 'Непиковый период (00:00 - 5:59)',                               
                               variable = self.rb_var, value = 3)

        # Упаковать элементы Radiobutton.
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        # Создать элементы интерфейса для средней рамки.
        self.minutes_label = Label(self.mid_frame, 
                                   text = 'Введите количество минут:')
        self.minutes_entry = Entry(self.mid_frame, width = 10)

        # Упаковать элементы в рамке value_frame.
        self.minutes_label.pack(side = 'left')
        self.minutes_entry.pack(side = 'left')

        # Создать две кнопки в нижней рамке.
        self.display_button = Button(self.bottom_frame, 
                                     text = 'Показать стоимость', 
                                     command = self.calculate)
        self.quit_button = Button(self.bottom_frame, 
                                  text = 'Выйти', 
                                  command = self.main_window.destroy)
              
        # Упаковать элементы в нижней рамке.
        self.display_button.pack(side='left')
        self.quit_button.pack(side='left')
                
        # Упаковать рамки.
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # Войти в главный цикл tkinter.
        tkinter.mainloop()

    # Определить функцию calculate.
    def calculate(self):
        # Получить введенное значение.
        self.minutes = float(self.minutes_entry.get())

        # Определить тариф на основе выбранной радиокнопки.
        if self.rb_var.get() == 1:
            self.rate = 10.0
        if self.rb_var.get() == 2:
            self.rate = 12.0
        if self.rb_var.get() == 3:
            self.rate = 5.0
            
        # Вычислить стоимость.
        self.charges = self.minutes * self.rate

        # Показать информационное окно.
        tkinter.messagebox.showinfo('Общая стоимость', 
                                    'Ваши затраты = ' + \
                                    format(self.charges,',.2f') + ' руб.')
              
# Создать экземпляр LongDistanceGUIю
long_dist = LongDistanceGUI()