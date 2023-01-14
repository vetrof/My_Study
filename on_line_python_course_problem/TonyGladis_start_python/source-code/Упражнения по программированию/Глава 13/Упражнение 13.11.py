# Упражнение по программированию 13.11

# Контур транспортного средства 

import tkinter

# Именованные константы
CANVAS_WIDTH = 410
CANVAS_HEIGHT = 300
X1 = 10
Y1 = 250
X2 = 10
Y2 = 150
X3 = 100
Y3 = 140
X4 = 120
Y4 = 80
X5 = 200
Y5 = 80
X6 = 200
Y6 = 140
X7 = 400
Y7 = 140
X8 = 400
Y8 = 250
X9 = 350
Y9 = 250
X10 = 340
Y10 = 220
X11 = 300
Y11 = 220
X12 = 290
Y12 = 250
X13 = 110
Y13 = 250
X14 = 100
Y14 = 220
X15 = 60
Y15 = 220
X16 = 50
Y16 = 250
BTIRE_X1 = 290
BTIRE_Y1 = 210
BTIRE_X2 = 350
BTIRE_Y2 = 270
FTIRE_X1 = 50
FTIRE_Y1 = 210
FTIRE_X2 = 110
FTIRE_Y2 = 270

class MyGUI:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать элемент интерфейса Canvas.
        self.canvas = tkinter.Canvas(self.main_window, 
		                             width=CANVAS_WIDTH,
                                     height=CANVAS_HEIGHT)

        # Нарисовать контур транспортного средства
        self.canvas.create_polygon(X1, Y1, X2, Y2, X3, Y3, X4, Y4, X5, Y5,
                                   X6, Y6, X7, Y7, X8, Y8, X9, Y9, X10, Y10,
                                   X11, Y11, X12, Y12, X13, Y13, X14, Y14,
                                   X15, Y15, X16, Y16)

        # Нарисовать заднюю шину.
        self.canvas.create_oval(BTIRE_X1, BTIRE_Y1, BTIRE_X2, BTIRE_Y2)

        # Нарисовать переднюю шину.
        self.canvas.create_oval(FTIRE_X1, FTIRE_Y1, FTIRE_X2, FTIRE_Y2)

        # Упаковать холст.
        self.canvas.pack()
        
        # Запустить главный цикл.
        tkinter.mainloop()

# Создать экземпляр класса MyGUI.
my_gui = MyGUI()