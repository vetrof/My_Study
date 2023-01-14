# Упражнение по программированию 4.19

# Черепашья графика: знак 'Stop'

import math
import turtle

# Именованные константы
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10

# Размер окна.
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

# Вычислить диаметр шестиугольника, чтобы его
# можно было центрировать в графическом окне.
#                s
#        ---------------
#       / |             \
#  s   /  |              \
#     /   | x             \  s
#    /    |                \
#   |------                 |
#   |   x                   |
#   |                       |
#   Чтобы получить диаметр:
#     diameter = s + 2 * x
#   Мы знаем, что s равняется 100.
#   Применить теорему Пифагора, чтобы получить x:
#   s^2 = x^2 + x^2
#   s^2 = 2*x^2
#   x = s / sqrt(2)
s = LENGTH
x = s / math.sqrt(2)
diameter = s + (2 * x)

# Инициализировать черепаху.
turtle.penup()
turtle.hideturtle()
turtle.speed(ANIMATION_SPEED)

# Переместить черепаху в исходную точку.
starting_x = (0 - (diameter / 2)) + ((WINDOW_WIDTH - diameter) / 2)
starting_y = (s / 2) + x
turtle.goto(starting_x, starting_y)
turtle.pendown()

# Начертить шестиугольник.
for x in range(NUM_SIDES):
    turtle.forward(LENGTH)
    turtle.right(ANGLE)

# Показать надпись 'STOP'
turtle.penup()
turtle.goto(TEXT_X, TEXT_Y)
turtle.pendown()
turtle.write('STOP')
turtle.done()