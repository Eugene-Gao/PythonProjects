#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# **** 数据类型
# 1. 没有单独的 long 类型。 int 类型可以指任何大小的整数。
print("Welcome to Python 3.x")
# 2. 如何指定多行字符串
multiLine_str = '''
这是一段多行字符串。 这是它的第一行。
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
'''
print(multiLine_str)
# 3. format用法
age = 20
name = 'Swaroop'
print('{0} was {1} years old when he wrote this book'.format(name, age))
# 4. 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:.3f}'.format(2.0 / 3))
# 5. 使用下划线填充文本， 并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:_^11}'.format('hello'))
# 6. 基于关键词输出 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
# 7. print 总是会以一个不可见的“新一行”字符（ \n ）结尾, 通过 end 指定以空格结尾
print('a', end=' ')
print('b', end=' ')
print('c')
# 8. 转义字符
# \n 表示新一行的开始
# \t 表示制表符
# \放在句尾，表示字符串将在下一行继续， 但不会添加新的一行
# 9. r 或 R 来指定一个 原始（ Raw） 字符串
# 10. ** （乘方），// （ 整除），^（ 按位异或），
var1 = 5
powerVal = var1 ** 3
print(powerVal)
# range(1,5,2) 将会输出 [1, 3]，它不会包括第二个数字在内。
for i in range(1, 5, 2):
    print(i)
else:
    print('The for loop is over')
    print(list(range(5)))

# **** 集合类型
# 1. List是可变的（ Mutable） 而String是不可变的（ Immutable）。
#   List是一种有序的集合，元素的数据类型也可以不同
shoplist = ['apple', 'mango', 'carrot', 'banana']
for fruit in shoplist:
    print('Hello,{fruit}!'.format(fruit=fruit))
# 2. tuple的一大特征类似于字符串， 它们是不可变的（ Immutable）。
#   如果可能，能用 tuple 代替 list 就尽量用 tuple。
#   定义一个空的 tuple
varTuple = ()
print(len(varTuple))
#   单一元素的元组，不能写为 singleton = (2)，定义的不是 tuple，是 1 这个数！
#   只有 1 个元素的 tuple 定义时必须加一个逗号,，来消除歧义
singleton = (2,)
zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))
new_zoo = 'monkey', 'camel', zoo
print('Number of cages in the new zoo is', len(new_zoo))
#   快速创建一个list
print([x * x for x in range(1, 11)])
print([m + n for m in 'ABC' for n in 'XYZ'])  # 使用两层循环，可以生成全排列
print([s.lower() for s in shoplist])  # 所有的字符串变成小写
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])  # 使用两个变量来生成 list
# 3. Dict使用不可变的对象（ 如字符串） 作为字典的键值。
# “ab”是地址（ Address） 簿（ Book） 的缩写
ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}
print("Whether Eugene is in the address book: ", 'Eugene' in ab)
#   获取key对应的value的2种方式
print("Swaroop's address is", ab['Swaroop'])
# 通过 dict 提供的 get 方法，如果 key 不存在，可以返回 None，或者自己指定的 value
print("Swaroop's address is", ab.get('Eugene', 'None'))
#   删除一对键值—值配对的2种方式
del ab['Spammer']
ab.pop('Matsumoto')
print('\nThere are {} contacts in the address-book\n'.format(len(ab)))
#   创建一个 dict 对象的5种方式
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
a == b == c == d == e  # True
#   创建一个set对象，无序和无重复元素的集合
s_set = set(shoplist)
s_set.add('Water lemon')
#   可以重复添加
s_set.add('Water lemon')
#   删除元素
s_set.remove('Water lemon')
#   两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 1, 2, 2, 3, 3])
print(s1)
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)
# 20. 引用赋值和拷贝赋值
# 直接赋值实际是引用赋值，二者同指一个存储单元
reflist = shoplist
del shoplist[0]
print('shoplist is', shoplist)
print('reflist is', reflist)
# 通过生成一份完整的切片制作一份列表的副本，【二者指向不同存储单元】
copylist = shoplist[:]
del copylist[0]
print('shoplist is', shoplist)
print('copylist is', copylist)
delimiter = '_*_'
print(delimiter.join(shoplist))


