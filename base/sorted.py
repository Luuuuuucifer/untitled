# -*- coding:utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。
# print(L[1][0])
# print(L[][1])
def by_name(t):
    T = t[0]
    return T


L2 = sorted(L, key=by_name)
print(L2)
