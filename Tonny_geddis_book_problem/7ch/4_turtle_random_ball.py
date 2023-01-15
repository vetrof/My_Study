import random
import turtle

color_list = ['coral', 'purple', 'ivory3', 'azure3', 'navy', 'gold', 'orange2']
turtle.speed(0)
turtle.hideturtle()


while 1:
    # turtle.penup()
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    size = random.randint(2, 100)
    color = color_list[random.randint(0, 6)]


    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

    # turtle.pendown()
    # turtle.dot(10, color)




turtle.mainloop()



