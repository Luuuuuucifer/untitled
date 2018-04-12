# -*- coding:utf-8 -*-
from contextlib import contextmanager


@contextmanager
def context():
    print('entering the zone')
    try:
        # yield
        print('aaa')
        yield
    except Exception as e:
        print('with an error %s' % e)
        raise e
    else:
        print('with no error')


with context():
    print('----------in context call----------')
