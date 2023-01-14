import random
import turtle
turtle.speed()

angle = 10

print(angle)

for i in range(2000):

    turtle.setheading(angle)
    turtle.forward(1)

    xcor = turtle.xcor()
    ycor = turtle.ycor()

    if xcor >= 100:
        angle_incidence = 180 - angle - 90
        angle = 90 + angle_incidence
        turtle.setheading(angle)
        turtle.forward(10)
        turtle.write(angle)
        print(angle)

    if xcor <= -100:
        angle = angle + 90
        turtle.setheading(angle)
        turtle.forward(10)

    if ycor >= 100:
        angle = angle + 90
        turtle.setheading(angle)
        turtle.forward(10)

    if ycor <= -100:
        angle = angle + 90
        turtle.setheading(angle)
        turtle.forward(10)




























turtle.done()