from tkinter import *

root = Tk()
root.title("Calculator 3000")
root.minsize(310,350)
root.maxsize(310,350)
root.configure(bg='grey')

e = Entry(root, width=50, borderwidth=5, bg='#404040', fg='white')
e.grid(row=0,column=0,columnspan=3)

total = 0
def equals():
    global total
    if e.get() != '' :
        if e.get() not in '+' : total += int(e.get())
        e.delete(0,END)
        e.insert(0, total)
        total = 0
    if e.get() == '69' :
        e.delete(0,END)
        e.insert(0, 'Nice')

def clear():
    global total
    total = 0
    e.delete(0,END)

def add():
    global total
    if str(e.get()) != '' and str(e.get()) != '+' : 
        total += int(e.get())
        e.delete(0,END)
        e.insert(0, '+')

def button_click(number):
    if number == '=':
        equals()
    elif number == 'clear':
        clear()
    elif number == '+':
        add()
    else :
        if e.get() in '+':
            e.delete(0,END)
        e.insert(END,number)



b1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
b2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
b3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
b4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
b5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
b6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
b7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
b8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
b9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
b0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))
b_add =Button(root, text='+', padx=91, pady=20, command=lambda: button_click('+'))
b_clear = Button(root, text='Clear', width=12, pady=20, command=lambda: button_click('clear'))
b_equal = Button(root, text='=', width=27, pady=20, command=lambda: button_click('='))

b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)

b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)

b0.grid(row=4,column=0)

b_clear.grid(row=5,column=0)
b_add.grid(row=4,column=1,columnspan=2)
b_equal.grid(row=5,column=1,columnspan=2)

root.mainloop()


# A faire pour plus tard : Ajouter le -,*,/,²,sqrt et float