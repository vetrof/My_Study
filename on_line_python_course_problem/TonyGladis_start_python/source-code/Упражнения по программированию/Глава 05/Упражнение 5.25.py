# Упражнение по программированию 5.25

# Черепашья графика: шахматная доска

import turtle

# Именованные константы
ANIMATION_SPEED = 0
SCREEN_WIDTH = 500
SCREEN_HEIGHT = SCREEN_WIDTH
NUM_SQUARES_IN_A_ROW = 5
NUM_SQUARES_IN_A_COL = 5
SQUARE_WIDTH = int(SCREEN_WIDTH / NUM_SQUARES_IN_A_ROW)
SCREEN_LEFT_EDGE_X = int(-(SCREEN_WIDTH / 2))
SCREEN_TOP_EDGE_Y = int(SCREEN_HEIGHT / 2)
FIRST_X = SCREEN_LEFT_EDGE_X
LAST_X = FIRST_X + (NUM_SQUARES_IN_A_ROW * SQUARE_WIDTH)
FIRST_Y = SCREEN_TOP_EDGE_Y - SQUARE_WIDTH
LAST_Y = FIRST_Y - (NUM_SQUARES_IN_A_COL * SQUARE_WIDTH)


# Функция square чертит квадрат. Параметры x и y являются
# координатами левого нижнего угла. Параметр width
# является шириной каждой стороны. Параметр color является
# цветом заполнения, как строковое значение.

def square(x, y, width, color):
    turtle.penup()            # Поднять перо
    turtle.goto(x, y)         # Переместить в указанную позицию
    turtle.fillcolor(color)   # Задать цвет заполнения
    turtle.pendown()          # Опустить перо
    turtle.begin_fill()       # Начать заполнение
    for count in range(4):    # Начертить квадрат
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()         # Завершить заполнение

def main():
    turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    turtle.speed(ANIMATION_SPEED)
    turtle.hideturtle()
    color = 'black'

    for y in range(FIRST_Y, LAST_Y, -SQUARE_WIDTH):
        for x in range(FIRST_X, LAST_X, SQUARE_WIDTH):
            square(x, y, SQUARE_WIDTH, color)
            if color == 'black':
                color = 'white'
            else:
                color = 'black'

    # Не закрывать окно.
    turtle.done()

# Вызвать главную функцию
main()