# -*- coding:utf-8 -*-


def count():
    fs = []
    print(fs)
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
#       fs.append(f())
    return fs

#
f1 = count()
f2 = count()
# print(f1)
print(f1[1]())
print(f2[1]())
# fs.append()里面的f方法，加了括号，返回的就是数字，不加返回的就是方法
#
# # f1, f2, f3 = count()
# print(f1(), f2(), f3())
#  返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。


def count_v2():
    # def f(j):
    #     def g():
    #         return j*j
    #     return g

    def f(j):
        return j * j

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1 = count_v2()
# print(f1[1]())
print(f1)
# 可不可以理解为，count（）中调用的是f，没有给参数，所以没有立即把i传进去
