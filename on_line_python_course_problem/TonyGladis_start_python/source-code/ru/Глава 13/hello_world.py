# Эта программа показывает надпись с текстом.

import tkinter

class MyGUI:
    def __init__(self):
        # Создать виджет главного окна.
        self.main_window = tkinter.Tk()

        # Создать виджет Label, содержащий
        # надпись 'Привет, Мир!'
        self.label = tkinter.Label(self.main_window,
                                   text='Привет, мир!')

        # Вызвать метод pack виджета Label.
        self.label.pack()

        # Войти в главный цикл tkinter.
        tkinter.mainloop()

# Создать экземпляр класса MyGUI.
if __name__ == '__main__':
    my_gui = MyGUI() 