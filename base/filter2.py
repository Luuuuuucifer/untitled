# -*- coding:utf-8 -*-


def is_palindrome(n):
    sn = str(n)
    a = 0
    b = -1
    while sn[a] == sn[b]:
        if (a + 1) >= len(sn) / 2:
            if a - b == len(sn) or a - b == len(sn) - 1:
                return True
            break
        a += 1
        b -= 1

    return False
# 只有在循环内判断才能保证最后ab与len的比较是在计算通过的情况下
# 换句话说，只有循环进行到底，ab与len满足条件的情况下才能得出正确结论

# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
                                                  111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
