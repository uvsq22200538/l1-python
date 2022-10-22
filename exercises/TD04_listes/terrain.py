# ************
#  2D Terrain
# ************

from tkinter import *
from random import randint

# constants
WIDTH = 900
HEIGHT = 600
SIZE = 25
BACKGROUND_COLOR = '#000000'
SPEED = 100
VARIANCE = 200

root = Tk()
root.resizable(False, False)

canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg=BACKGROUND_COLOR)
canvas.pack()
canvas.create_line(0, HEIGHT//2 + VARIANCE, WIDTH, HEIGHT//2 + VARIANCE, fill='red')
canvas.create_line(0, HEIGHT//2 - VARIANCE, WIDTH, HEIGHT//2 - VARIANCE, fill='red')

def refresh(event):
    canvas.delete(ALL)
    last = 0
    r = 0
    for i in range(WIDTH//SIZE):
        if -150 < r < 150 :
            r = randint(last-VARIANCE, last+VARIANCE)
        elif r >= 150 :
            r = last - SIZE
        else :
            r = last + SIZE
        canvas.create_line(i*SIZE, HEIGHT//2 + last, i*SIZE+SIZE, HEIGHT//2 + r, fill='#FFFFFF', width=2)
        last = r

def refresh2(event):
    global pente, x1, x2, y1, y2
    canvas.delete('courbe')
    pente = 0
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = HEIGHT//2
    for i in range(WIDTH//SIZE):
        x1 = i*SIZE
        y1 = y2
        x2 = i*SIZE+SIZE
        y2 = (pente * (x2-x1)) + y1
        canvas.create_line(x1, y1, x2, y2, fill='#FFFFFF', width=2, tag='courbe')
        if y2 >= HEIGHT :
            pente = ((y2-y1)/(x2-x1)) + randint(25, 100)/250
        elif y2 < HEIGHT//2+VARIANCE :
            pente = ((y2-y1)/(x2-x1)) + randint(-33, 100)/500
        elif y2 <= HEIGHT :
            pente = ((y2-y1)/(x2-x1)) + randint(-100, -25)/250
        elif y2 > HEIGHT//2-VARIANCE :
            pente = ((y2-y1)/(x2-x1)) + randint(-100, 33)/500
        else :
            pente = ((y2-y1)/(x2-x1)) + randint(-75, 75)/2500

def scroll(event):
    global pente, x1, x2, y1, y2
    canvas.move("courbe", -SIZE, 0)
    x1 = WIDTH-SIZE
    y1 = y2
    x2 = WIDTH
    y2 = (pente * (x2-x1)) + y1
    canvas.create_line(x1, y1, x2, y2, fill='#FFFFFF', width=2, tag='courbe')
    if y2 >= HEIGHT :
        pente = ((y2-y1)/(x2-x1)) + randint(25, 100)/250
    elif y2 < HEIGHT//2+VARIANCE :
        pente = ((y2-y1)/(x2-x1)) + randint(-33, 100)/500
    elif y2 <= HEIGHT :
        pente = ((y2-y1)/(x2-x1)) + randint(-100, -25)/250
    elif y2 > HEIGHT//2-VARIANCE :
        pente = ((y2-y1)/(x2-x1)) + randint(-100, 33)/500
    else :
        pente = ((y2-y1)/(x2-x1)) + randint(-75, 75)/100

root.bind('<r>', refresh)
root.bind('<t>', refresh2)
root.bind('<Right>', scroll)
root.mainloop()
