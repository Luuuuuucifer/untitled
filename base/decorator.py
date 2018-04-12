# -*- coding:utf-8 -*-

import datetime
import time


def log(func):
    print('text')

    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        print('begin call!time: %s' % datetime.datetime.now())
        return func(*args, **kw)
    # print('end call!time: %s' % datetime.datetime.now())
    return wrapper


@log
def now():
    time.sleep(1)
    print('2017-12-6')
# now = log(now)
now()
print('end call!time: %s' % datetime.datetime.now())

