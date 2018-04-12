# -*- coding:utf-8 -*-


import unittest

from base.mydict import Dict

a = 1
b = 1


class TestDict(unittest.TestCase):
    # a = 1
    # b = 1

    def setUp(self):
        global a
        # a = 1
        print('setUp: %s' % a)
        a += 1

    def tearDown(self):
        global b
        # b = 1
        print('tearDown: %s' % b)
        b += 1

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


if __name__ == '__main__':
    unittest.main()

# 所以，if __name__ == '__main__' 我们简单的理解就是：
# 如果模块是被直接运行的，则代码块被运行，如果模块是被导入的，则代码块不被运行。
# http://blog.konghy.cn/2017/04/24/python-entry-program/
