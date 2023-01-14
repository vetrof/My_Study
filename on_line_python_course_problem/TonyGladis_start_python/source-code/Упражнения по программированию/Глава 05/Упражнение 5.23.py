# Упражнение по программированию 5.23

# Черепашья графика: модульный снеговик

import turtle

ANIMATION_SPEED = 0
BASE_X = 0
BASE_Y = -200
BASE_RADIUS = 100
MID_X = 0
MID_Y = 0
MID_RADIUS = 60

RIGHT_ARM_X1 = 60
RIGHT_ARM_Y1 = 60
RIGHT_ARM_X2 = 108
RIGHT_ARM_Y2 = 75
RIGHT_ARM_X3 = 118
RIGHT_ARM_Y3 = 75
RIGHT_ARM_X4 = 118
RIGHT_ARM_Y4 = 85

LEFT_ARM_X1 = -60
LEFT_ARM_Y1 = 60
LEFT_ARM_X2 = -105
LEFT_ARM_Y2 = 70
LEFT_ARM_X3 = -120
LEFT_ARM_Y3 = 110
LEFT_ARM_X4 = -130
LEFT_ARM_Y4 = 115
LEFT_ARM_X5 = -120
LEFT_ARM_Y5 = 125

HEAD_X = 0
HEAD_Y = 120
HEAD_RADIUS = 40

LEFT_EYE_X = -20
LEFT_EYE_Y = 170
RIGHT_EYE_X = 20
RIGHT_EYE_Y = 170
EYE_RADIUS = 5

MOUTH_START_X = -25
MOUTH_START_Y = 140
MOUTH_END_X = 25
MOUTH_END_Y = 140

HAT_X1 = -50
HAT_Y1 = 180
HAT_X2 = 50
HAT_Y2 = 180
HAT_X3 = 50
HAT_Y3 = 205
HAT_X4 = -50
HAT_Y4 = 205
HAT_X5 = -30
HAT_Y5 = 205
HAT_X6 = 30
HAT_Y6 = 205
HAT_X7 = 30
HAT_Y7 = 245
HAT_X8 = -30
HAT_Y8 = 245

def drawBase():
	# Нарисовать основание
    turtle.penup()
    turtle.goto(BASE_X, BASE_Y)
    turtle.pendown()
    turtle.circle(BASE_RADIUS)

def drawMidSection():
    turtle.penup()
    turtle.goto(MID_X, MID_Y)
    turtle.pendown()
    turtle.circle(MID_RADIUS)

def drawArms():
    # Нарисовать правую руку
    turtle.penup()
    turtle.goto(RIGHT_ARM_X1, RIGHT_ARM_Y1)
    turtle.pendown()
    turtle.goto(RIGHT_ARM_X2, RIGHT_ARM_Y2)
    turtle.goto(RIGHT_ARM_X3, RIGHT_ARM_Y3)
    turtle.penup()
    turtle.goto(RIGHT_ARM_X2, RIGHT_ARM_Y2)
    turtle.pendown()
    turtle.goto(RIGHT_ARM_X4, RIGHT_ARM_Y4)

    # Нарисовать левую руку
    turtle.speed(1)
    turtle.penup()
    turtle.goto(LEFT_ARM_X1, LEFT_ARM_Y1)
    turtle.pendown()
    turtle.goto(LEFT_ARM_X2, LEFT_ARM_Y2)
    turtle.goto(LEFT_ARM_X3, LEFT_ARM_Y3)
    turtle.goto(LEFT_ARM_X4, LEFT_ARM_Y4)
    turtle.penup()
    turtle.goto(LEFT_ARM_X3, LEFT_ARM_Y3)
    turtle.pendown()
    turtle.goto(LEFT_ARM_X5, LEFT_ARM_Y5)

def drawHead():
    # Нарисовать голову
    turtle.penup()
    turtle.goto(HEAD_X, HEAD_Y)
    turtle.pendown()
    turtle.circle(HEAD_RADIUS)

    # Нарисовать левый глаз
    turtle.penup()
    turtle.goto(LEFT_EYE_X, LEFT_EYE_Y)
    turtle.pendown()
    turtle.circle(EYE_RADIUS)

    # Нарисовать правый глаз
    turtle.penup()
    turtle.goto(RIGHT_EYE_X, RIGHT_EYE_Y)
    turtle.pendown()
    turtle.circle(EYE_RADIUS)

    # Нарисовать рот
    turtle.penup()
    turtle.goto(MOUTH_START_X, MOUTH_START_Y)
    turtle.pendown()
    turtle.goto(MOUTH_END_X, MOUTH_END_Y)

def drawHat():
    # Нарисовать нижнюю часть шляпы
    turtle.penup()
    turtle.goto(HAT_X1, HAT_Y1)
    turtle.fillcolor('black')
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(HAT_X2, HAT_Y2)
    turtle.goto(HAT_X3, HAT_Y3)
    turtle.goto(HAT_X4, HAT_Y4)
    turtle.end_fill()

    # Нарисовать верхнюю часть шляпы
    turtle.penup()
    turtle.goto(HAT_X5, HAT_Y5)
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(HAT_X6, HAT_Y6)
    turtle.goto(HAT_X7, HAT_Y7)
    turtle.goto(HAT_X8, HAT_Y8)
    turtle.end_fill()

def main():
    turtle.speed(ANIMATION_SPEED)
    turtle.hideturtle()
    drawBase()
    drawMidSection()
    drawArms()
    drawHead()
    drawHat()

    # Не закрывать окно.
    turtle.done()

# Вызвать главную функцию
main()    
