# Упражнение по программированию 4.17

# Черепашья графика: звездочный узор

import turtle

# Именованные константы
INITIAL_ANGLE = 45
ANGLE_STEP = 135
NUM_LINES = 8
LENGTH = 200
ANIMATION_SPEED = 0

# Инициализировать черепаху.
turtle.hideturtle()
turtle.speed(ANIMATION_SPEED)
turtle.left(INITIAL_ANGLE)

# Начертить линии.
for count in range(NUM_LINES):
    turtle.forward(LENGTH)
    turtle.left(ANGLE_STEP)
turtle.done()