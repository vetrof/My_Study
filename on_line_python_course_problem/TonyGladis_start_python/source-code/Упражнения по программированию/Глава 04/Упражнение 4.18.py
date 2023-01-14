# Упражнение по программированию 4.18

# Черепашья графика: гипнотический узор

import turtle

# Именованные константы
ANIMATION_SPEED = 0
NUM_LINES = 50
STARTING_LENGTH = 1
ENDING_LENGTH = 500
STEP = 10
ANGLE = 90

# Инициализировать черепаху.
turtle.hideturtle()
turtle.speed(ANIMATION_SPEED)

# Начертить линии.
for x in range(STARTING_LENGTH, ENDING_LENGTH, STEP):
    turtle.forward(x)
    turtle.left(ANGLE)
turtle.done()