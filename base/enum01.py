# -*- coding:utf-8 -*-

# 很愚蠢的错误，把名字写成了enum，导致后面包的路径有问题
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',  'Nov', 'Dec'))
# 似乎是一个类，名叫Month，成员名字带有Month.，成员自动从1开始赋值

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

print(Month.Jan.value)

# __member__ .items()从何而来
#
