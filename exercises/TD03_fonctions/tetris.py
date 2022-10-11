# ***********
#   Tetris
# ***********

from tkinter import *
from random import randint

# constants
WIDTH = 200
HEIGHT = 600
SIZE = 20
SPEED = 150
BACKGROUND_COLOR = '#000000'
# all possible block colors
COLORS = ('#FF0000', '#00FF00', '#0000FF', '#FF00FF')
# setting all blocks and their variations
BLOCKS = (
    # 1
    (((2,0),(0,0),(1,0),(0,1)),
    ((1,2),(0,0),(0,1),(0,2)),
    ((2,0),(0,1),(1,1),(2,1)),
    ((1,0),(0,0),(1,1),(1,2))),
    # 1 bis
    (((2,1),(0,0),(0,1),(1,1)),
    ((1,0),(1,1),(1,2),(0,2)),
    ((2,0),(0,0),(1,0),(2,1)),
    ((1,0),(0,0),(0,1),(0,2))),
    # 2 (2x2)
    (((1,0),(0,0),(0,1),(1,1)),
    ((1,0),(0,0),(0,1),(1,1))),
    # 3 (4x1)
    (((0,0),(0,1),(0,2),(0,3)),
    ((3,0),(0,0),(1,0),(2,0))),
    # 3 bis (4x1)
    (((0,0),(0,1),(0,2),(0,3)),
    ((3,0),(0,0),(1,0),(2,0))),
    # 4
    (((2,1),(0,0),(1,0),(1,1)),
    ((1,0),(0,1),(1,1),(0,2))),
    # 4 bis
    (((2,0),(0,1),(1,0),(1,1)),
    ((1,1),(0,0),(0,1),(1,2))),
    # 5
    (((1,1),(0,1),(1,0),(1,2)),
    ((2,1),(0,1),(1,0),(1,1)),
    ((1,1),(0,0),(0,1),(0,2)),
    ((2,0),(0,0),(1,0),(1,1)))

)

# activated by player, speeds up the next_turn function
def speedup(a):
    global tempspeed
    tempspeed=a

