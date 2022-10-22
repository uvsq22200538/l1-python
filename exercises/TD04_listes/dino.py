# ******
# Dino
# ******
from tkinter import *
from random import randint
from math import sin

WIDTH=700
HEIGHT=300
BACKGROUD_COLOR = "#000000"
DINO_COLOR = "#FFFFFF"
SIZE = 20
SPEED = 50

root = Tk()

canvas = Canvas(root,width=WIDTH, height=HEIGHT, bg=BACKGROUD_COLOR)
canvas.pack()

canvas.create_line(0,HEIGHT//2+SIZE, WIDTH, HEIGHT//2+SIZE, fill='#FFFFFF')


canvas.create_rectangle(WIDTH//2-SIZE,HEIGHT//2-SIZE,WIDTH//2+SIZE,HEIGHT//2+SIZE, fill=DINO_COLOR, tag='dino')

switch = True
stage = 0
is_jumping = False
def jump(event):
    global y, y1, stage, switch
    is_jumping = True
    #if switch and 



x = WIDTH//2-SIZE
y = HEIGHT//2-SIZE
x1 = WIDTH//2+SIZE
y1 = HEIGHT//2+SIZE

def position():
    if is_jumping :
        jump()
    canvas.delete("dino")
    canvas.create_rectangle(x,y,x1,y1, fill=DINO_COLOR, tag='dino')

def next_turn():
    position()
    root.after(SPEED, next_turn)

next_turn()

root.bind('<space>', jump)

root.resizable(False,False)
root.mainloop()