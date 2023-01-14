# Эскиз 1

import turtle

# Спрятать черепаху.
turtle.hideturtle()

# Сделать цвет заполнения синим.
turtle.fillcolor('blue')

# Начертить первый ромб.
turtle.begin_fill()
turtle.left(135)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.end_fill()

# Начертить второй ромб.
turtle.begin_fill()
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.end_fill()