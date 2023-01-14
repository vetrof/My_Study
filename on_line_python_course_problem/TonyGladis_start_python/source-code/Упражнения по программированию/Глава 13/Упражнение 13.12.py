# Упражнение по программированию 13.12

# Солнечная система

import tkinter

# Именованные константы.
CANVAS_WIDTH = 520
CANVAS_HEIGHT = 300
SPACING = 10

SUN_X = 60
SUN_Y = 150
SUN_RAD = 50
SUN_COLOR = 'yellow'

MERC_RAD = 10
MERC_X = SUN_X + SUN_RAD + SPACING + MERC_RAD
MERC_Y = 150
MERC_COLOR = 'orange'

VENUS_RAD = 15
VENUS_X = MERC_X + MERC_RAD + SPACING + VENUS_RAD
VENUS_Y = 150
VENUS_COLOR = 'lightblue'

EARTH_RAD = 10
EARTH_X = VENUS_X + VENUS_RAD + SPACING + EARTH_RAD
EARTH_Y = 150
EARTH_COLOR = 'blue'

MARS_RAD = 8
MARS_X = EARTH_X + EARTH_RAD + SPACING + MARS_RAD
MARS_Y = 150
MARS_COLOR = 'red'

JUPITER_RAD = 30
JUPITER_X = MARS_X + MARS_RAD + SPACING + JUPITER_RAD
JUPITER_Y = 150
JUPITER_COLOR = 'brown'

SAT_RAD = 30
SAT_X = JUPITER_X + JUPITER_RAD + SPACING + SAT_RAD
SAT_Y = 150
SAT_COLOR = 'blanched almond'

URN_RAD = 20
URN_X = SAT_X + SAT_RAD + SPACING + URN_RAD
URN_Y = 150
URN_COLOR = 'deep sky blue'

NEP_RAD = 17
NEP_X = URN_X + URN_RAD + SPACING + NEP_RAD
NEP_Y = 150
NEP_COLOR = 'light steel blue'

PLU_RAD = 5
PLU_X = NEP_X + NEP_RAD + SPACING + PLU_RAD
PLU_Y = 150
PLU_COLOR = 'dark olive green'

class MyGUI:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать элемент интерфейса Canvas.
        self.canvas = tkinter.Canvas(self.main_window,
                                     width=CANVAS_WIDTH,
                                     height=CANVAS_HEIGHT)
        # Нарисовать планеты
        self.draw_planet(self.canvas, SUN_X, SUN_Y, SUN_RAD, SUN_COLOR, 'Солнце')
        self.draw_planet(self.canvas, MERC_X, MERC_Y, MERC_RAD, MERC_COLOR, 'Меркурий')
        self.draw_planet(self.canvas, VENUS_X, VENUS_Y, VENUS_RAD, VENUS_COLOR, 'Венера')
        self.draw_planet(self.canvas, EARTH_X, EARTH_Y, EARTH_RAD, EARTH_COLOR, 'Земля')
        self.draw_planet(self.canvas, MARS_X, MARS_Y, MARS_RAD, MARS_COLOR, 'Марс')
        self.draw_planet(self.canvas, JUPITER_X, JUPITER_Y, JUPITER_RAD, JUPITER_COLOR, 'Юпитер')
        self.draw_ringed_planet(self.canvas, SAT_X, SAT_Y, SAT_RAD, SAT_COLOR, 'Сатурн')
        self.draw_planet(self.canvas, URN_X, URN_Y, URN_RAD, URN_COLOR, 'Уран')
        self.draw_planet(self.canvas, NEP_X, NEP_Y, NEP_RAD, NEP_COLOR, 'Петун')
        self.draw_planet(self.canvas, PLU_X, PLU_Y, PLU_RAD, PLU_COLOR, 'Платон')

        # Упаковать холст.
        self.canvas.pack()
        
        # Запустить главный цикл.
        tkinter.mainloop()

    # Метод draw_planet чертит круг с центральной точкой в
    # x,y на холсте. Параметр radius задает радиус круга,
    # параметр color задает цвет заполнения круга.
    def draw_planet(self, canvas, x, y, radius, color, name):
        x1 = int(x) - int(radius)
        y1 = int(y) - int(radius)
        x2 = int(x) + int(radius)
        y2 = int(y) + int(radius)
        canvas.create_oval(x1, y1, x2, y2, fill=color)
        canvas.create_text(x, y2, text=name, anchor=tkinter.N)

    # Метод draw_ringed_planet рисует обведенную кольцом планету.
    def draw_ringed_planet(self, canvas, x, y, radius, color, name):
        # Нарисовать кольцо.
        ring_x1 = int(x) - int(radius) - SPACING
        ring_y1 = int(y) - int(radius) + SPACING
        ring_x2 = int(x) + int(radius) + SPACING
        ring_y2 = int(y) + int(radius) - SPACING
        canvas.create_oval(ring_x1, ring_y1, ring_x2, ring_y2)
        
        # Нарисовать планету.
        self.draw_planet(canvas, x, y, radius, color, name)
        
# Создать экземпляр класса MyGUI.
my_gui = MyGUI()