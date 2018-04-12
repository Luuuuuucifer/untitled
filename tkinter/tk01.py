# -*- coding:utf-8 -*-

import tkinter

window = tkinter.Tk()
window.title('my window')
window.geometry('200x200')
# 很神奇，这里就是字母x
# 窗口内容

on_hit = False
num = 0


def hit_me():
    global on_hit
    global num
    num += 1
    if on_hit is False:
        on_hit = True
        var.set('you hit me %d' % num)
    else:
        on_hit = False
        var.set(num)


# hit_me如果放在后面就会导致b里面的command报错，这个很尴尬，我估计是和python解释有关，一行行解释导致找不到哦啊hit_me

var = tkinter.StringVar()
i = tkinter.Label(window,
                  # text='OMG!this is TK',  # 标签文字
                  textvariable=var,  # 使用textvariable替换text，因为这可以变化
                  bg='green',  # 背景颜色
                  font=('Arial', 12),  # 字体
                  width=15, height=2)  # 标签长宽
i.pack()  # 固定窗口位置

b = tkinter.Button(window,
                   text='hit me',  # 显示按钮文字
                   width=15, height=2,
                   command=hit_me)  # 点击按钮执行的命令
b.pack()  # 按钮位置

window.mainloop()
