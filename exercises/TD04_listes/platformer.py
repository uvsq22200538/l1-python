# **********
# platformer
# **********

from tkinter import *

root = Tk()
root.resizable(False, False)

HEIGHT = 512
WIDTH = 1024
BACKGROUND_COLOR = '#000000'
SPEED = 16
PLAYER_SIZE = 16
PLAYER_COLOR = '#FF0000'

g_over = False
pos_x = WIDTH//2
pos_y = HEIGHT//2
move = ['none', 'none']
aim = ['right', 'none']
last = ['right', 'none']
gun_x = 0
gun_y = 0

canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg=BACKGROUND_COLOR)
canvas.pack()

def next():
    movement()
    draw_player()
    gun_orientation()
    if not g_over :
        root.after(SPEED, next)

def draw_player():
    canvas.delete('player')
    canvas.create_oval(pos_x-PLAYER_SIZE, pos_y-PLAYER_SIZE, pos_x+PLAYER_SIZE, pos_y+PLAYER_SIZE, fill=PLAYER_COLOR, outline='', tag='player')

def gun_orientation():
    global gun_x, gun_y
    print(last)
    canvas.delete('gun')
    if aim[0] == 'left' or aim[0] == 'right':
        last[0] = aim[0]
    elif 'none' not in last : 
        last[0] = 'none'
    if aim[1] == 'up' or aim[1] == 'down':
        last[1] = aim[1]
    elif 'none' not in last : 
        last[1] = 'none'
    
    if last[0] == 'left':
        gun_x = -PLAYER_SIZE
    elif last[0] == 'right':
        gun_x = PLAYER_SIZE
    else :
        gun_x = 0
    
    if last[1] == 'up':
        gun_y = -PLAYER_SIZE
    elif last[1] == 'down':
        gun_y = PLAYER_SIZE
    else :
        gun_y = 0
    canvas.create_rectangle(pos_x-5+gun_x, pos_y-5+gun_y, pos_x+5+gun_x, pos_y+5+gun_y, fill='#FFFFFF', tag='gun')

def movement():
    global pos_x, pos_y
    if 'none' in move :
        speed = 8
    else :
        speed = 6
    
    if move[1] == 'up' and check_collision('y', -speed):
        pos_y -= speed
    elif move[1] == 'down' and check_collision('y', speed):
        pos_y += speed
    if move[0] == 'left' and check_collision('x', -speed):
        pos_x -= speed
    elif move[0] == 'right' and check_collision('x', speed):
        pos_x += speed

def check_collision(direction, value):
    # check boudaries
    if direction == 'y' and (pos_y+value < 0+PLAYER_SIZE or pos_y+value > HEIGHT-PLAYER_SIZE):
        return False
    elif direction == 'x' and (pos_x+value < 0+PLAYER_SIZE or pos_x+value > WIDTH-PLAYER_SIZE):
        return False
            
    return True

def direction_x(direction):
    global move
    move[0] = direction
    print(move)

def direction_y(direction):
    global move
    move[1] = direction

def aim_x(direction):
    global aim
    aim[0] = direction

def aim_y(direction):
    global aim
    aim[1] = direction

def game_over():
    global g_over, move
    g_over = True
    move = 'none'


root.bind('<KeyPress-z>', lambda event : direction_y('up'))
root.bind('<KeyPress-s>', lambda event : direction_y('down'))
root.bind('<KeyPress-q>', lambda event : direction_x('left'))
root.bind('<KeyPress-d>', lambda event : direction_x('right'))

root.bind('<KeyRelease-z>', lambda event : direction_y('none'))
root.bind('<KeyRelease-s>', lambda event : direction_y('none'))
root.bind('<KeyRelease-q>', lambda event : direction_x('none'))
root.bind('<KeyRelease-d>', lambda event : direction_x('none'))

root.bind('<KeyPress-Up>', lambda event : aim_y('up'))
root.bind('<KeyPress-Down>', lambda event : aim_y('down'))
root.bind('<KeyPress-Left>', lambda event : aim_x('left'))
root.bind('<KeyPress-Right>', lambda event : aim_x('right'))

root.bind('<KeyRelease-Up>', lambda event : aim_y('none'))
root.bind('<KeyRelease-Down>', lambda event : aim_y('none'))
root.bind('<KeyRelease-Left>', lambda event : aim_x('none'))
root.bind('<KeyRelease-Right>', lambda event : aim_x('none'))

next()

root.mainloop()