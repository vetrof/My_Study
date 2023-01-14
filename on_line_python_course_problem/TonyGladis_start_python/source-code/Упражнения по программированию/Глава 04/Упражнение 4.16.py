# Упражнение по программированию 4.16

# Черепашья графика: повторение квадратов

import turtle

# Именованные константы
STARTING_X = -4
STARTING_Y = 4
STARTING_SIZE = 8
NUM_SQUARES = 50
STEP = 4
NUM_SIDES = 4
ANGLE = 90
ANIMATION_SPEED = 0

# Задать скорость анимации и спрятать черепаху.
turtle.speed(ANIMATION_SPEED)
turtle.hideturtle()

# Задать исходные координаты x и y, а также исходный размер.
x = STARTING_X
y = STARTING_Y
size = STARTING_SIZE

# Начертить узор.
for count in range(NUM_SQUARES):
    # Спозиционировать черепаху.
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    # Начертить квадрат
    for s in range(NUM_SIDES):
        turtle.forward(size)
        turtle.right(ANGLE)

    # Подготовить следующий квадрат.
    x = x - STEP
    y = y + STEP
    size = size + STEP