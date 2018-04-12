# -*- coding:utf-8 -*-

# print(bool((0,)))
# x = 255
# print(hex(x))

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-1))


def my_abs_v2(m):
    try:
        x = int(m)
        isinstance(x, int)
        if x >= 0:
            return x
        else:
            return -x
    except ValueError:
            #'print('except:', e)
        return 'it is not a number！'


# print('That`s over')


a = input('Please input a number:')
print(my_abs_v2(a))
