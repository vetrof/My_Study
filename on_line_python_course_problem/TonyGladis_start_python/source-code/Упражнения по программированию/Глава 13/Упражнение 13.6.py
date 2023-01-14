# Упражнение по программированию 13.6

# Авторемонтная фирма "Автоцех"

import tkinter
from tkinter.ttk import *
import tkinter.messagebox

class AutoGUI:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать рамки.
        self.top_frame = Frame(self.main_window)
        self.bottom_frame = Frame(self.main_window)

        # Создать переменные для использования с элементами Checkbuttons.
        self.cb_oil_var = tkinter.IntVar()
        self.cb_lube_var = tkinter.IntVar()
        self.cb_radiator_var = tkinter.IntVar()
        self.cb_trans_var = tkinter.IntVar()
        self.cb_inspection_var = tkinter.IntVar()
        self.cb_muffler_var = tkinter.IntVar()
        self.cb_tire_var = tkinter.IntVar()
       
        # Присвоить переменным значение 0.
        self.cb_oil_var.set(0)
        self.cb_lube_var.set(0)
        self.cb_radiator_var.set(0)
        self.cb_trans_var.set(0)
        self.cb_inspection_var.set(0)
        self.cb_muffler_var.set(0)
        self.cb_tire_var.set(0)
        
        # Создать флаговые кнопки Checkbutton в верхней рамке.
        self.cb1 = Checkbutton(self.top_frame, 
                               text= 'Замена масла - 500 руб.',
                               variable = self.cb_oil_var)
        self.cb2 = Checkbutton(self.top_frame, 
                               text = 'Смазочные работы - 300 руб.',
                               variable = self.cb_lube_var)
        self.cb3 = Checkbutton(self.top_frame, 
                               text='Промывка радиатора - 700 руб.',
                               variable = self.cb_radiator_var)
        self.cb4 = Checkbutton(self.top_frame, 
                               text='Замена жидкости в трансмиссии - 1000 руб.',
                               variable = self.cb_trans_var)
        self.cb5 = Checkbutton(self.top_frame, 
                               text= 'Осмотр - 800 руб.',
                               variable = self.cb_inspection_var)
        self.cb6 = Checkbutton(self.top_frame, 
                               text='Замена глушителя выхлопа - 1300 руб.',
                               variable = self.cb_muffler_var)
        self.cb7 = Checkbutton(self.top_frame, 
                               text = 'Перестановка шин - 1300 руб.',
                               variable = self.cb_tire_var) 
      
        # Упаковать элементы Checkbutton.
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()
       
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
        self.bottom_frame.pack()

        # Войти в главный цикл tkinter.
        tkinter.mainloop()

    # Определить функцию show_info.
    def calculate(self):
        # Создать переменную для итоговой суммы.
        self.total = 0.0
        
        # Определить общую стоимость на основе выбранных флаговых кнопок.
        if self.cb_oil_var.get() == 1:
            self.total += 500.0
        if self.cb_lube_var.get() == 1:
            self.total += 300.0
        if self.cb_radiator_var.get() == 1:
            self.total += 700.0
        if self.cb_trans_var.get() == 1:
            self.total += 1000.0
        if self.cb_inspection_var.get() == 1:
            self.total += 800.0
        if self.cb_muffler_var.get() == 1:
            self.total += 1300.0
        if self.cb_tire_var.get() == 1:
            self.total += 1300.0
                
        # Показать информационное окно.
        tkinter.messagebox.showinfo('Общая стоимость', 
                                    'Ваши затраты = ' + \
                                    format(self.total,',.2f') + ' руб.')

# Создать экземпляр AutoGUI.
auto = AutoGUI()