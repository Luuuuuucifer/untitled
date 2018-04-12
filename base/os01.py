# -*- coding:utf-8 -*-


import os

print(os.name)
# posix==>Linux   nt==>windows

print(os.environ)

print(os.environ.get('Path', 'nothing'))

print(os.environ.get('x', 'what is this'))

print(os.path.abspath('.'))

ass = os.path.join('C:/Users/tinker/PycharmProjects/untitled', 'testdir')
print(ass)

# os.mkdir('C:/Users/tinker/PycharmProjects/untitled/testdir')
# os.rmdir('C:/Users/tinker/PycharmProjects/untitled/testdir')

# os.mkdir(ass)
# os.rmdir(ass)
# ass保存的就是一个路径

# os.path.join()
# os.path.split(),os.path.splittext()
# 关于路径要用这两个方法合并和拆分，可以有效解决不同系统的路径问题
# 这里还应该提防文件已经存在的问题

print(os.path.split('C:/Users/tinker/Desktop/123.txt'))
bss = os.path.split('C:/Users/tinker/Desktop/123.txt')
print(bss[1])