# **** 函数
# 1. 定义空函数
def nop():
    pass  # 用来作为占位符


# 2. 只有那些位于参数列表末尾的参数才能被赋予默认参数值
#   *param 的星号参数，收集并汇集成一个称为“param”的元组（ Tuple）
#   **param 的双星号参数，收集并汇集成一个名为 param 的字典（ Dictionary）
#   *nums 表示把 nums 这个 list 的所有元素作为可变参数传进去
def total(a=5, *numbers, **phonebook):
    print('a', a)
    # 遍历元组中的所有项目
    for single_item in numbers:
        print('single_item', single_item)
    # 遍历字典中的所有项目
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))
# 3. 函数的第一行逻辑行中的字符串是该函数的 文档字符串（ DocString）
#     第一行以某一大写字母开始， 以句号结束，
#     第二行为空行，
#     第三行开始是任何详细的解释说明。函数的 __doc__
# 4. import moduleName/ from moduleName import argv （不推荐，易产生变量名冲突）
# 5. __name__ == '__main__' 用来判断该模块是为自己所用还是从其它从的模块中导入而来
# 6. dir() 函数能对任何对象工作，del argv 语句移除了一个变量或是属性
# 7. 数据类型检查可以用内置函数 isinstance()实现
import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


n = my_abs(-20)
print(n)

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

# TypeError: bad operand type:
try:
    my_abs('123')
except:
    pass
finally:
    print("bad operand type!")


# 参数定义的顺序必须是：必选参数、默认参数、可变参数/命名关键字参数（*）和关键字参数（**）。
def hello(greeting, *args):
    if (len(args) == 0):
        print('%s!' % greeting)
    else:
        print('%s, %s!' % (greeting, ', '.join(args)))


hello('Hi')  # => greeting='Hi', args=()
hello('Hi', 'Sarah')  # => greeting='Hi', args=('Sarah')
hello('Hello', 'Michael', 'Bob', 'Adam')  # => greeting='Hello', args=('Michael', 'Bob', 'Adam')
names = ('Bart', 'Lisa')
hello('Hello', *names)  # => greeting='Hello', args=('Bart', 'Lisa')


#
def print_scores(**kw):
    print('      Name  Score')
    print('------------------')
    for name, score in kw.items():
        print('%10s  %d' % (name, score))
    print()


print_scores(Adam=99, Lisa=88, Bart=77)

data = {
    'Adam Lee': 99,
    'Lisa S': 88,
    'F.Bart': 77
}

print_scores(**data)


def print_info(name, *, gender, city='Beijing', age):
    print('Personal Info')
    print('---------------')
    print('   Name: %s' % name)
    print(' Gender: %s' % gender)
    print('   City: %s' % city)
    print('    Age: %s' % age)
    print()


print_info('Bob', gender='male', age=20)
print_info('Lisa', gender='female', city='Shanghai', age=18)

#   Python 内置的 enumerate 函数可以把一个 list 变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
# iterate
import collections


def g():
    yield 1
    yield 2
    yield 3

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
    return 'done'

n = fib(10)
for n1 in n:
    print(n1)

print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], collections.Iterable))
print('Iterable? \'abc\':', isinstance('abc', collections.Iterable))
print('Iterable? 123:', isinstance(123, collections.Iterable))
print('Iterable? g():', isinstance(g(), collections.Iterable))

print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], collections.Iterator))
print('Iterator? iter([1, 2, 3]):', isinstance(iter([1, 2, 3]), collections.Iterator))
print('Iterator? \'abc\':', isinstance('abc', collections.Iterator))
print('Iterator? 123:', isinstance(123, collections.Iterator))
print('Iterator? g():', isinstance(g(), collections.Iterator))

# iter list:
print('for x in [1, 2, 3, 4, 5]:')
for x in [1, 2, 3, 4, 5]:
    print(x)

print('for x in iter([1, 2, 3, 4, 5]):')
for x in iter([1, 2, 3, 4, 5]):
    print(x)

