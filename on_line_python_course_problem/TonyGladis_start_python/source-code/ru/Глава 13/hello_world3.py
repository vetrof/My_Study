# Эта программа изпользует аргумент side='left' в
# методе pack для изменения размещения виджетов.

import tkinter

class MyGUI:
    def __init__(self):
        # Создать виджет главного окна.
        self.main_window = tkinter.Tk()

        # Создать два виджета Label.
        self.label1 = tkinter.Label(self.main_window,
                                    text='Привет, мир!')
        self.label2 = tkinter.Label(self.main_window,
                        text='Это моя программа с GUI.')

        # Вызвать метод pack обоих виджетов Label.
        self.label1.pack(side='left')
        self.label2.pack(side='left')

        # Войти в главный цикл tkinter.
        tkinter.mainloop()

# Создать экземпляр класса MyGUI.
if __name__ == '__main__':
    my_gui = MyGUI()