from tkinter import *
from random import randint



WIDTH = 600
HEIGHT = 600
SIZE = 10
SPEED = 16
PLAYER_SPEED = 4
BACKGROUND_COLOR = '#000000'
E_SIZE = 15
E_COLOR = '#197d00'
E_SPEED = 1

bullet_color = '#666666'
score = 0

root = Tk()

canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg=BACKGROUND_COLOR)
canvas.pack()


def next():
    global is_shooting, countup, bullet_color, damage
    draw_player(xp, yp)
    aim_cursor()
    check_boost()
    if is_shooting :
        create_bullet()
        if (countup >= 1) and (countup < 150):
            boost_player()
            bullet_color = '#ff3108'
            damage = 16
        else :
            bullet_color = '#f2ac44'
            countup = 0
            damage = 4
    draw_bullets()
    if wave_timer():
        new_wave()
    if entity_timer():
        spawn_entity()
    move_entities()
    draw_entities()
    switch()
    timer()
    canvas.lower('aim')
    canvas.lower('bullet')
    canvas.delete('score')
    canvas.create_text(WIDTH/2,HEIGHT/10,text=f'Score : {score}', font=('consolas',20), fill='#FFFFFF', tag='score')
    if not g_over:
        root.after(SPEED, next)

time = 0
time_var = randint(-100,100)
def timer():
    global time, time_var
    if time > 1500 + time_var:
        time = 0
        time_var = randint(-100,100)
        spawn_boost()
    elif len(boosts) < 1 :
        time += 1

def spawn_player():
    global pos_x, pos_y, xp, yp, cur_x, cur_y, is_shooting, bullets
    cur_x, cur_y = WIDTH/2, HEIGHT/2
    xp = 0
    yp = 0
    pos_x = WIDTH/2
    pos_y = HEIGHT/2
    is_shooting = False
    bullets = []

def draw_player(x=0,y=0):
    global pos_y, pos_x
    canvas.delete('player')
    if x != 0 and y != 0 :
        a = 0.66
    else :
        a = 1
    if not (pos_x + x*a > WIDTH-SIZE or pos_x + x*a < SIZE) :
        pos_x += x*a
    if not (pos_y + y*a > HEIGHT-SIZE or pos_y + y*a < SIZE) :
        pos_y += y*a
    canvas.create_oval(pos_x-SIZE,pos_y-SIZE,pos_x+SIZE,pos_y+SIZE, fill='#14535c', width=0, tag='player')

def move_player_x(direction):
    global xp
    xp = direction

def move_player_y(direction):
    global yp
    yp = direction

def motion(event):
    global cur_x, cur_y
    cur_x, cur_y = event.x, event.y

sw = False
def switch():
    global sw
    if sw :
        sw = False
    else :
        sw = True

def aim_cursor():
    global cx, cy
    canvas.delete('aim')
    x_off = cur_x - pos_x
    y_off = cur_y - pos_y
    dist = (x_off**2 + y_off**2)**(1/2)
    if is_shooting :
        if sw :
            a = 20
        else :
            a = 15
    else :
        a = 20

    if dist != 0 :
        cx = pos_x + x_off*a/dist
        cy = pos_y + y_off*a/dist
    else :
        cx = pos_x
        cy = pos_y
    canvas.create_line(pos_x, pos_y, cx, cy, fill='#666666', width=5, tag='aim')

def shoot():
    global is_shooting
    is_shooting = True

def stop_shoot():
    global is_shooting
    is_shooting = False

def create_bullet():
    global bullets
    x1 = pos_x
    y1 = pos_y
    stage = 0
    bullets.append([x1,y1,cx+randint(-20,20)/8-x1,cy+randint(-20,20)/8-y1,stage])

def draw_bullets():
    global bullets, score
    canvas.delete('bullet')
    if len(bullets) < 1:
        return
    if bullets[0][4] > 9:
        bullets.pop(0)
    for i in range(len(bullets)):
        bullets[i][4] += 1
        varx = bullets[i][2]*bullets[i][4]
        vary = bullets[i][3]*bullets[i][4]
        x = bullets[i][0]+varx
        y = bullets[i][1]+vary
        x1 = bullets[i][0]
        y1 = bullets[i][1]
        skip = False
        for u in range(len(entities)):
            ex = entities[u][0]
            ey = entities[u][1]
            for o in range(10):
                if ((ex+E_SIZE*1.5 > x1 + varx*o/10) and (ex-E_SIZE*1.5 < x1 + varx*o/10)) and ((ey+E_SIZE*1.5 > y1 + vary*o/10) and (ey-E_SIZE*1.5 < y1 + vary*o/10)):
                    bullets[i][4] = 10
                    skip = True
                    entities[u][2] -= damage
                    score += damage
                    x = x1 + varx*o/10
                    y = y1 + vary*o/10
                    if entities[u][2] < 0:
                        entities.pop(u)
                    break
            if skip :
                break
        canvas.create_line(bullets[i][0],bullets[i][1],x,y,fill=bullet_color,width=1, tag='bullet')
        
        bullets[i][0] = x
        bullets[i][1] = y