# when freezed blocks reaches the last row
def game_over():
    canvas.configure(bg='red')
    canvas.itemconfigure(ALL, fill='black', outline='black')
    canvas.create_text(WIDTH//2,HEIGHT//2,text='GAME OVER',font=('consolas',20),fill='white')

# chacks for collisions with walls or freezed blocks
def check_collision():
    if chosen[0][0]*SIZE+y1 > HEIGHT-SIZE :
        return True
    else :
        for y, x in chosen :
            if (y1//SIZE+y) > 0 and (x+x1/SIZE in freezed[y1//SIZE+y]) :
                return True
        return False

# deletes a row when it is completed (also shifts down all upwards blocks)
def delete_row(i):
    canvas.delete(f"a{i}")
    freezed[i] = []
    f_colors[i] = []
    for a in range(i, 0,-1):
        freezed[a] = freezed[a-1]
        f_colors[a] = f_colors[a-1]
    freezed[0] = []
    f_colors[0] = []
    canvas.delete(ALL)
    for y in range(len(freezed)):
        count = 0
        for x in freezed[y] :
                canvas.create_rectangle(x*SIZE, y*SIZE, x*SIZE + SIZE, y*SIZE + SIZE, fill=f_colors[y][count][1] ,outline='white', tag=f"a{y}")
                count += 1

# main function, can be sped up, also checks for collision and freezes the block when touching ground
def next_turn():
    global y1, x1, x, y, freezed, tempspeed, f_colors, score
    label.configure(text=f'Score : {score}')
    y1 += SIZE
    canvas.delete('block')
    if not check_collision() :
        for y, x in chosen :
            canvas.create_rectangle(x*SIZE + x1, y*SIZE + y1, x*SIZE + SIZE + x1, y*SIZE + SIZE + y1, fill=color,outline='white', tag='block')
    else : 
        for y, x in chosen :
            canvas.create_rectangle(x*SIZE + x1, y*SIZE + y1 -SIZE , x*SIZE + SIZE + x1, y*SIZE + SIZE + y1 - SIZE, fill=color,outline='white', tag=f"a{(y1//SIZE+y-1)}")
            freezed[y1//SIZE+y-1].append(x1//SIZE+x)
            f_colors[y1//SIZE+y-1].append([x1//SIZE+x, color])
        streak = 0
        for i in range(0,len(freezed)) :
            if len(freezed[i]) == WIDTH//SIZE :
                streak += 1
                score += (WIDTH//SIZE)*streak
                delete_row(i)
        new_block()
    if freezed[0] == [] :
        root.after(SPEED-tempspeed, next_turn)
    else :
        game_over()

# choses a random block, block variant and color
def choose_rand():
    global chosen, number, color, variant
    number = randint(0,len(BLOCKS)-1)
    variant = randint(0,len(BLOCKS[number])-1)
    chosen = BLOCKS[number][variant]
    color = COLORS[randint(0, len(COLORS)-1)]

# creates a new block
def new_block():
    global x1, y1
    x1, y1 = 0, 0
    canvas.delete('block')
    choose_rand()
    for y, x in chosen :
        canvas.create_rectangle(x*SIZE, y*SIZE, x*SIZE+SIZE, y*SIZE+SIZE, fill=color,outline='white', tag='block')

# allows rotation of the block only if there is no obstacles
def rotate(direction):
    global chosen, variant, var
    if direction == 'right' :
        if variant < len(BLOCKS[number])-1 :
            variant += 1
        else :
            variant = 0
    else :
        if variant > 0 :
            variant -= 1
        else :
            variant = len(BLOCKS[number])-1
    chosen = BLOCKS[number][variant]
    if check_collision():
        if direction == 'right':
            rotate('left')
        else :
            rotate('right')
    canvas.delete('block')
    for y, x in chosen :
        canvas.create_rectangle(x*SIZE +x1, y*SIZE +y1, x*SIZE + SIZE +x1, y*SIZE + SIZE +y1, fill=color,outline='white', tag='block')
        if x*SIZE +x1 < 0 :
            var = (True, 'right')
        elif x*SIZE +x1 > WIDTH-SIZE*(chosen[-1][1]+1) :
            var = (True, 'left')
    if var[0] :
        move(var[1])
        var = (False, 'right')
    
# allows player to move block right or left as long as there is no obstacles
def move(direction):
    global chosen, x1
    if direction == 'right' and x1 < WIDTH-SIZE*(chosen[-1][1]+1):
        for y, x in chosen :
            if (x+x1/SIZE+1 in freezed[y1//SIZE+y]) :
                return
        x1 += SIZE
    elif direction == 'left' and x1 > 0 :
        for y, x in chosen :
            if (x+x1/SIZE-1 in freezed[y1//SIZE+y]) :
                return
        x1 -= SIZE
    else : return
    canvas.delete('block')
    for y, x in chosen :
        canvas.create_rectangle(x*SIZE +x1, y*SIZE +y1, x*SIZE + SIZE +x1, y*SIZE + SIZE +y1, fill=color,outline='white', tag='block')

# variables
score = 0
y1, z1 = 0, 0
var = (False, 'left')
freezed = []
tempspeed = 0
f_colors = []
for i in range(HEIGHT//SIZE) :
    freezed.append([])
for i in range(HEIGHT//SIZE) :
    f_colors.append([])

# creating window
root = Tk()
root.title('Tetriste')
root.configure(bg=BACKGROUND_COLOR)
root.resizable(False, False)

# setting score label
label = Label(root, text=f'Score : {score}', font=('consolas', 20), bg=BACKGROUND_COLOR, fg='white')
label.pack()

# drawing canvas
canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg=BACKGROUND_COLOR)
canvas.pack()

# binding arrow keys to movement
root.bind('<Up>', lambda event: rotate('right'))
root.bind('<Down>', lambda event: rotate('left'))
root.bind('<Right>', lambda event: move('right'))
root.bind('<Left>', lambda event: move('left'))
# biniding zqsd to movement
root.bind('<z>', lambda event: rotate('right'))
root.bind('<s>', lambda event: rotate('left'))
root.bind('<d>', lambda event: move('right'))
root.bind('<q>', lambda event: move('left'))
# binding spacebar to speedup function
root.bind('<KeyPress-space>', lambda event : speedup(SPEED - SPEED//4))
root.bind('<KeyRelease-space>', lambda event : speedup(0))

# launching program loop
new_block()
next_turn()

# launching window
root.mainloop()