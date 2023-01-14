# Упражнение по программированию 13.10

# Голливудская звезда 

import tkinter

# Именованные константы.
CANVAS_WIDTH = 100
CANVAS_HEIGHT = 100
X1 = 50
Y1 = 1
X2 = 20
Y2 = 91
X3 = 97
Y3 = 35
X4 = 2
Y4 = 35
X5 = 79
Y5 = 91
TEXT_X = 50
TEXT_Y = 35

class MyGUI:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать элемент интерфейса Canvas.
        self.canvas = tkinter.Canvas(self.main_window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)

        # Нарисовать звезду.
        self.canvas.create_polygon(X1, Y1, X2, Y2, X3, Y3, X4, Y4, X5, Y5, fill='white')

        # Написать имя
        self.canvas.create_text(TEXT_X, TEXT_Y, text='Ваше имя',
                                anchor= tkinter.N, fill='black')
        
        # Упаковать холст.
        self.canvas.pack()
        
        # Запустить главный цикл.
        tkinter.mainloop()

# Создать экземпляр класса MyGUI.
my_gui = MyGUI()