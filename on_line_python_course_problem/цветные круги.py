import tkinter
import time
window = tkinter.Tk()
canvas = tkinter.Canvas(window)
canvas.pack()

for R in range(5, 100 , 5):
    x0 = 100 - R
    y0 = 100 - R
    x1 = 100 + R
    y1 = 100 + R
    if R % 2 == 0:
        canvas.create_oval(x0, y0, x1, y1, outline="red")
    else:
        canvas.create_oval(x0, y0, x1, y1, outline="grey")
    canvas.update()
    time.sleep(0.1)


window.mainloop()