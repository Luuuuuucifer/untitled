# -*- coding:utf-8 -*-


def triangles():
    # 思路错了，应该循环
    # get新思路，list末尾添加一个0，从而使得除了第一位、后面每位都是两项之和
    l = [1]
    while True:
        yield list(l)
        # print(l)
        # yield l
        l.append(0)
        # m = l
        m = list(l)
        #非常重要，m=l时，两个指向同一个数组
        for i in range(len(m)):
            l[i] = m[i] + m[i-1]

# for a in triangles(2):
#     print(a)
# 非常重要，当有yield时，triangles（4）已经不再是一个值，而是一个iterable对象，需要用for循环来取值
# triangles(4)
# 测试
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
