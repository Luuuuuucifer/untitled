# -*- coding:utf-8 -*-

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = []

for n in L1:
    if isinstance(n, str):
        L2.append(n.lower())

#L2 = [n.lower() for n in L2]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')