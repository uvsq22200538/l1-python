from tkinter import *
from turtle import end_fill

root = Tk()


def buttonPress(number) :
    if ((e.get() == '') or (str(e.get())[-1] in '1234567890.')) and str(number) not in '+-*/' :
        e.insert(END, str(number))

    elif str(e.get())[-1] in '+-*/' :
        e_op.delete(0, END)
        e_op.insert(END, e.get())
        e.delete(0, END)
        e.insert(END, str(number))

    else :
        e_last.delete(0, END)
        e_last.insert(END, e.get())
        e.delete(0, END)
        e.insert(END, str(number))
        e_op.delete(0, END)
        e_op.insert(END, e.get())


def entry_delete_last() :
    if str(e.get())[-1] in '1234567890.' :
        e.delete(int(len(str(e.get())))-1, END)

def clear() :
    e_last.delete(0, END)
    e_op.delete(0, END)
    e.delete(0, END)

def equals() :
    baltazar = float(e.get())
    if (str(e.get())[-1] in '1234567890') and (len(str(e_last.get())) > 0) and (len(str(e_op.get())) == 1) :
        e.delete(0,END)
        if str(e_op.get()) == '+' :
            e.insert(0, float(e_last.get()) + baltazar)
        elif str(e_op.get()) == '-' :
            e.insert(0, float(e_last.get()) - baltazar)
        elif str(e_op.get()) == '*' :
            e.insert(0, float(e_last.get()) * baltazar)
        elif str(e_op.get()) == '/' :
            e.insert(0, "{:.2f}".format(float(e_last.get()) / baltazar))
    else :
        e.delete(0,END)
        e.insert(0, "{:.2f}".format(baltazar))
    e_op.delete(0,END)
    e_last.delete(0,END)
        

menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff=0)

file_menu.add_command(label="Effacer", command=clear)
file_menu.add_command(label="Quitter", command=root.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)


e = Entry(root, borderwidth=10, bg='black', fg='white', width=26, font=('Arial', 20))
e_last = Entry(root, borderwidth=10, bg='black', fg='red', width=19, font=('Arial', 20))
e_op = Entry(root, borderwidth=10, bg='black', fg='red', width=5, font=('Arial', 20))

b1 = Button(root, width=13, height=5, command=lambda: buttonPress(1), text='1')
b2 = Button(root, width=13, height=5, command=lambda: buttonPress(2), text='2')
b3 = Button(root, width=13, height=5, command=lambda: buttonPress(3), text='3')

b4 = Button(root, width=13, height=5, command=lambda: buttonPress(4), text='4')
b5 = Button(root, width=13, height=5, command=lambda: buttonPress(5), text='5')
b6 = Button(root, width=13, height=5, command=lambda: buttonPress(6), text='6')

b7 = Button(root, width=13, height=5, command=lambda: buttonPress(7), text='7')
b8 = Button(root, width=13, height=5, command=lambda: buttonPress(8), text='8')
b9 = Button(root, width=13, height=5, command=lambda: buttonPress(9), text='9')

b0 = Button(root, width=28, height=5, command=lambda: buttonPress(0), text='0')

b_add = Button(root, width=13, height=5, command=lambda: buttonPress('+'), text='+')
b_subtract = Button(root, width=13, height=5, command=lambda: buttonPress('-'), text='-')
b_multiply = Button(root, width=13, height=5, command=lambda: buttonPress('*'), text='*')
b_divide = Button(root, width=13, height=5, command=lambda: buttonPress('/'), text='/')
b_delete = Button(root, width=13, height=5, command=entry_delete_last, text='Del')
b_clear = Button(root, width=13, height=5, command=clear, text='Clear')
b_equals = Button(root, width=13, height=11, command=equals, text='=')
b_comma = Button(root, width=13, height=5, command=lambda: buttonPress('.'), text='.')

e.grid(row=1, column=0, columnspan=4, pady=5, padx=5)
e_last.grid(row=0, column=0, pady=5, padx=5, columnspan=3)
e_op.grid(row=0, column=3, pady=5, padx=5)

b1.grid(pady=5, row=5, column=0)
b2.grid(pady=5, row=5, column=1)
b3.grid(pady=5, row=5, column=2)

b4.grid(pady=5, row=4, column=0)
b5.grid(pady=5, row=4, column=1)
b6.grid(pady=5, row=4, column=2)

b7.grid(pady=5, row=3, column=0)
b8.grid(pady=5, row=3, column=1)
b9.grid(pady=5, row=3, column=2)

b0.grid(pady=5, row=6, column=0, columnspan=2)

b_add.grid(pady=5, row=4, column=3)
b_subtract.grid(pady=5, row=3, column=3)
b_multiply.grid(pady=5, row=2, column=2)
b_divide.grid(pady=5, row=2, column=1)
b_delete.grid(pady=5, row=2, column=3)
b_clear.grid(pady=5, row=2, column=0)
b_equals.grid(pady=5, row=5, column=3, rowspan=2)
b_comma.grid(pady=5, row=6, column=2)

root.title('Calculatrix 5000')
root.configure(bg='grey', menu=menu_bar)
root.resizable(False, False)

root.mainloop()