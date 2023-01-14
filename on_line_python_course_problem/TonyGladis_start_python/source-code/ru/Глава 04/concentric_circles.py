# Концентрические круги
import turtle

# Именованные константы
NUM_CIRCLES = 20
STARTING_RADIUS = 20 
OFFSET = 10
ANIMATION_SPEED = 0

# Настроить черепаху.
turtle.speed(ANIMATION_SPEED)
turtle.hideturtle()

# Задать радиус первого круга
radius = STARTING_RADIUS

# Нарисовать круги.
for count in range(NUM_CIRCLES):
    # Нарисовать круг.
    turtle.circle(radius)

    # Получить координаты следующего круга.
    x = turtle.xcor()
    y = turtle.ycor() - OFFSET

    # Вычислить радиус следующего круга.
    radius = radius + OFFSET

    # Позиция черепахи для следующего круга.
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
turtle.done()