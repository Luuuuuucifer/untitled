# -*- coding: utf-8 -*-
from functools import reduce

def str2float(s):
    i = getpoint(s)
    if i == len(s)-1:
        return str2int(s)
    else:
        str1 = s[:i]
        str2 = s[i+1:]
        # print(str1)
        # print(str2)
        return str2int(str1)+str2int(str2)/pow(10, len(str2))

def getpoint(s):
    i = 0
    while s[i] != '.':
        i += 1
    return i

def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(fn, map(char2num, s))

#
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

# print(str2float('1234.56789'))
# 直接getpoint，去掉小数点之后str2int，最后除去10的N次方
# getpoint方法其实可以用list解决，list.index('.')效果相同，不过要转成list