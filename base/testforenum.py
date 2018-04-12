# -*- coding:utf-8 -*-

# 如果要限制定义枚举时，不能定义相同值的成员。可以使用装饰器@unique【要导入unique模块】
from enum import Enum, unique


# Color = Enum('Color', ('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple'))


@unique
class Color(Enum):
    red = 10
    orange = 2
    yellow = 3
    green = 4
    blue = 5
    indigo = 6
    purple = 7

for name, member in Color.__members__.items():
    print('name:', name, ',member:', member, ',value:', member.value)

for a in Color:
    print(a.name)

b = isinstance(Color.red.value, int)
print(b)
