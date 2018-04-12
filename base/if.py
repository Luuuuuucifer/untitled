# -*- coding:utf-8 -*-

#x = 1

try:
    x = input('please input a number:')
    intx = int(x)
except ValueError as e:
    print('WTF!it is not a number')
else:
    print(intx)
finally:
    print('END')




#if isinstance(x, int):
#   print(x)
#else:
#   print('wtf,it is not a number!')
