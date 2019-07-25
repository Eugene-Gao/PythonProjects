# -*- coding: utf-8 -*-
"""
How to use doctest
doctest 非常有用，不但可以用来测试，还可以直接作为示例代码。通过
某些文档生成工具，就可以自动把包含 doctest 的注释提取出来。用户
看文档的时候，同时也看到了 doctest
"""
__author__ = 'Eugene Gao'
__date__ = '2018.05.18'
# ****
class Dict(dict):
    '''
    Simple dict but also support access as x.y style.
    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']  # 测试异常的时候，可以用...表示中间一大段烦人的输出
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


if __name__ == '__main__':
    import doctest  # 提取注释中的代码并执行测试。
    doctest.testmod()
    # 什么输出也没有。这说明我们编写的 doctest 运行都是正确的