# Эскиз 5

import turtle

# Именованные константы
CENTER_X = 0
CENTER_Y = 0
X_AXIS_LENGTH = 200
Y_AXIS_LENGTH = 200
RADIUS = 25
SOUTH = 270
EAST = 0

# Спрятать черепаху и задать скорость анимации.
turtle.hideturtle()
turtle.speed(0)

# Начертить ось X
x = CENTER_X - (X_AXIS_LENGTH / 2)
y = CENTER_Y
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.forward(X_AXIS_LENGTH)

# Начертить ось Y
x = CENTER_X
y = CENTER_Y + (Y_AXIS_LENGTH / 2)
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.setheading(SOUTH)
turtle.forward(X_AXIS_LENGTH)

# Начертить центральный круг
x = CENTER_X
y = CENTER_Y - RADIUS
turtle.penup()
turtle.setheading(EAST)
turtle.goto(x, y)
turtle.pendown()
turtle.circle(RADIUS)

# Написать "Север"
x = CENTER_X - 10
y = CENTER_Y + (Y_AXIS_LENGTH / 2)
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.write("Север")

# Написать "Юг"
x = CENTER_X - 10
y = CENTER_Y - (Y_AXIS_LENGTH / 2) - 10
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.write("Юг")

# Написать "Запад"
x = CENTER_X - (X_AXIS_LENGTH / 2) - 25
y = CENTER_Y - 7
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.write("Запад")

# Написать "Восток"
x = CENTER_X + (X_AXIS_LENGTH / 2) + 2
y = CENTER_Y - 7
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.write("Восток")