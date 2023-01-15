import random
import tkinter
import time

window = tkinter.Tk()
canvas = tkinter.Canvas(window, width = 400, height = 400)
colors = ['black', 'yellow', 'green', 'blue', 'red']
canvas.pack()

circle = []

for i in range(5):
    x0 = random.randint(50, 350)
    y0 = random.randint(50, 350)
    r0 = random.randint(10, 50)
    x1 = x0 + r0
    y1 = y0 + r0
    a = {}
    a['dx'] = random.randint(-10, 10)
    a['dy'] = random.randint(-10, 10)
    a['id'] = canvas.create_oval(x0, y0, x1, y1, fill=colors[i])
    circle.append(a)

while True:
    for i in circle:
        x0, y0, x1, y1 = canvas.coords(i['id'])
        if x1 >= 400 or x0 <= 0:
            i['dx'] *= -1
        if y1 >= 400 or y0 <= 0:
            i['dy'] *= -1
        canvas.move(i['id'], i['dx'], i['dy'])
    canvas.update()
    time.sleep(0.001)
window.mainloop()














# x = 0
# y = 10
# x2 = 50
# y2 = 50
# delta = 2
#
# rect = canvas.create_rectangle(x, y, x2, y2)
#
#
# ##############################
#
# while True:
#     x += delta
#     x2 += delta
#     time.sleep(.01)
#     canvas.coords(rect, x, y, x2, y2)
#     canvas.update()
#     if x < 0 or x > 200:
#         delta = -delta
#

#################
window.mainloop()