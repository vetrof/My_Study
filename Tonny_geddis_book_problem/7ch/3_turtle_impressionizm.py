import random
import turtle

color_list = ['coral', 'purple', 'ivory3', 'azure3', 'navy', 'gold', 'orange2']
turtle.speed(0)
turtle.hideturtle()


while 1:
    # turtle.penup()
    x = random.randint(-500, 500)
    y = random.randint(-500, 500)
    turtle.width(random.randint(1, 10))

    color = color_list[random.randint(0, 6)]
    turtle.color(color)
    turtle.goto(x, y)

    # turtle.pendown()
    # turtle.dot(10, color)




turtle.mainloop()



