# -*- coding:utf-8 -*-


def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10/n


def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise
# 这个raise是在捕获了错误之后继续抛出，这样更容易追踪
bar()
