# -*- coding:utf-8 -*-

from types import MethodType


class Student(object):
    pass


def set_name(self, name):
    self.name = name

# 方法绑到类上和帮到实例上会有不同，
# 将方法绑定在类上，会导致后面的值覆盖前面的值
Student.set_name = MethodType(set_name, Student)
s1 = Student()
s2 = Student()
s3 = Student()
s1.set_name('tom')
print(s1.name)
s2.set_name('tony')

# print(s1.name, s2.name)
print(s1.name, s2.name, s3.name)
