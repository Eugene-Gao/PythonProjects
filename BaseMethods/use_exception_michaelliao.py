# -*- coding: utf-8 -*-
"""
How to use Exceptions
Python 内置的 try...except...finally 用来处理错误十分方便。
出错时，会分析错误信息并定位错误发生的代码位置才是最关键的。
程序也可以主动抛出错误，让调用者来处理相应的错误。
但是，应该在文档中写清楚可能会抛出哪些错误，以及错误产生的原因。
"""
__author__ = 'Eugene Gao'
__date__ = '2018.05.18'
# ****
import logging
logging.basicConfig(level=logging.INFO)  # debug, info, warning, error


class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)  # 抛出自定义Exception
    return 10 / n


def bar(s):
    try:
        foo(s)
    except ValueError as e:
        print('ValueError!')
        logging.exception(e)  # 记录Exception信息
        raise  # 抛出当前Exception


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


main()
print('END')