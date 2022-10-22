from tkinter import *
from random import randint

WIDTH = 500
HEIGHT = 500
SPEED = 16
E_SIZE = 10
E_COLOR = '#FF0000'
E_SPEED = 1
BG_COLOR = '#FFFFFF'

root = Tk()

canvas = Canvas(root, width=WIDTH, height=HEIGHT, background=BG_COLOR)
canvas.pack()



def refresh(event):
    global entities, cur_x, cur_y, go
    entities = []
    for a in range(4):
        for i in range(9):
            xe = 50 + i*50
            ye = HEIGHT/10 + a*50
            entities.append([xe,ye])
    cur_x, cur_y = WIDTH/2, HEIGHT/2
    go = False
        

def draw_entities():
    canvas.delete('entity')
    for i in range(len(entities)):
        x = entities[i][0]
        y = entities[i][1]
        canvas.create_oval(x-E_SIZE,y-E_SIZE,x+E_SIZE,y+E_SIZE, fill=E_COLOR, tag='entity')


def next():
    draw_entities()
    if go :
        move_entities()
    root.after(SPEED, next)

def motion(event):
    global cur_x, cur_y
    cur_x, cur_y = event.x, event.y


def update_goal(var):
    global go
    go = var

def move_entities():
    for i in range(len(entities)):
        x = entities[i][0]
        y = entities[i][1]
        dx = cur_x - x
        dy = cur_y - y
        dist = (dx**2 + dy**2)**(1/2)
        dy /= dist
        dx /= dist
        x += dx + dx*E_SPEED
        y += dy + dy*E_SPEED
        entities[i][0] = x
        entities[i][1] = y
        closest = 0
        c_dist = WIDTH*HEIGHT
        if len(entities) > 1 :
            for u in range(len(entities)):
                if u == i : continue
                a = ((x - entities[u][0])**2 + (y - entities[u][1])**2)**(1/2)
                if a < c_dist :
                    c_dist = a
                    closest = u
            if c_dist == 0:
                repel_force = 0
            else :
                repel_force = E_SIZE*2/c_dist
            if repel_force != 0:
                dxr = (x - entities[closest][0])/c_dist
                dyr = (y - entities[closest][1])/c_dist
                entities[i][0] += (dxr + dxr*E_SPEED*0.4)*repel_force*0.5
                entities[i][1] += (dyr + dyr*E_SPEED*0.4)*repel_force*0.5
                



refresh(1)

next()

root.bind('<ButtonPress-1>', lambda event : update_goal(True))
root.bind('<ButtonRelease-1>', lambda event : update_goal(False))
root.bind('<Motion>', motion)

root.bind('<r>', refresh)

root.resizable(False,False)
root.mainloop()