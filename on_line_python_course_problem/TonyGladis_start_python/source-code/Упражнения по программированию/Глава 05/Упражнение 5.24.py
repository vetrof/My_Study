# Упражнение по программированию 5.24

# Черепашья графика: прямоугольный узор

import turtle

# Именованные константы
ANIMATION_SPEED = 0
BASE_X = 0
BASE_Y = 0

def rectangle(x, y, width, height, color):
    turtle.setheading(0)
    turtle.fillcolor(color)     # Задать цвет заполнения
    turtle.penup()              # Поднять перо
    turtle.goto(x, y)           # Переместить в указанную позицию
    turtle.pendown()            # Опустить перо
    
    # Начертить прямоугольник.
    turtle.begin_fill()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.end_fill()

def rectangular_pattern(width, height):
    # Узор состоит из 3 вложенных прямоугольников, в которых
    # диагональные отрезки соединяют углы и четыре стороны.
	
    # Начертить самый внешний прямоугольник.
    rectangle(BASE_X, BASE_Y, width, height, 'white')

    # Начертить средний прямоугольник.
    middle_x = BASE_X + width / 8
    middle_y = BASE_Y + height / 8
    middle_width = width - width / 4
    middle_height = height - height / 4
    rectangle(middle_x, middle_y, middle_width, middle_height, 'white')

    # Начертить самый внутренний прямоугольник.
    inner_x = BASE_X + width / 4
    inner_y = BASE_Y + height / 4
    inner_width = width - width / 2
    inner_height = height - height / 2
    rectangle(inner_x, inner_y, inner_width, inner_height, 'black')

    # Начертить диагональные соединяющие отрезки.
    turtle.penup()
    turtle.goto(BASE_X, BASE_Y)
    turtle.pendown()
    turtle.goto(inner_x, inner_y)

    turtle.penup()
    turtle.goto(BASE_X + width, BASE_Y + height)
    turtle.pendown()
    turtle.goto(inner_x + inner_width, inner_y + inner_height)

    turtle.penup()
    turtle.goto(BASE_X + width, BASE_Y)
    turtle.pendown()
    turtle.goto(inner_x + inner_width, inner_y)

    turtle.penup()
    turtle.goto(BASE_X, BASE_Y + height)
    turtle.pendown()
    turtle.goto(inner_x, inner_y + inner_height)

    # Начертить горизонтальные соединяющие отрезки.
    turtle.penup()
    turtle.goto(BASE_X, BASE_Y + height / 2)
    turtle.pendown()
    turtle.goto(inner_x, BASE_Y + height / 2)

    turtle.penup()
    turtle.goto(BASE_X + width, BASE_Y + height / 2)
    turtle.pendown()
    turtle.goto(inner_x + inner_width, BASE_Y + height / 2)

    # Начертить вертикальные соединяющие отрезки.
    turtle.penup()
    turtle.goto(BASE_X + width / 2, BASE_Y)
    turtle.pendown()
    turtle.goto(BASE_X + width / 2, inner_y)

    turtle.penup()
    turtle.goto(BASE_X + width / 2, BASE_Y + height)
    turtle.pendown()
    turtle.goto(BASE_X + width / 2, inner_y + inner_height)

def main():
    turtle.speed(ANIMATION_SPEED)
    turtle.hideturtle()
    w = int(input('Введите ширину: '))
    h = int(input('Введите высоту: '))
    rectangular_pattern(w, h)

    # Не закрывать окно.
    turtle.done()

# Вызвать главную функцию
main()