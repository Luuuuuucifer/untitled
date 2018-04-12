# -*- coding:utf-8 -*-


import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        #这个可以让方法的相关信息也换过来
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('2015-3-25')

now()
print(now.__name__)