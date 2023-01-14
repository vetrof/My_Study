# Упражнение по программированию 13.2

# Переводчик с латинского

import tkinter
from tkinter.ttk import *

class LatinTranslatorGUI:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать две рамки.
        self.top_frame = Frame(self.main_window)
        self.bottom_frame = Frame(self.main_window)
        
        # Создать пустое поле в верхней рамке.
        self.value = tkinter.StringVar()
        self.word_label = Label(self.top_frame, 
                                textvariable= self.value)
                                            
        # Создать кнопки в нижней рамке.
        self.sinister_button = Button(self.bottom_frame, 
                                      text = 'sinister', 
                                      command = self.show_word1)
        self.dexter_button = Button(self.bottom_frame, 
                                    text = 'dexter', 
                                    command = self.show_word2)
        self.medium_button = Button(self.bottom_frame,
                                    text = 'medium', 
                                    command = self.show_word3)                
        # Упаковать элемент Label.
        self.word_label.pack()
        
        # Упаковать элементы Button.
        self.sinister_button.pack(side = 'left')
        self.dexter_button.pack(side = 'left')
        self.medium_button.pack(side = 'left')

        # Упаковать элементы Frame.
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Войти в главный цикл tkinter.
        tkinter.mainloop()

    # Определить функцию show_word.
    def show_word1(self):
        self.value.set('левый')
    def show_word2(self):
        self.value.set('правый')
    def show_word3(self):
        self.value.set('центральный')

# Создать экземпляр LatinTranslatorGUI.
latin_translator = LatinTranslatorGUI()