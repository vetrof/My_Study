import turtle

#упажнение 5:25

def square(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()

def main():
    z = 0
    for y in range(0, 251, 50):
        z += 1
        for x in range(0, 251, 50):
            if z % 2 == 0:
                color = 'white'
            else:
                color = 'black'
            z += 1
            square(x, y, color)

main()
turtle.done()




