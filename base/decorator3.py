# -*- coding: utf-8 -*-


import time
import functools
import datetime


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        print('%s executed in %s ms' % (fn.__name__, datetime.datetime.now()))
        return fn(*args, **kw)

    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


# print(fast(1, 2))
# f = fast(1, 2)
# print(f == 3)
f = fast(11, 22)
s = slow(11, 22, 33)
# print(f)
# print(s)
# print(f == 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
elif f == 33 and s == 7986:
    print('success')

