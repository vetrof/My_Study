# Эскиз 2

import turtle

# Именованные константы
OUTER_TOP_X = 0
OUTER_TOP_Y = 200
INNER_TOP_X = OUTER_TOP_X
INNER_TOP_Y = OUTER_TOP_Y / 2
BASE_LEFT_X = -100
BASE_LEFT_Y = 0
BASE_RIGHT_X = 100
BASE_RIGHT_Y = 0

# Спрятать черепаху и поднять перо.
turtle.hideturtle()
turtle.penup()

# Переместить перо в правый нижний угол.
turtle.goto(BASE_RIGHT_X, BASE_RIGHT_Y)

# Сделать цвет заполнения синим и опустить перо.
turtle.fillcolor('blue')
turtle.pendown()

# Начертить внешний треугольник.
turtle.goto(OUTER_TOP_X, OUTER_TOP_Y)
turtle.goto(BASE_LEFT_X, BASE_LEFT_Y)
turtle.goto(BASE_RIGHT_X, BASE_RIGHT_Y)

# Начертить внутренний треугольник.
turtle.begin_fill()
turtle.goto(INNER_TOP_X, INNER_TOP_Y)
turtle.goto(BASE_LEFT_X, BASE_LEFT_Y)
turtle.goto(BASE_RIGHT_X, BASE_RIGHT_Y)
turtle.end_fill()