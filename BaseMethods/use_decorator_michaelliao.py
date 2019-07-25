# -*- coding: utf-8 -*-
"""
How to use decorator
"""
__author__ = 'Eugene Gao'
__date__ = '2018.05.18'
# **** 装饰器，decorator 就是一个返回函数的高阶函数
import functools


def log(func):
    @functools.wraps(func)  # 把func.__name__等属性复制到 wrapper.__name__
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2015-3-25')


now()


def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@logger('DEBUG')
def today():
    print('2015-3-25')


today()
print(today.__name__)
