# -*- coding:utf-8 -*-


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    # __repr__ = __str__


print(Student('A'))
b = Student('B')
print(b.name)
print(b)


