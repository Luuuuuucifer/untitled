# -*- coding:utf-8 -*-


# def build(x, y):
#     return lambda x, y: (x * x + y * y)
#
# print(build(1, 2)(3, 4))
# 调用每一级函数都要看有没有需求，比如说lambda如果加了xy的需求，那么最后输出的最后面一个括号就需要再添一对数字
# 其实这里应该是return lambda: x*x + y*y，最后只需要build(1,2)()即可

# def is_odd(n):
#     return n % 2 == 1

L = list(filter(lambda n : n % 2 == 1, range(1, 20)))
print(L)
