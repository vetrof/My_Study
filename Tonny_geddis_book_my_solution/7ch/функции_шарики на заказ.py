
import random
import time
import def_color_rnd
import turtle

#прветсвие и выбор вариантов 1 и 2  3- выход
# 1 - показываемшарики в основных цветах
# 2 показываем шарики в осенних цветах
# 3 - выход программы
# ввод всегда проверям на корректность

def main():

    menu()
    vibor = int(input('...выбирай, ну...- '))
    if vibor == 3:
        print(' я понял.. пошол я нухуй...')

    while vibor != 3:
        if vibor == 1 or vibor == 2:
            random_baloons(vibor)
            vibor = 3
        else:
            print('ты чо? разливать разучился?')
            vibor = int(input('...выбирай, ну...- '))

    

def menu():
    print('дратути, я вам щас покажу шарики, в каких цветах будем смотреть?')
    print('1 - если в основных цветах')
    print('2 - если в осенних, дизайнерский колерах')
    print('3 - а не пойти ли мне нахуй уважаемый...')
    time.sleep(1)
    print()
    print('... ну мля...давай ужо')
    time.sleep(1)

def random_baloons(vibor):

    for i in range(10):

        if vibor == 1:
            color = def_color_rnd.primary_color()

        elif vibor == 2:
            color = def_color_rnd.autumn_color()

        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        turtle.speed(100)
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(x, y)
        turtle.dot(50, color)



    # if vibor == 1:
    #     for i in range(10):
    #         color = def_color_rnd.primary_color()
    #         x = random.randint(-200, 200)
    #         y = random.randint(-200, 200)
    #         turtle.speed(100)
    #         turtle.penup()
    #         turtle.hideturtle()
    #         turtle.goto(x, y)
    #         turtle.dot(50, color)
    #
    # if vibor == 2:
    #     for i in range(10):
    #         color = def_color_rnd.autumn_color()
    #         x = random.randint(-200, 200)
    #         y = random.randint(-200, 200)
    #         turtle.speed(100)
    #         turtle.penup()
    #         turtle.hideturtle()
    #         turtle.goto(x, y)
    #         turtle.dot(50, color)

main()