from tkinter import *
from math import cos, sin

root = Tk()
root.resizable(False, False)
root.title('ice cube')

WIDTH = 550
HEIGHT = 550
LINE_W = 16
DIAMETER = 256
BACKGOUND_COLOR = '#000000'
LINE_COLOR = '#FFFFFF'
a = 128

canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg=BACKGOUND_COLOR)
canvas.grid(row=1,column=0,columnspan=5)

def myfunc():
    print('a')

coord = []
coord2 = []
count = -1
mvar = 4
resolution = 32
ellipses = False
corners = False
arteses = True

def showellipses():
    global ellipses
    if ellipses : ellipses = False
    else : ellipses = True
    load()

def showarteses():
    global arteses
    if arteses : arteses = False
    else : arteses = True
    load()

def showcorners():
    global corners
    if corners : corners = False
    else : corners = True
    load()

aspin = False
def autospin():
    global aspin
    if aspin : aspin = False
    else : 
        aspin = True
        spin()

def spin():
    turn(xdirection)
    if aspin :
        root.after(25, spin)

faces = False
def showfaces():
    global faces
    if faces : faces = False
    else : faces = True
    load()



CheckVar = IntVar()
b1 = Checkbutton(root, text='Show faces', font=('Arial', 10), command=showfaces)
b1.grid(row=0,column=1)
b2 = Checkbutton(root, text='Show ellipses', font=('Arial', 10), command=showellipses)
b2.grid(row=0,column=0)
b3 = Checkbutton(root, text='Show arteses', font=('Arial', 10), command=showarteses)
b3.grid(row=0,column=2)
b3.toggle()
b4 = Checkbutton(root, text='Auto spin', font=('Arial', 10), command=autospin)
b4.grid(row=0,column=4)
b4 = Checkbutton(root, text='Show corners', font=('Arial', 10), command=showcorners)
b4.grid(row=0,column=3)

a1 = 128
a2 = 128
xdirection = 'right'
def turn(direction):
    global a1, a2, xdirection
    xdirection = direction
    if xdirection == 'right' :
        a1 += 2
        a2 -= 2
    else :
        a1 -= 2
        a2 += 2
    load()

def load():
    canvas.delete(ALL)
    var = mvar/10
    ecart = 1-var
    coord = []
    coord2 = []
    count = -1
    for i in range(-a1, a2, 2):
        x = cos((i*3.14)/a)*a + WIDTH//2
        y = sin((i*3.14)/a)*a*var + HEIGHT//2
        if ellipses :
            canvas.create_rectangle(x, y-a*ecart, x+3, y-a*ecart+3, outline='red', fill='red')
            canvas.create_rectangle(x, y+a*ecart, x+3, y+a*ecart+3, outline='green', fill='green')
        count+=1
        if count%32 == 0 :
            if corners :
                canvas.create_rectangle(x-3, y+a*ecart-3, x+3, y+a*ecart+3, outline='red', fill='red')
                canvas.create_rectangle(x-3, y-a*ecart-3, x+3, y-a*ecart+3, outline='green', fill='green')
            coord.append([x, y-a*ecart])
            coord2.append([x, y+a*ecart])

    if arteses :
        for i in range(4):
            canvas.create_line(coord[i][0], coord[i][1], coord[i-1][0], coord[i-1][1], fill='white', width=2)

            canvas.create_line(coord[i][0], coord2[i][1], coord[i-1][0], coord2[i-1][1], fill='white', width=2)

            canvas.create_line(coord[i][0], coord[i][1], coord[i][0], coord2[i][1], fill='white', width=2)

    if faces :
        l = []
        for i in range(4):
            l.append([coord[i-1][0],coord[i-1][1], coord[i][0],coord[i][1], coord2[i][0],coord2[i][1], coord2[i-1][0],coord2[i-1][1]])
        l1 = [[coord2[0][0],coord2[0][1], coord2[1][0],coord2[1][1], coord2[2][0],coord2[2][1], coord2[3][0],coord2[3][1]],
        [coord[0][0],coord[0][1], coord[1][0],coord[1][1], coord[2][0],coord[2][1], coord[3][0],coord[3][1]]]
        canvas.create_polygon(l1[0], fill='yellow')
        load_faces(a2, l)
        canvas.create_polygon(l1[1], fill='blue')

p = 0
z = a2
COULEURS = ('red', 'green', 'cyan', 'orange')
def load_faces(a2, l):
    global p, z
    if z > a2  and (a2)%64  == 32 :
        if p<3 :
            p+=1
        else :
            p=0
    elif z < a2 and (a2)%64 == 32 :
        if p>0 :
            p-=1
        else :
            p=3
    z = a2
    
    canvas.create_polygon(l[p-1], fill=COULEURS[p-1])
    canvas.create_polygon(l[p], fill=COULEURS[p])


sw = False
def switch():
    global sw
    if sw : sw = False
    else : sw = True

def pitch(direction) :
    global mvar
    if direction == 'down' and mvar < 10 :
        mvar += 1
    elif direction == 'up' and mvar > 0 :
        mvar -= 1
    load()

load()

root.bind('<Left>', lambda event : turn('left'))
root.bind('<Right>', lambda event : turn('right'))
root.bind('<Up>', lambda event : pitch('up'))
root.bind('<Down>', lambda event : pitch('down'))
root.bind('<space>', lambda event : autospin())

root.mainloop()