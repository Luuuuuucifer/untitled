# -*- coding:utf-8 -*-


# stringio是在内存中读str
from io import StringIO

f = StringIO('Hello\nHi\nGoodbye')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

#  奇怪了，为什么s==None不行。猜测这是readline不会为none

# f.seek()这里是stream position问题
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431918785710e86a1a120ce04925bae155012c7fc71e000#0
