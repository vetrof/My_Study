import tkinter
import time

window = tkinter.Tk()
canvas = tkinter.Canvas(window)
canvas.pack()


x = 0
y = 10
x2 = 50
y2 = 50
delta = 2

rect = canvas.create_rectangle(x, y, x2, y2)


##############################

while True:
    x += delta
    x2 += delta
    time.sleep(.01)
    canvas.coords(rect, x, y, x2, y2)
    canvas.update()
    if x < 0 or x > 200:
        delta = -delta


#################
window.mainloop()