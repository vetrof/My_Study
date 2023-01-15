#упражнение 5:23
import turtle
turtle.speed(100)


def drawBase():
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.circle(100)

def drawMidSection():
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.circle(60)

def drawArms():
    turtle.penup()
    turtle.goto(60, 60)
    turtle.pendown()
    turtle.goto(120, 80)
    turtle.goto(140, 100)
    turtle.goto(120, 80)
    turtle.goto(140, 70)
    turtle.penup()
    turtle.goto(-60, 60)
    turtle.pendown()
    turtle.goto(-100, 70)
    turtle.goto(-110, 110)
    turtle.goto(-120, 120)
    turtle.goto(-110, 110)
    turtle.goto(-100, 120)
    turtle.penup()
    turtle.goto(0, 120)
    turtle.pendown()

def drawHead():
    turtle.circle(40)
    turtle.penup()
    turtle.goto(0, 140)
    turtle.pendown()
    turtle.goto(0, 155)
    turtle.penup()
    turtle.goto(- 12, 160)
    turtle.pendown()
    turtle.circle(5)
    turtle.penup()
    turtle.goto(12, 160)
    turtle.pendown()
    turtle.circle(5)
    turtle.penup()
    turtle.goto(-15, 135)
    turtle.pendown()
    turtle.goto(15, 135)

def drawHat():
    turtle.penup()
    turtle.goto(-60, 180)
    turtle.pendown()
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.goto(60, 180)
    turtle.goto(60, 200)
    turtle.goto(40, 200)
    turtle.goto(40, 250)
    turtle.goto(-40, 250)
    turtle.goto(-40, 200)
    turtle.goto(-60, 200)
    turtle.goto(-60, 180)
    turtle.end_fill()

def main():
    drawBase()
    drawMidSection()
    drawArms()
    drawHead()
    drawHat()

main()
turtle.done()
