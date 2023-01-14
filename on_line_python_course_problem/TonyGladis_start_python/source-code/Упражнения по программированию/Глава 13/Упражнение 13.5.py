# Упражнение по программированию 13.5

# Налог на недвижимость 

import tkinter
from tkinter.ttk import *

class PropertyGUI:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать рамки
        self.value_frame = Frame(self.main_window)
        self.assess_frame = Frame(self.main_window)
        self.tax_frame = Frame(self.main_window)
        self.bottom_frame = Frame(self.main_window)

        # Создать элементы интерфейса для рамки value_frame.
        self.value_label = Label(self.value_frame, 
                                 text = 'Введите стоимость имущества: $')
        self.value_entry = Entry(self.value_frame, width = 10)

        # Упаковать элементы рамки value_frame.
        self.value_label.pack(side = 'left')
        self.value_entry.pack(side = 'left')

        # Создать элементы интерфейса для рамки assess_frame.
        self.assess_results_label = Label(self.assess_frame, 
                                          text = 'Оценочная стоимость: ')
                  
        # Создать пустое поле для оценочной стоимости.
        self.assess = tkinter.StringVar()
        self.assess_label = Label(self.assess_frame, 
                                  textvariable= self.assess)

        # Создать элементы интерфейса для рамки assess_frame.
        self.assess_results_label.pack(side = 'left')
        self.assess_label.pack(side = 'left')

        # Создать элементы интерфейса для рамки tax_frame.
        self.tax_results_label = Label(self.tax_frame, 
                                       text = 'Налог на имущество: ')
                  
        # Создать пустое поле для величины налона на имущество.
        self.tax = tkinter.StringVar()
        self.tax_label = Label(self.tax_frame, 
                               textvariable= self.tax)

        # Упаковать элементы рамки tax_frame.
        self.tax_results_label.pack(side = 'left')
        self.tax_label.pack(side = 'left')
                                                           
        # Создать две кнопки в нижней рамке.
        self.display_button = Button(self.bottom_frame, 
                                     text = 'Вычислить', 
                                     command = self.calculate)
        self.quit_button = Button(self.bottom_frame, 
                                  text = 'Выйти', 
                                  command = self.main_window.destroy)
              
        # Упаковать элементы в нижней рамке.
        self.display_button.pack(side='left')
        self.quit_button.pack(side='left')
                
        # Упаковать рамки.
        self.value_frame.pack()
        self.assess_frame.pack()
        self.tax_frame.pack()
        self.bottom_frame.pack()

        # Войти в главный цикл tkinter.
        tkinter.mainloop()

    # Определить функцию show_info.
    def calculate(self):
        # Получить введенные значения.
        self.value = float(self.value_entry.get())

        # Вычислить оценочную стоимость.
        self.assessment = 0.60 * self.value

        # Обновить поле с оценочной стоимостью.
        self.assess.set('$' + str(self.assessment))

        # Вычислить налог.
        self.property_tax = float(self.assessment) / 100 * 0.75
        
        # Обновить поле с налогом.
        self.tax.set('$' + str(self.property_tax))
        
# Создать экземпляр PropertyGUI.
prop = PropertyGUI()