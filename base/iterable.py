# -*- coding:utf-8 -*-


def findMinAndMax(L):
    if L == []:
        return (None, None)
    else:
        a = L[0]
        # xiao
        b = L[0]
        # da
        # n提前赋值没有任何意义，ab赋值是为了防止list只有一个数
        for n, value in enumerate(L):
            if value < a:
                a = value
            elif value > b:
                b = value

        return (a, b)



# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')