# эта программа наносит звезды созвездия ориона

import turtle
turtle.speed(1)

# window size
turtle.setup(500, 600)

#set turtle
turtle.penup()
turtle.hideturtle()

# star coordinate
LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200

RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180

LEFT_BELTSTAR_X = -40
LEFT_BELTSTAR_Y = -20

MIDDLE_BELTSTAR_X = 0
MIDDLE_BELTSTAR_Y = 0

RIGHT_BELTSTAR_X = 40
RIGHT_BELTSTAR_Y = 20

LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180

RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140

# set star
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y) #left shoulder
turtle.dot()
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y) #right shoulder
turtle.dot()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y) #LEFT BELTSTAR
turtle.dot()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y) #MIDLE BELTSTAR
turtle.dot()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y) #RIGHT BELTSTAR
turtle.dot()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y) #LEFT KNEE
turtle.dot()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y) #RIGHT KNEE
turtle.dot()

# naming star
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y) #left shoulder
turtle.write('Бетельгейзе')
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y) #right shoulder
turtle.write('Хатиса')
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y) #LEFT BELTSTAR
turtle.write('Альнитак')
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y) #MIDLE BELTSTAR
turtle.write('Альнилам')
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y) #RIGHT BELTSTAR
turtle.write('Минтака')
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y) #LEFT KNEE
turtle.write('Саиф')
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y) #RIGHT KNEE
turtle.write('Ригель')

# write line
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y) #left shoulder
turtle.pendown()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y) #LEFT BELTSTAR
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y) #LEFT KNEE
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y) #LEFT BELTSTAR
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y) #MIDLE BELTSTAR
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y) #RIGHT BELTSTAR
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y) #right shoulder
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y) #RIGHT BELTSTAR
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y) #RIGHT KNEE


turtle.done()