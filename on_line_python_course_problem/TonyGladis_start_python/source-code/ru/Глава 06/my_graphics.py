# Функции черепашьей графики
import turtle

# Функция square рисует квадрат. 
# Параметры x и y - это координаты левого нижнего угла. 
# Параметр width - это ширина стороны квадрата. 
# Параметр color - это цвет заливки в виде строки.

def square(x, y, width, color):
    turtle.penup()             # Поднять перо
    turtle.goto(x, y)          # Переместить в указанное место
    turtle.fillcolor(color)    # Установить цвет заливки
    turtle.pendown()           # Опустить перо
    turtle.begin_fill()        # Начать заливку
    for count in range(4):     # Нарисовать квадрат
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()          # Закончить заливку

# Функция circle рисует круг. 
# Параметры x и y - это координаты центральной точки.
# Параметр radius - это радиус круга. 
# Параметр color - это цвет заливки в виде строки.

def circle(x, y, radius, color):
    turtle.penup()              # Поднять перо
    turtle.goto(x, y - radius)  # Спозиционировать черепаху
    turtle.fillcolor(color)     # Установить цвет заливки
    turtle.pendown()            # Опустить перо
    turtle.begin_fill()         # Начать заливку
    turtle.circle(radius)       # Нарисовать круг
    turtle.end_fill()           # Закончить заливку

# Функция line рисует линию от (startX, startY) до (endX, endY).
# Параметр color – это цвет линии.

def line(startX, startY, endX, endY, color):
    turtle.penup()               # Поднять перо
    turtle.goto(startX, startY)  # Переместить в начальную точку
    turtle.pendown()             # Опустить перо
    turtle.pencolor(color)       # Установить цвет заливки
    turtle.goto(endX, endY)      # Нарисовать треугольник