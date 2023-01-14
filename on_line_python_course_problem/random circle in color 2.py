
import random
import tkinter
import time
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=400, height=400)
canvas.pack()

colors = ('chartreuse2', 'red', 'blue1', 'DarkOliveGreen1',
          'DeepPink1', 'DarkOliveGreen3', 'goldenrod1' )

# lencolor = len(colors)
col = 0
# xc yc - это коррдинаты центров круга    r - радиус


while 1:
    xc = random.randint(0, 400)
    yc = random.randint(0, 400)
    # r = 145

    for r in range(150, 185, 5):
        canvas.create_oval(xc - r, yc - r, xc + r, yc + r, outline=colors[col])
        col = col + 1
        if col > 6:
            col = 1
        canvas.update()
        time.sleep(0.1)

        # print(xc, yc, r, c)


window.mainloop()