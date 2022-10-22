# **********
# shooter
# **********

from tkinter import *
from random import randint


root = Tk()
root.resizable(False, False)

HEIGHT = 512
WIDTH = 1024
BACKGROUND_COLOR = '#000000'
SPEED = 16
ENEMY_SPEED = 4
PLAYER_SIZE = 20
ENEMY_SIZE = 16
PLAYER_COLOR = '#FF0000'
ENEMY_COLOR = '#00FF00'
BULLET_COLOR = '#0000FF'
GUN_COLOR = '#FFFFFF'

flicker = True
g_over = False
pos_x = WIDTH//2
pos_y = HEIGHT//2
move = ['none', 'none']
aim = ['right', 'none']
last = ['right', 'none']
gun_x = 0
gun_y = 0
bullets = []
is_shooting = False
spawn_timer = 0
enemies = []
remove_bullet = None
score = 0
spawn_speed = 65
ammos = []
player_ammo = 15
delete_ammo = None
player_lives = 3
player_immunity = False
remove_enemy = None
delay = 0


canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg=BACKGROUND_COLOR)
canvas.pack()

def read_highscore():
    with open('highscore.txt', 'r') as f:
        highscore = f.read()
    return highscore

def write_highscore(highscore):
    with open('highscore.txt', 'w') as f:
        f.write(str(highscore))

highscore = read_highscore()



def restart():
    global score, player_lives, player_ammo, ammos, spawn_speed, enemies, flicker, pos_x,pos_y,move,aim,last,gun_x,gun_y,\
        bullets,is_shooting,spawn_timer,remove_bullet,delete_ammo,player_immunity,g_over, remove_enemy, highscore, delay
    if not g_over : return
    canvas.delete(ALL)
    flicker = True
    g_over = False
    pos_x = WIDTH//2
    pos_y = HEIGHT//2
    move = ['none', 'none']
    aim = ['right', 'none']
    last = ['right', 'none']
    gun_x = 0
    gun_y = 0
    bullets = []
    is_shooting = False
    spawn_timer = 0
    enemies = []
    remove_bullet = None
    score = 0
    spawn_speed = 65
    ammos = []
    player_ammo = 15
    delete_ammo = None
    player_lives = 3
    player_immunity = False
    remove_enemy = None
    highscore = read_highscore()
    delay = 0

    next()
    spawn_enemy()

def next():
    global is_shooting, spawn_timer, spawn_speed, player_immunity, delay
    if is_shooting :
        new_bullet()
        is_shooting = False

    if spawn_timer >= spawn_speed+20 :
        spawn_timer = 0
        spawn_speed -= spawn_speed/20
        #print(spawn_speed)
        spawn_ammo()
        spawn_enemy()
    
    if player_immunity and delay < 60 :
        delay += 1
    else :
        delay = 0
        player_immunity = False
    spawn_timer += 1
    draw_bullets()
    draw_ammo()
    draw_enemies()
    movement()
    draw_player()
    gun_orientation()
    update_lives()
    canvas.delete('score')
    canvas.create_text(WIDTH/2,HEIGHT/8,text=f"Score : {score}   |   Ammo : {player_ammo}/50", fill='#FFFFFF', font=('consolas', 20),tag='score')
    if not g_over :
        root.after(SPEED, next)

def update_lives():
    global player_lives, g_over
    if player_lives < 1:
        g_over = True
        game_over()
    canvas.delete('lives')
    for i in range(3):
        x = WIDTH/2 + (i-1)*25
        y = HEIGHT/20
        if i+1 > player_lives :
            color = '#000000'
        else :
            color = PLAYER_COLOR
        canvas.create_oval(x-10,y-10,x+10,y+10, fill=color, outline='#FFFFFF', width=3, tag='lives')

def draw_player():
    canvas.delete('player')
    if player_immunity :
        wd = '#FFFFFF'
    else :
        wd = '#000000'
    canvas.create_oval(pos_x-PLAYER_SIZE, pos_y-PLAYER_SIZE, pos_x+PLAYER_SIZE, pos_y+PLAYER_SIZE, fill=PLAYER_COLOR,\
        width=3, outline=wd, tag='player')

def gun_orientation():
    global gun_x, gun_y
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
    canvas.create_rectangle(pos_x-5+gun_x, pos_y-5+gun_y, pos_x+5+gun_x, pos_y+5+gun_y, fill=GUN_COLOR, outline='', tag='gun')

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

def direction_y(direction):
    global move
    move[1] = direction

def aim_x(direction):
    global aim
    aim[0] = direction

def aim_y(direction):
    global aim
    aim[1] = direction

def shoot():
    global is_shooting
    is_shooting = True

def new_bullet():
    global bullets, player_ammo
    if player_ammo > 0:
        bullets.append([pos_x, pos_y, gun_x, gun_y, 0])
        player_ammo -= 1

