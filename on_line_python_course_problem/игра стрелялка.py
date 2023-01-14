
import random
import time
import turtle
turtle.hideturtle()

win = False #переменная для отключения цикла при выигрыше

while not win:
    turtle.goto(0, 0)
    turtle.bgcolor('palegreen4')
    turtle.color('gold')
    turtle.clear()

    turtle.speed(0)  # рисуем координатную сетку и градусы
    turtle.setheading(0)
    turtle.forward(300)
    turtle.write('0', font=('Arial', 13, 'normal'))
    turtle.setheading(180)
    turtle.forward(600)
    turtle.write('180', font=('Arial', 13, 'normal'))
    turtle.setheading(0)
    turtle.forward(300)
    turtle.setheading(90)
    turtle.forward(300)
    turtle.write('90', font=('Arial', 13, 'normal'))
    turtle.setheading(270)
    turtle.forward(600)
    turtle.write('270', font=('Arial', 13, 'normal'))
    turtle.speed(4)

    x_cel = random.randint(-300, 300)  #задаем рандомную мишень
    y_cel = random.randint(-300, 300)

    turtle.penup() #рисуем мишень
    turtle.goto(0, 0)
    turtle.goto(x_cel,y_cel)
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(0)
    turtle.forward(50)
    turtle.setheading(270)
    turtle.forward(50)
    turtle.setheading(180)
    turtle.forward(50)
    turtle.penup()

    angle_shoot = 00  # дефолтные значения для выстрела
    power_shoot = 00

    for i in range(3):

        turtle.goto(0,0) #возвращаем перо в центр
        turtle.pendown()

        #делаем запрос угла и силы
        angle_shoot = int(turtle.numinput(f'You have {3 - i} shoot', 'Input angle of shoot', default=angle_shoot))
        power_shoot = int(turtle.numinput(f'You have {3 - i} shoot', 'Input power you shoot', default=power_shoot))

        # выстрел
        turtle.speed(2)
        # turtle.showturtle()
        turtle.setheading(angle_shoot)
        turtle.forward(power_shoot)
        for i in range(0, 20, 4):
            turtle.dot(i, 'red')

        #проверка результатов выстрела
        x_shoot = turtle.xcor()
        y_shoot = turtle.ycor()

        if (x_shoot >= x_cel and        #если выстрел удачный
            x_shoot <= (x_cel + 50) and
            y_shoot >= y_cel and
            y_shoot <= (y_cel + 50)):

            for i in range(15, 300, 12): # рисуем взрыв
                turtle.dot(i, 'red')

            #поздравляем
            turtle.write('you WIN!!!', font=('Arial', 30, 'normal'))

            time.sleep(1) #мигаем экраном от радости
            turtle.bgcolor('gold')
            time.sleep(0.2)
            turtle.bgcolor('white')
            time.sleep(0.2)
            turtle.bgcolor('gold')
            time.sleep(0.2)
            turtle.bgcolor('white')
            time.sleep(0.2)
            turtle.bgcolor('hotpink4')
            win = True
            break           # и выходим из цикла if range(3)

        else:
            print('you luser !! a ha ha')  #если выстрел не имел успеха
            # turtle.write(f'{angle_shoot:.1f} , {power_shoot:.1f}', font=('Arial', 13, 'normal'))
            time.sleep(1)



while 1: #анимация концовки - бесконечные круги
    turtle.speed(0)
    turtle.forward(10)
    turtle.left(random.randint(0, 15))

turtle.done()
