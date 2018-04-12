# -*- coding:utf-8 -*-


class Base(object):
    def __init__(self):
        print('Base create')


class ChildA(Base):
    def __init__(self):
        print('A create')


class ChildB(Base):
    def __init__(self):
        print('B create')
        # super().__init__()


base = Base()
a = ChildA()
b = ChildB()