boosts = []
def spawn_boost():
    global boosts
    x = randint(WIDTH/6,WIDTH-WIDTH/6)
    y = randint(HEIGHT/6,HEIGHT-HEIGHT/6)
    boosts.append([x,y])
    draw_boost()
    
def draw_boost():
    canvas.delete('boost')
    for i in range(len(boosts)):
        canvas.create_rectangle(boosts[i][0]-5, boosts[i][1]-5, boosts[i][0]+5, boosts[i][1]+5, fill='#FF0000', width=2, \
        outline='#FFFFFF', tag='boost')

remove_boost = None
def check_boost():
    global remove_boost
    if type(remove_boost) == int:
        boosts.pop(remove_boost)
        remove_boost = None
        draw_boost()
    for i in range(len(boosts)):
        if (boosts[i][0]-SIZE*2 < pos_x and boosts[i][0]+SIZE*2 > pos_x) and (boosts[i][1]-SIZE*2 < pos_y and boosts[i][1]+SIZE*2 > pos_y):
            remove_boost = i
            boost_player()

countup = 0
def boost_player():
    global countup
    countup+=1

e_count = 0
def entity_timer():
    global e_count
    if e_count <= 0 :
        e_count = 5
        return True
    e_count -= 1
    return False

countdown = 0
def wave_timer():
    global countdown
    if countdown <= 0 :
        countdown = 250
        return True
    countdown -= 1
    return False

def new_wave():
    global wcoord
    rand = randint(1,4)
    if rand == 1:
        wcoord = [-SIZE,-SIZE, WIDTH+SIZE,-SIZE]
    elif rand == 2:
        wcoord = [-SIZE,HEIGHT+SIZE, WIDTH+SIZE,HEIGHT+SIZE]
    elif rand == 3:
        wcoord = [-SIZE,-SIZE, -SIZE,HEIGHT+SIZE]
    else :
        wcoord = [WIDTH+SIZE,-SIZE, WIDTH+SIZE,HEIGHT+SIZE]

entities = []
def spawn_entity():
    global entities
    x = randint(wcoord[0],wcoord[2])
    y = randint(wcoord[1],wcoord[3])
    health = 100
    entities.append([x,y,health])

def draw_entities():
    canvas.delete('entity')
    for i in range(len(entities)):
        x = entities[i][0]
        y = entities[i][1]
        g = hex(int(entities[i][2]*255/100))[2:]
        r = hex(int(255 - entities[i][2]*255/100))[2:]
        if len(g) == 1:
            g = '0' + g
        if len(r) == 1:
            r = '0' + r
        canvas.create_oval(x-E_SIZE,y-E_SIZE,x+E_SIZE,y+E_SIZE, fill=f"#{r}{g}00", tag='entity')
        if (x-E_SIZE-SIZE+5 < pos_x and x+E_SIZE+SIZE-5 > pos_x) and \
            (y-E_SIZE-SIZE+5 < pos_y and y+E_SIZE+SIZE-5 > pos_y):
            game_over()

def move_entities():
    global entities
    for i in range(len(entities)):
        x = entities[i][0]
        y = entities[i][1]
        dx = pos_x - x
        dy = pos_y - y
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

g_over = False
def game_over():
    global g_over
    g_over = True
    canvas.create_text(WIDTH/2, HEIGHT/2, fill='#FFFFFF', font=('consolas',30), text='GAME OVER', tag='end')
    canvas.lift('end')

spawn_player()

next()

root.bind('<KeyPress-z>', lambda event: move_player_y(-PLAYER_SPEED))
root.bind('<KeyPress-q>', lambda event: move_player_x(-PLAYER_SPEED))
root.bind('<KeyPress-s>', lambda event: move_player_y(PLAYER_SPEED))
root.bind('<KeyPress-d>', lambda event: move_player_x(PLAYER_SPEED))

root.bind('<KeyRelease-z>', lambda event: move_player_y(0))
root.bind('<KeyRelease-q>', lambda event: move_player_x(0))
root.bind('<KeyRelease-s>', lambda event: move_player_y(0))
root.bind('<KeyRelease-d>', lambda event: move_player_x(0))

root.bind('<ButtonPress-1>', lambda event : shoot())
root.bind('<ButtonRelease-1>', lambda event : stop_shoot())

root.bind('<Motion>', motion)


root.resizable(False, False)
root.mainloop()