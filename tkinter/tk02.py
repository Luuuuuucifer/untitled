# -*- coding:utf-8 -*-

import tkinter

window = tkinter.Tk()
window.title('my window2')

window.geometry('500x500')


def insert_point():
    var = e.get()
    t.insert('insert', var)


def insert_end():
    var = e.get()
    t.insert('end', var)


b1 = tkinter.Button(window, text='insert point', width=15, height=3, command=insert_point)
b1.pack()

b2 = tkinter.Button(window, text='insert end', width=15, height=3, command=insert_end)
b2.pack()

e = tkinter.Entry(window, width=200, show='*')
e.pack()

t = tkinter.Text(window, height=3)
t.pack()

window.mainloop()
