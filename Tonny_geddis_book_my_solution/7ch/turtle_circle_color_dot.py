
import turtle
import random

color_list = ['red', 'green', 'blue', 'yellow', 'cyan']

turtle.bgcolor('gray10')
turtle.setup(300, 300)

for i in range(100):
	rnd_adgle = random.randint(0, 360)
	color = color_list[random.randint(0, 4)]
	turtle.setheading(rnd_adgle)
	turtle.penup()
	turtle.forward(100)
	turtle.pendown()
	turtle.color(color)
	turtle.dot(10)
	for io in range(3):
		color = color_list[random.randint(0, 4)]
		turtle.color(color)
		turtle.dot(10)
	turtle.penup()
	turtle.backward(100)
	print(i,rnd_adgle, color)

turtle.dot(30)
# turtle.color(1)
# turtle.circle(50)


turtle.mainloop()
print(color)