print('next():')
it = iter([1, 2, 3, 4, 5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

d = {'a': 1, 'b': 2, 'c': 3}

# iter each key:
print('iter key:', d)
for k in d.keys():
    print('key:', k)

# iter each value:
print('iter value:', d)
for v in d.values():
    print('value:', v)

# iter both key and value:
print('iter item:', d)
for k, v in d.items():
    print('item:', k, v)

# iter list with index:
print('iter enumerate([\'A\', \'B\', \'C\']')
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# iter complex list:
print('iter [(1, 1), (2, 4), (3, 9)]:')
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


# **** 生成器
#   列表生成式的[]改成()，就创建了一个 generator
#   如果一个函数定义中包含 yield，那么它是一个 generator
#   generator 的函数，在每次调用 next()的时候执行，遇到 yield 语句返回，
#   再次执行时从上次返回的 yield 语句处继续执行。
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)
    return 'done'


o_generator = odd()
#   用for调用generator时，得不到 return 语句的返回值，二维for循环，同时遍历同一个generator
for n in o_generator:
    for m in o_generator:
        print('n = %d, m = %d' % (n, m))


# **** map函数
def f(x):
    return x * x
print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# **** reduce函数
from functools import reduce
CHAR_TO_INT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

def str2int(s):
    ints = map(lambda ch: CHAR_TO_INT[ch], s)
    return reduce(lambda x, y: x * 10 + y, ints)


print(str2int('0'))
print(str2int('12300'))
print(str2int('0012345'))

CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0

    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point

    return reduce(to_float, nums, 0.0)


print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))


# **** filter函数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        print('_odd_iter yield value is %d' % (n))
        yield n


def _not_divisible(n):
    print('_not_divisible input args is %d' % (n))
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        print('primes yield value is %d' % (n))
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


for n in primes():
    if n < 1000:
        print(n)
    else:
        break

# **** sorted高阶函数示例
from operator import itemgetter

L = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L))
print(sorted(L, key=str.lower))

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1), reverse=True))


# **** 返回函数
#   返回函数不要引用任何循环变量， 或者后续会发生变化的变量
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f = lazy_sum(1, 2, 4, 5, 7, 8, 9)
print(f)
print(f())


# why f1(), f2(), f3() returns 9, 9, 9 rather than 1, 4, 9?
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())


# fix:
def count():
    fs = []

    def f(n):
        def j():
            return n * n

        return j

    for i in range(1, 4):
        fs.append(f(i))
    return fs


f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())

# **** 匿名函数
#   匿名函数只能有一个表达式，不用写 return，返回值就是该表达式的结果
f = lambda x: x * x

# **** 偏函数 partial function
import functools

int2 = functools.partial(int, base=2)

print('1000000 =', int2('1000000'))
print('1010101 =', int2('1010101'))

# **** 获取对象信息
print('type(123) =', type(123))
print('type(\'123\') =', type('123'))
print('type(None) =', type(None))
print('type(abs) =', type(abs))

import types


def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)


# ****
class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()

print('hasattr(obj, \'x\') =', hasattr(obj, 'x'))  # 有属性'x'吗？
print('hasattr(obj, \'y\') =', hasattr(obj, 'y'))  # 有属性'y'吗？
setattr(obj, 'y', 19)  # 设置一个属性'y'
print('hasattr(obj, \'y\') =', hasattr(obj, 'y'))  # 有属性'y'吗？
print('getattr(obj, \'y\') =', getattr(obj, 'y'))  # 获取属性'y'
print('obj.y =', obj.y)  # 获取属性'y'

print('getattr(obj, \'z\') =', getattr(obj, 'z', 404))  # 获取属性'z'，如果不存在，返回默认值404

f = getattr(obj, 'power')  # 获取属性'power'
print(f)
print(f())


# **** class和instance动态绑定属性和方法
#    __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
#   考虑 from types import MethodType 中 MethodType的用法
class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


class GraduateStudent(Student):
    pass


s = Student()  # 创建新的实例
s.name = 'Michael'  # 绑定属性'name'
s.age = 25  # 绑定属性'age'
# ERROR: AttributeError: 'Student' object has no attribute 'score'
try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:', e)

g = GraduateStudent()
g.score = 99
print('g.score =', g.score)


# **** 使用@property
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
s.score = 60
print('s.score =', s.score)
# ValueError: score must between 0 ~ 100!
s.score = 9999
