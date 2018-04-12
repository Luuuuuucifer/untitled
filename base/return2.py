# -*- coding:utf-8 -*-


def createCounter():
    a = 0
    print(a)

    def counter():
        nonlocal a
        a += 1
        print('执行循环')
        print(a)
        # b = a + 1
        return a

    return counter


counterA = createCounter()
# 在这里调用这个方法,a就被赋予0，以后counterA始终都用这个
print(counterA(), counterA(), counterA(), counterA(), counterA())
print(counterA())

counterB = createCounter()
print(counterA())
# 这里可以发现B用的a和A的a不是一个
