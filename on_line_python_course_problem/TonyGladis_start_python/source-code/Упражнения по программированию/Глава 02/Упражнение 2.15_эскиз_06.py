# Эскиз 6

import turtle

# Именованные константы
UPPER_LEFT_X = -100
UPPER_LEFT_Y = 100
UPPER_RIGHT_X = 100
UPPER_RIGHT_Y = 100
LOWER_LEFT_X = -100
LOWER_LEFT_Y = -100
LOWER_RIGHT_X = 100
LOWER_RIGHT_Y = -100
CENTER_X = 0
CENTER_Y = 0
GAP = 20

# Спрятать черепаху и задать скорость анимации.
turtle.hideturtle()
turtle.speed(0)

# Начертить сплошные линии.
turtle.penup()
turtle.goto(UPPER_LEFT_X, UPPER_LEFT_Y)
turtle.pendown()
turtle.goto(LOWER_RIGHT_X, LOWER_RIGHT_Y)
turtle.penup()
turtle.goto(UPPER_RIGHT_X, UPPER_RIGHT_Y)
turtle.pendown()
turtle.goto(LOWER_LEFT_X, LOWER_LEFT_Y)
turtle.penup()
turtle.goto(UPPER_LEFT_X, UPPER_LEFT_Y)
turtle.pendown()
turtle.goto(LOWER_LEFT_X, LOWER_LEFT_Y)
turtle.penup()
turtle.goto(UPPER_RIGHT_X, UPPER_RIGHT_Y)
turtle.pendown()
turtle.goto(LOWER_RIGHT_X, LOWER_RIGHT_Y)

# Начертить верхнюю пунктирную линию.
turtle.penup()
turtle.goto(UPPER_LEFT_X, UPPER_LEFT_Y)
turtle.pendown()
turtle.forward(GAP)
turtle.penup()
turtle.forward(GAP)
turtle.pendown()
turtle.forward(GAP)
turtle.penup()
turtle.forward(GAP)
turtle.pendown()
turtle.forward(GAP)
turtle.penup()
turtle.forward(GAP)
turtle.pendown()
turtle.forward(GAP)
turtle.penup()
turtle.forward(GAP)
turtle.pendown()
turtle.forward(GAP)
turtle.penup()
turtle.forward(GAP)

# Начертить нижнюю пунктирную линию.
turtle.penup()
turtle.goto(LOWER_LEFT_X, LOWER_LEFT_Y)
turtle.pendown()
turtle.forward(GAP)
turtle.penup()
turtle.forward(GAP)
turtle.pendown()
turtle.forward(GAP)
turtle.penup()
turtle.forward(GAP)
turtle.pendown()
turtle.forward(GAP)
turtle.penup()
turtle.forward(GAP)
turtle.pendown()
turtle.forward(GAP)
turtle.penup()
turtle.forward(GAP)
turtle.pendown()
turtle.forward(GAP)
turtle.penup()
turtle.forward(GAP)

# Начертить точки.
turtle.penup()
turtle.goto(UPPER_LEFT_X, UPPER_LEFT_Y)
turtle.dot()
turtle.goto(UPPER_RIGHT_X, UPPER_RIGHT_Y)
turtle.dot()
turtle.goto(LOWER_LEFT_X, LOWER_LEFT_Y)
turtle.dot()
turtle.goto(LOWER_RIGHT_X, LOWER_RIGHT_Y)
turtle.dot()
turtle.goto(CENTER_X, CENTER_Y)
turtle.dot()