def draw_bullets():
    global bullets, remove_bullet
    canvas.delete('bullet')
    if type(remove_bullet) == int :
        bullets.pop(remove_bullet)
        remove_bullet = None
    if len(bullets) > 0 and bullets[0][4] > 1024:
        bullets.pop(0)
    for i in range(len(bullets)):
        x = bullets[i][0] + bullets[i][2]
        y = bullets[i][1] + bullets[i][3]
        if bullets[i][2] > 0 :
            stage_x = bullets[i][4]
        elif bullets[i][2] < 0 :
            stage_x = -bullets[i][4]
        else :
            stage_x = 0
        
        if bullets[i][3] > 0 :
            stage_y = bullets[i][4]
        elif bullets[i][3] < 0 :
            stage_y = -bullets[i][4]
        else :
            stage_y = 0
        
        if stage_y != 0 and stage_x != 0:
            a = 3
        else :
            a = 2
        if is_enemy_killed(x+stage_x*2/a, y+stage_y*2/a):
            remove_bullet = i
        canvas.create_rectangle(x-4+stage_x*2/a, y-4+stage_y*2/a, x+4+stage_x*2/a, y+4+stage_y*2/a, fill=BULLET_COLOR, tag='bullet')
        bullets[i][4] += 16

def spawn_ammo():
    global ammos
    if (randint(0,1) == 0) or len(ammos) > 2:
        return
    x = randint(WIDTH//6, WIDTH-WIDTH//6)
    y = randint(HEIGHT//6, HEIGHT-HEIGHT//6)
    ammos.append([x,y])

def draw_ammo():
    global ammos, player_ammo, delete_ammo
    canvas.delete('ammo')
    if type(delete_ammo) == int:
        ammos.pop(delete_ammo)
        delete_ammo = None
    for i in range(len(ammos)):
        x = ammos[i][0]
        y = ammos[i][1]
        if (x+PLAYER_SIZE*2 > pos_x and x-PLAYER_SIZE*2 < pos_x) and (y+PLAYER_SIZE*2 > pos_y and y-PLAYER_SIZE*2 < pos_y):
            delete_ammo = i
            player_ammo += 5
        if player_ammo > 50:
            player_ammo = 50
        canvas.create_rectangle(x-10,y-10,x+10,y+10, fill=BULLET_COLOR, outline='#FFFFFF', width=2, tag='ammo')

def spawn_enemy():
    global enemies
    aleatoire = randint(0,4)
    if aleatoire == 0:
        x = randint(0,WIDTH)
        y = -ENEMY_SIZE
    elif aleatoire == 1:
        x = randint(0,WIDTH)
        y = HEIGHT+ENEMY_SIZE
    elif aleatoire == 2:
        x = 0-ENEMY_SIZE
        y = randint(0,HEIGHT)
    else :
        x = WIDTH+ENEMY_SIZE
        y = randint(0,HEIGHT)
    enemies.append([x, y])

def draw_enemies():
    global enemies, player_lives, player_immunity, remove_enemy
    canvas.delete('enemy')
    if type(remove_enemy) == int:
        enemies.pop(remove_enemy)
        remove_enemy = None
    for i in range(len(enemies)):
        if (pos_x+PLAYER_SIZE > enemies[i][0] and pos_x-PLAYER_SIZE < enemies[i][0]) and \
            (pos_y+PLAYER_SIZE > enemies[i][1] and pos_y-PLAYER_SIZE < enemies[i][1]) and not player_immunity:
            player_lives -= 1
            remove_enemy = i
            player_immunity = True
            continue
        dy = (pos_y - enemies[i][1])
        dx = (pos_x - enemies[i][0])
        dist = (dy**2 + dx**2)**(1/2)
        dy /= dist
        dx /= dist
        enemies[i][0] += dx*ENEMY_SPEED
        enemies[i][1] += dy*ENEMY_SPEED
        x = enemies[i][0]
        y = enemies[i][1]


        canvas.create_oval(x-ENEMY_SIZE,y-ENEMY_SIZE,x+ENEMY_SIZE,y+ENEMY_SIZE, fill=ENEMY_COLOR, tag='enemy')

def is_enemy_killed(xb, yb):
    global enemies, score
    for i in range(len(enemies)):
        xe = enemies[i][0]
        ye = enemies[i][1]
        if ((xe-ENEMY_SIZE < xb) and (xe+ENEMY_SIZE > xb)) and ((ye-ENEMY_SIZE < yb) and (ye+ENEMY_SIZE > yb)):
            enemies.pop(i)
            score += 1
            return True
    return False

def game_over():
    global g_over, flicker, highscore
    if not g_over : return
    if score > int(highscore): 
        write_highscore(score)
        highscore = score
    canvas.delete('flicker')
    canvas.create_text(WIDTH/2, HEIGHT/2, font=('consolas', 40), fill='#FFFFFF', text='GAME OVER', tag='flicker')
    canvas.create_text(WIDTH/2, HEIGHT/2-40, font=('consolas', 15), fill='#FF0000', text=f'High Score : {highscore}', tag='flicker')
    if flicker :
        canvas.create_text(WIDTH/2, HEIGHT/2+40, font=('consolas', 20), fill='#FFFFFF', text='<Press Enter>', tag='flicker')
        flicker = False
    else : flicker = True
    if g_over :
        root.after(500, game_over)



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

root.bind('<c>', lambda event : shoot())

root.bind('<Return>', lambda event : restart())

next()

spawn_enemy()

root.mainloop()