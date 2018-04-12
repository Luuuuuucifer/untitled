# -*-coding:utf-8 -*-


# 汉诺塔
def move(n, a, b, c):
    if n == 1:
        print(a, '- - >', c)
    elif n > 1:
        move(n - 1, a, c, b)
        print(a, '- - >', c)
        move(n - 1, b, a, c)


# 测试
move(3, 'A', 'B', 'C')
move(5, 'A', 'B', 'C')
