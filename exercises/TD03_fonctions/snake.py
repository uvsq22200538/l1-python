# *****************
#    Snake Game
# *****************

from tkinter import *
from random import randint

# Constants
WIDTH = 500
HEIGHT = 500
SIZE = 10
SPEED = 100
BODY_PARTS = 3
BACKGROUND_COLOR = '#000000'
SNAKE_COLOR = '#00FF00'
FOOD_COLOR = '#FF0000'

# Variables
hscore = 0
score = 0
direction = 'down'
pas_confirme = True
g_over = False
var = True

# Creating the window
root = Tk()
root.resizable(False, False)
root.title('sake game')
root.configure(bg='black')
# Creating score label
label = Label(root, text=f"High Score : {hscore} | Score : {score}", font=('consolas', 20), fg='White', bg='Black')
label.pack()

# Creating canvas
canvas = Canvas(root, bg=BACKGROUND_COLOR , width=WIDTH, height=HEIGHT)
canvas.pack()

# Creating snake head
snake_pos = []
for i in range(BODY_PARTS):
    snake_pos.append([0,0])
for x,y in snake_pos:
    snake = canvas.create_rectangle(x, y, x+WIDTH//SIZE, y+WIDTH//SIZE, fill=SNAKE_COLOR, outline=SNAKE_COLOR, tag="snake")

# Creating food
xf = WIDTH//SIZE * randint(0, SIZE-1)
yf = HEIGHT//SIZE * randint(0, SIZE-1)
food = canvas.create_oval(xf, yf, xf+WIDTH//SIZE, yf+WIDTH//SIZE, fill=FOOD_COLOR, outline=FOOD_COLOR, tag="food")


# Generates a new food
def new_food():
    global score, food, xf, yf
    canvas.delete(food)
    score += 1
    xf = WIDTH//SIZE * randint(0, SIZE-1)
    yf = HEIGHT//SIZE * randint(0, SIZE-1)
    food = canvas.create_oval(xf, yf, xf+WIDTH//SIZE, yf+WIDTH//SIZE, fill=FOOD_COLOR, outline=FOOD_COLOR, tag="food")
    label.configure(text=f"High Score : {hscore} | Score : {score}")


# Main function, makes snake move
def next_turn():
    global snake_pos, BODY_PARTS, snake, pas_confirme, x, y, xf, yf, g_over
    pas_confirme = True
    canvas.delete("snake")
    if direction == 'up' :
        y = snake_pos[0][1]-(WIDTH//SIZE)
    elif direction == 'down' :
        y = snake_pos[0][1]+(WIDTH//SIZE)
    elif direction == 'right' :
        x = snake_pos[0][0]+(WIDTH//SIZE)
    elif direction == 'left' :
        x = snake_pos[0][0]-(WIDTH//SIZE)
    snake_pos.insert(0, [x, y])
    # Adding 1 block to snake if it touched food
    if not (x == xf and y == yf) :
        snake_pos.pop(-1)
    else :
        new_food()
    for xs, ys in snake_pos :
        snake = canvas.create_rectangle(xs, ys, xs+WIDTH//SIZE, ys+WIDTH//SIZE, fill=SNAKE_COLOR, outline=SNAKE_COLOR, tag="snake")
    canvas.tag_lower("snake")
    # checking for collision, if so : game is over
    if check_collision():
        game_over()
    # closing the loop
    if not g_over :
        root.after(SPEED, next_turn)

# define new direction
def change_direction(new_direction) :
    global direction, pas_confirme
    if pas_confirme and new_direction != direction :
        if new_direction == 'up' and direction != 'down' :
            direction = new_direction
        elif new_direction == 'down' and direction != 'up' :
            direction = new_direction
        elif new_direction == 'right' and direction != 'left' :
            direction = new_direction
        elif new_direction == 'left' and direction != 'right' :
            direction = new_direction
        else :
            pas_confirme = True
            return
    else :
        pas_confirme = True
        return
    pas_confirme = False

# ends game, loads game over screen
def game_over():
    global g_over
    canvas.delete(ALL)
    g_over = True
    if score > hscore :
        canvas.create_text(WIDTH//2,HEIGHT//2-50, text=f"NEW HIGH SCORE : {score}", font=('consolas', 15), fill = 'red')
    canvas.create_text(WIDTH//2,HEIGHT//2, text="GAME OVER", font=('consolas', 30), fill = 'White')
    blink()

# makes game over sreen blink
def blink():
    global var
    if g_over :
        if var :
            canvas.create_text(WIDTH//2,HEIGHT//2+50, text="<Press ENTER>", font=('consolas', 15), fill = 'White', tag='tt')
            var = False
        else :
            canvas.delete('tt')
            var = True
        root.after(500, blink)
    else :
        canvas.delete('tt')

# checks if the snek collides with itself or the border (returns True or False)
def check_collision():
    global snake_pos
    x, y = snake_pos[0][0], snake_pos[0][1]
    if (x < 0 or x > WIDTH-SIZE) or (y < 0 or y > HEIGHT-SIZE) :
        return True
    for i in snake_pos[1:]:
        if i == snake_pos[0] :
            return True
    return False

# allows player to start a fresh game if they died
def new_game(event):
    global score, snake_pos, direction, pas_confirme, g_over, snake, food, xf, yf, food, x, y, hscore
    if not g_over :
        return
    g_over = False
    if score > hscore :
        hscore = score
    score = 0
    label.configure(text=f"High Score : {hscore} | Score : {score}")
    direction = 'down'
    pas_confirme = True
    canvas.delete(ALL)
    snake_pos = []
    for i in range(BODY_PARTS):
        snake_pos.append([0,0])
    for x,y in snake_pos:
        snake = canvas.create_rectangle(x, y, x+WIDTH//SIZE, y+WIDTH//SIZE, fill=SNAKE_COLOR, outline=SNAKE_COLOR, tag="snake")
    xf = WIDTH//SIZE * randint(0, SIZE-1)
    yf = HEIGHT//SIZE * randint(0, SIZE-1)
    food = canvas.create_oval(xf, yf, xf+WIDTH//SIZE, yf+WIDTH//SIZE, fill=FOOD_COLOR, outline=FOOD_COLOR, tag="food")
    next_turn()

    
# binding keys zqsd and arrows to movement function
root.bind('<z>', lambda event: change_direction('up'))
root.bind('<q>', lambda event: change_direction('left'))
root.bind('<s>', lambda event: change_direction('down'))
root.bind('<d>', lambda event: change_direction('right'))
root.bind('<Up>', lambda event: change_direction('up'))
root.bind('<Left>', lambda event: change_direction('left'))
root.bind('<Down>', lambda event: change_direction('down'))
root.bind('<Right>', lambda event: change_direction('right'))

# binding new game key
root.bind('<Return>', new_game)

# starts the loop
next_turn()

# launches the window
root.mainloop()