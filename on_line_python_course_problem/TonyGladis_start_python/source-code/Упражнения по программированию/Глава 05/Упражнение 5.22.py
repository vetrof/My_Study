# Упражнение по программированию 5.22

# Черепашья графика: функция рисования треугольника

import turtle

def triangle(x1, y1, x2, y2, x3, y3, color):
    # Задать цвет заполнения.
    turtle.fillcolor(color)
    
    # Поднять перо и переместить черепаху.
    turtle.penup()
    turtle.goto(x1, y1)

    # Начертить треугольник.
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.goto(x1, y1)
    turtle.end_fill()

def main():
    # Инициализировать черепаху.
    turtle.hideturtle()
    turtle.speed(0)
    
    # Начертить три треугольника.
    triangle(0, 0, 100, 0, 0, -100, 'red')
    triangle(0, 0, -100, 0, 0, -100, 'green')
    triangle(0, -100, -100, -200, 100, -200, 'blue')

    # Не закрывать окно.
    turtle.done()

# Вызвать главную функцию
main()