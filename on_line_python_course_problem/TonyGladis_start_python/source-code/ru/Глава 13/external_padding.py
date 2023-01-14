# Эта программа демонстрирует внешнее заполнение.
import tkinter

class MyGUI:
    def __init__(self):
        # Создать виджет главного окна.
        self.main_window = tkinter.Tk()

        # Создать два виджета Label со сплошными границами.
        self.label1 = tkinter.Label(self.main_window,
                                    text='Привет, мир!',
                                    borderwidth=1,
                                    relief='solid')
 
        self.label2 = tkinter.Label(self.main_window,
                                    text='Это моя программа с GUI.',
                                    borderwidth=1,
                                    relief='solid')

        # Вывести на экран виджеты Label с 20 пикселами 
        # горизонтального внешнего и вертикального внешнего заполнения.
        self.label1.pack(padx=20, pady=20)
        self.label2.pack(padx=20, pady=20)

        # Войти в главный цикл tkinter.
        tkinter.mainloop()

# Создать экземпляр класса MyGUI.
if __name__ == '__main__':
    my_gui = MyGUI()