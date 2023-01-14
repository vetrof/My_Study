import turtle

# Именованные константы для точек треугольника
TOP_X = 0
TOP_Y = 100
BASE_LEFT_X  = -100
BASE_LEFT_Y  = -100
BASE_RIGHT_X =  100
BASE_RIGHT_Y = -100

def main():
    turtle.hideturtle()
    line(TOP_X, TOP_Y, BASE_LEFT_X, BASE_LEFT_Y, 'red')
    line(TOP_X, TOP_Y, BASE_RIGHT_X, BASE_RIGHT_Y, 'blue')
    line(BASE_LEFT_X, BASE_LEFT_Y, BASE_RIGHT_X, BASE_RIGHT_Y, 'green')

# Функция line рисует отрезок от (startX, startY) до (endX, endY).
# Параметр color – это цвет отрезка.
def line(startX, startY, endX, endY, color):
    turtle.penup()               # Поднять перо
    turtle.goto(startX, startY)  # Переместить в начальную точку
    turtle.pendown()             # Опустить перо
    turtle.pencolor(color)       # Задать цвет заливки
    turtle.goto(endX, endY)      # Нарисовать треугольник

# Вызвать главную функцию.
main()