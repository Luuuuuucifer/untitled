# -*- coding:utf-8 -*-


import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

i = tk.Label(window, bg='yellow', width=20, text='empty')
i.pack()


def print_selection(v=None):
    i.config(text='you have selected ' + v)


s = tk.Scale(window, label='try me', from_=5, to_=11, orient=tk.HORIZONTAL,
             length=200, showvalue=0, tickinterval=1, resolution=0.01, command=print_selection)
s.pack()

window.mainloop()
