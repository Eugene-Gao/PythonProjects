# -*- coding: utf-8 -*-
"""

"""
__author__ = 'Eugene Gao'
__date__ = '2018.08.13'

from collections import namedtuple, deque, Counter

# namedtuple('名称', [属性 list])
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print("namedtuple('Point', ['x', 'y']) is ", (p.x, p.y))
print("the class of p is ", ("Point", isinstance(p, Point)), ("Point", isinstance(p, tuple)))

# deque 是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print("deque is ", q)

# Counter 是一个简单的计数器，例如，统计字符出现的个数
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print(c)