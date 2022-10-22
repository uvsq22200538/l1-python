from tkinter import *
from math import cos
from random import randint

root = Tk()

WIDTH = 800
HEIGHT = 400
SPEED = 25

canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg='#000000')
canvas.pack()

x0, x1, y0, y1 = WIDTH//3 -25, WIDTH//3 +25, HEIGHT*2//3 -25, HEIGHT*2//3 +25 

var = 0
is_jumping = False

def check_collision():
    print(y1, HEIGHT//2+50)
    if WIDTH - ver > WIDTH//3 -25 and WIDTH - ver < WIDTH//3 +25 and y1 > 250:
        game_over()

def jump():
    global is_jumping
    if not is_jumping :
        move_block()

def move_block():
    global y0, y1, var, is_jumping
    is_jumping = True
    canvas.delete('block')
    y0 -= cos(var/10)*14
    y1 -= cos(var/10)*14
    var += 1
    canvas.create_rectangle(x0,y0,x1,y1, fill='#FFFFFF', outline='#FFFFFF', tag='block')

    if var < 32 and not g_over :
        root.after(15, move_block)
    else :
        is_jumping = False
        var = 0
        y0, y1 = HEIGHT*2//3 -25, HEIGHT*2//3 +25

def next_turn():
    global y0, y1
    check_collision()
    if not is_jumping :
        canvas.delete('block')
        y0, y1 = HEIGHT*2//3 -25, HEIGHT*2//3 +25
        canvas.create_rectangle(x0, y0, x1, y1, fill='#FFFFFF', outline='#FFFFFF', tag='block')
    if not g_over :
        root.after(SPEED,next_turn)

nb_obst = 0
def generate_obstacle():
    global nb_obst
    if nb_obst == 1 :
        return
    if  randint(0,50) == 1 :
        nb_obst = 1
        move_obstacles()

ver = 0
def move_obstacles():
    global nb_obst, ver
    canvas.delete('obst')
    canvas.create_rectangle(WIDTH-ver, HEIGHT//2+50, WIDTH-ver-25, HEIGHT*2//3+25, fill='#0000FF', tag='obst')
    ver += 10
    if nb_obst == 1 and WIDTH-ver > 0 and not g_over :
        root.after(SPEED, move_obstacles)
    else :
        nb_obst = 0
        ver = 0
        canvas.delete('obst')

variance = 200
def move_terrain():
    global variance
    if variance <= 0 :
        variance = 200
    canvas.delete('terrain')
    for i in range(10):
        if i%2 == 0 :
            color = 'green'
        else :
            color = 'lime'
        canvas.create_rectangle(i*100+variance-200,HEIGHT*2//3+25,i*100+variance-100,HEIGHT, fill=color, outline=color, tag='terrain')
    variance -= 10
    generate_obstacle()
    if not g_over :
        root.after(SPEED, move_terrain)

g_over = False
def game_over():
    global g_over
    g_over = True
    canvas.create_text(WIDTH//2, HEIGHT//2, text='GAME OVER', fill='#FFFFFF', font=('consolas', 20))

move_terrain()
next_turn()

root.bind('<space>', lambda event : jump())

root.mainloop()