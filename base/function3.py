# -*- coding:utf-8 -*-

# a*a+b*b+c*c
def calc(numbers):
    s = 0
    for n in numbers:
        s = s + n * n
    return s


print(calc((1, 2, 3)))


def calc_v2(*numbers):
    s = 0
    for n in numbers:
        s = s + n * n
    return s


print(calc_v2(1, 2))
print(calc_v2())
print(calc_v2(*(1, 2)))
