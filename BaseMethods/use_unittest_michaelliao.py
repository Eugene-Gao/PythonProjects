# -*- coding: utf-8 -*-
"""
How to use Unit test case
单元测试的测试用例要覆盖常用的输入组合、边界条件和异常
"""
__author__ = 'Eugene Gao'
__date__ = '2018.05.18'
# ****
import unittest


class Dict(dict):

    #   初始化基类信息
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


#   继承unittest.TestCase
class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')  # 调用__init__方法
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'  # 不调用__setattr__方法
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'  # 调用__setattr__方法
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):  # 用于unittest.TestCase的派生类对象
            value = d['empty']  # 不调用__getattr__方法

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty  # 调用__getattr__方法


if __name__ == '__main__':
    unittest.main()
