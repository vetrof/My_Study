import random
import tkinter
import time
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=400, height=400)
canvas.pack()

colors = ('chartreuse2', 'red', 'blue1', 'DarkOliveGreen1',
          'DeepPink1', 'DarkOliveGreen3', 'goldenrod1' )

# xc yc - это коррдинаты центров круга    r - радиус


while True:
    xc = random.randint(0, 400)
    yc = random.randint(0, 400)
    r = 145

    for i, c in enumerate(colors):
        r = r + 5
        canvas.create_oval(xc - r, yc - r, xc + r, yc + r, outline=c)
        canvas.update()
        # time.sleep(0.1)

        # print(xc, yc, r, c)



window.mainloop()