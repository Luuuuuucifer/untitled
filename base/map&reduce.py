# -*- coding:utf-8 -*-
from functools import reduce


def char2num(s):
    return{'0': 0, '1': 1}[s]
# 这是dict的用法

def nums2num(x, y):
    return(10 * x + y)


print(char2num('1'))

s = '101010101'
a = map(char2num, s)
# print(a)
a = reduce(nums2num, map(char2num, s))
print(a)
#map reduce里面的方法都不要加括号，只给一个方法名就行