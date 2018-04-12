# -*- coding:utf-8 -*-

def normalize(name):
    name1 = name[:1]
    name2 = name[1:]
    # name3 = ''

    print(name1)
    print(name2)
    # print(isinstance(name2, str))
    name1 = name1.upper()
    name2 = name2.lower()

    print(name1)
    print(name2)
    return name1 + name2

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


