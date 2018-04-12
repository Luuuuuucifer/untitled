# -*- coding:utf-8 -*-


class Student(object):
    count = 0

    def __init__(self, name):
        Student.count += 1
        self.name = name

# 思路:找每次创建实例都会调用的方法，然后在其中写入+1，实测成功
# a = Student('A')
# print(Student.count)
# b = Student('B')
# print(Student.count)
# c = Student('C')
# print(Student.count)
# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
