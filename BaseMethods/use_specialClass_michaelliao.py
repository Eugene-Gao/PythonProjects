# -*- coding: utf-8 -*-
"""
How to use the special class
"""
__author__ = 'Eugene Gao'

# **** __str__() 和 __repr__()
#   这是因为直接显示变量调用的不是__str__()，而是__repr__()，
# 区别是__str__()返回用户看到的字符串，
# 而__repr__()返回程序开发者看到的字符串，也就是说， __repr__()是为调试服务的
class Student(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__


print(Student('Michael'))
s = Student('Michael')


# **** __iter__() 和 __next__()
#   实现__iter__()方法，返回一个迭代对象
#   迭代对象的__next__()方法拿到循环的下一个值，直到遇到 StopIteration 错误时退出循环
class Fib(object):

    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值

for n in Fib():
    print(n)


# **** __getitem__()
#   要表现得像 list 那样按照下标取出元素，需要实现__getitem__()方法
#   与之对应的是__setitem__()方法，把对象视作 list 或 dict 来对集合赋值。
#   还有一个__delitem__()方法，用于删除某个元素。
class Fib(object):

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib()
print(f[0])
print(f[5])
print(f[100])
print(f[0:5])
print(f[:10])


# **** __getattr__()
#   只有在没有找到属性的情况下，才调用__getattr__，已有的属性
class Chain(object):
    def __init__(self, path=''):
        self._path = path
        print('__init__ is',path)

    @property
    def path(self):
        print('path is', self._path)
        return self._path

    def __getattr__(self, path):
        print('__getattr__ is',path)
        print('--%s/%s--' % (self._path, path))
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        print('__str__ is',self._path)
        return self._path

    __repr__ = __str__


print('output is', Chain('test').status)
print('output is', Chain().status.user.timeline.list)


# **** __call__()
#   定义一个__call__()方法，就可以直接对实例进行调用
#   判断一个对象是否能被调用，能被调用的对象就是一个 Callable 对象
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('Michael')
s()