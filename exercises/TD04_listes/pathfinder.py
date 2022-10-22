from tkinter import *
from random import randint

WIDTH = 600
HEIGHT = 600
SIZE = 10
BACKGROUND_COLOR = '#000000'
PATH_COLOR = '#FFFFFF'

GOAL = []

OBSTACLES = [[0,200,500,200],[100,400,600,400]]
grid = []

root = Tk()

canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg=BACKGROUND_COLOR)
canvas.pack()

def draw_obstacles():
    canvas.delete('obstacle')
    for x1, y1, x2, y2 in OBSTACLES:
        canvas.create_line(x1,y1,x2,y2, fill=PATH_COLOR, width=3, tag='obstacle')

def create_grid():
    global grid
    canvas.delete('grid')
    for x in range(0, WIDTH, SIZE):
        pass


draw_obstacles()
root.resizable(False, False)
root.mainloop()