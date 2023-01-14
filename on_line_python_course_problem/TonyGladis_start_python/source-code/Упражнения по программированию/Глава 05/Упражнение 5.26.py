# Упражнение по программированию 5.26

# Черепашья графика: городской силуэт 

import turtle
import random

# Именованные константы
ANIMATION_SPEED = 0
SCREEN_WIDTH = 500                  # Ширина экрана
SCREEN_HEIGHT = 500                 # Высота экрана
NUM_STARS = 20                      # Количество рисуемых звезд
MIN_X = -(int(SCREEN_WIDTH / 2))    # Минимальная координата x на экране
MAX_X = int((SCREEN_WIDTH / 2) - 1) # Максимальная координата x на экране
MIN_Y = -(int(SCREEN_HEIGHT / 2))   # Минимальная координата y на экране
MAX_Y = int(SCREEN_HEIGHT / 2)      # Максимальная координата y на экране

X1 = MIN_X          # Координата x начала горизонта
Y1 = -50            # Координата y начала горизонта

WINDOW_SIZE = 10    # Размер квадратного окна
WX1 = -160          # Координата x окна 1
WY1 = 10            # Координата y окна 1 
WX2 = -100          # Координата x окна 2
WY2 = 170           # Координата y окна 2
WX3 = -100          # Координата x окна 3
WY3 = 150           # Координата y окна 3
WX4 = -60           # Координата x окна 4
WY4 = 100           # Координата y окна 4
WX5 = -80           # Координата x окна 5
WY5 = -20           # Координата y окна 5
WX6 = 30            # Координата x окна 6
WY6 = 90            # Координата y окна 6

# Функция square чертить квадрат.
# Параметры x и y являются координатами левого нижнего угла.
# Параметр width является шириной каждой стороны.
# Параметр color является цветом заполнения, как строковое значение.

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

def screen_setup():
	# Настроить экран
    turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    turtle.speed(ANIMATION_SPEED)
    turtle.hideturtle()
    turtle.bgcolor('black')

def draw_stars():
    # Нарисовать звезды
    turtle.pencolor('white')
    for count in range(NUM_STARS):
        x = random.randint(MIN_X, MAX_X)
        y = random.randint(MIN_Y, MAX_Y)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.dot()
    
def draw_buildings():
    # Нарисовать здания
    turtle.pencolor('gray')
    turtle.fillcolor('gray')
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(X1, Y1)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(180)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(70)
    # Перейти в правый угол экрана.
    turtle.goto(MAX_X, turtle.ycor())
    # Закрыть фигуру.
    turtle.goto(MAX_X, MIN_Y)
    turtle.goto(MIN_X, MIN_Y)
    turtle.goto(X1, Y1)
    turtle.end_fill()

def draw_windows():
	# Нарисовать окна
    square(WX1, WY1, WINDOW_SIZE, 'white')
    square(WX2, WY2, WINDOW_SIZE, 'white')
    square(WX3, WY3, WINDOW_SIZE, 'white')
    square(WX4, WY4, WINDOW_SIZE, 'white')
    square(WX5, WY5, WINDOW_SIZE, 'white')
    square(WX6, WY6, WINDOW_SIZE, 'white')
    
def main():
    screen_setup()
    draw_stars()
    draw_buildings()
    draw_windows()

    # Не закрывать окно.
    turtle.done()

# Вызвать главную функцию
main()
