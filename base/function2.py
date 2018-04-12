# -*- coding:utf-8 -*-

# print(all([1]))
# print(all([0]))
# print(any([1]))
# print(any([0]))


def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)


enroll('Sarah', 'F')


def enroll_v2(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enroll_v2('Sarah', 'F')

enroll_v2('Bob', 'M', 7)
enroll_v2('Adam', 'M', city='Tianjin')
# 默认参数必须指向不变对象！！！！
