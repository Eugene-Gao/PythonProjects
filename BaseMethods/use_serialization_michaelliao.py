# -*- coding: utf-8 -*-
"""
How to use serialization
Python 语言特定的序列化模块是 pickle，
但如果要把序列化搞得更通用、更符合 Web 标准，就可以使用 json 模块
"""
__author__ = 'Eugene Gao'
__date__ = '2018.05.18'
# **** 操作文件和目录
import os
from datetime import datetime

os_dict = dict()
print(os.name)
print(os.environ.get('PATH'))
print(os.path.abspath('.'))
print(os.path)
print(os.path.join(os.path.abspath('.'), 'testdir'))
print(os.mkdir(os.path.join(os.path.abspath('.'), 'testdir')))
print(os.rmdir(os.path.join(os.path.abspath('.'), 'testdir')))
with open('test.txt', 'w') as f:
    f.write('今天是 ')
    f.write(datetime.now().strftime('%Y-%m-%d'))
print(os.path.split(os.path.join(os.path.abspath('.'), 'test.txt')))
print(os.path.splitext(os.path.join(os.path.abspath('.'), 'test.txt')))
print(os.rename('test.txt', 'test.py'))
print(os.remove('test.py'))

pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))


# **** 序列化
import pickle
# 我们存储相关对象的文件的名称
shoplistfile = 'shoplist.data'
# 需要购买的物品清单
shoplist = ['apple', 'mango', 'carrot']
# 准备写入文件
f = open(shoplistfile, 'wb')
# 转储对象至文件
pickle.dump(shoplist, f)
f.close()
# 清除 shoplist 变量
del shoplist
# 重新打开存储文件
f = open(shoplistfile, 'rb')
# 从文件中载入对象
storedlist = pickle.load(f)
f.close()
print(storedlist)


# **** 利用JSON对象序列化
import json

d = dict(name='Bob', age=20, score=88)
data = json.dumps(d)
print('JSON Data is a str:', data)
reborn = json.loads(data)
print(reborn)

class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score)

s = Student('Bob', 20, 88)
std_data = json.dumps(s, default=lambda obj: obj.__dict__)
print('Dump Student:', std_data)
rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print(rebuild)

