# -*- coding:utf-8 -*-


# L = ['A','B','C','D','E']
# print(L)
#
# print(L[:])
#
# print(L[2:10:2])
# #从下标为2的开始，取到下标为10的，但不包括10，并且每二个数取一个
# print(L[-5::2])
# 取倒数5个数，每两个取一个

# list，tuple，str均可以切片

def trim(s):
    a = 0
    b = -1
    while a < len(s):
        if not s[a] == ' ':
            break
        else:
            a = a + 1
            # s = s[a:len(s)+1]

    s = s[a:]
    # print(s)

    while b >= -len(s):
        if not s[b] == ' ':
            break
        else:
            b = b - 1
    b = b + 1
    if b == 0:
        return s
    s = s[:b]

    return s
#为什么会这么写呢，因为如果不加上这个的话，s[:0]什么都输出不了

print(trim('     hello'))
# #测试
if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('') != '':
    print('测试失败4!')
elif trim('    ') != '':
    print('测试失败5!')
else:
    print('测试成功!')
