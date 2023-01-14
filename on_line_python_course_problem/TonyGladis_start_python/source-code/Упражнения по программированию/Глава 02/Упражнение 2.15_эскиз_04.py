# Эскиз 4

import turtle

# Именованные константы
RADIUS = 100
STARTING_POINT_X = -250
STARTING_POINT_Y = 0
HSHIFT = 125
VSHIFT = 100

# Начертить круг #1
x = STARTING_POINT_X
y = STARTING_POINT_Y
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.circle(RADIUS)

# Начертить круг #2
x += HSHIFT
y -= VSHIFT
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.circle(RADIUS)

# Начертить круг #3
x += HSHIFT
y = 0
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.circle(RADIUS)

# Начертить круг #4
x += HSHIFT
y -= VSHIFT
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.circle(RADIUS)

# Начертить круг #5
x += HSHIFT
y = 0
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.circle(RADIUS)