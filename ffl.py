#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'fengf'

# 100+200
# print(100+200+2)

# 输入函数
# name=input('please input your name:')

# 输出函数
# print('my name is:'+name)

# 条件语句
# num1=input('input num1:')
# num2=input('input num2:')

# if num1 > num2:
#	print('num1 >>> num2')
# else:
#	print('num1 <<< num2')


a = 123  # a为int
print(a)
a = 'ABC'  # a为string
print(a)

print('A=', ord('A'))
print('65=', chr(65))

print('ABC'.encode('ascii'))
print('ABC'.encode('utf-8'))

print('fengfeilong-length:', len('fengfeilong'))
print('冯飞龙length：', len('冯飞龙'.encode('utf-8')))

print('我叫：ffl，今年%d岁了' % 25)
print('我叫：%s，今年%d岁了' % ('冯飞龙', 25))
print('增长率：%d %%' % 40)  # 转义%

# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
lastYear = 72
thisYear = 85
pro = thisYear - lastYear
proPercent = pro / lastYear
print('小明成绩提升了：%.1f %%' % (proPercent * 100))

# 集合
jobs = ['程序猿', '律师', '设计师', '服务员']
print(jobs)
print(jobs[0])

fruits = ('orange', 'banana', 'apple', 'pear', 'watermalon')
print(fruits)
print(fruits[2])

# 条件语句
# age = input('请输入年龄：')
# age = int(age)					#input()返回值为str，需转为int类型
# if age >= 18:
# 	print('成年人')
# elif age >= 6:
# 	print('青少年')
# else:
# 	print('儿童')

# 循环语句------------for in循环
for fruit in fruits:
    print('循环水果tuple：' + fruit)

for job in jobs:
    print('循环job：' + job)

# 累加
sum = 0
list = list(range(101))
# print(list)
for x in list:
    sum = sum + x
print('0-100所有整数之和：' + str(sum))  # 打印须将sum通过str()转为str

# 循环语句----------while循环
sum = 100
while sum > 0:
    sum = sum - 10
    print(sum)
    if sum == 50:
        print('遇到50，退出循环')
        break  # 结束循环

sum2 = 10
while sum2 > 0:
    sum2 = sum2 - 1
    if sum2 % 2 == 0:
        continue  # 结束当前循环，继续下轮循环
    print('0-10所有奇数：' + str(sum2))

x = abs
print('-100的绝对值为：' + str(x(-100)))


# 函数
def ffl_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(ffl_abs(-4))


# 空函数占位
def go():
    pass


num = 9
if num > 0:
    pass


# 限定参数类型为int和float
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('参数类型错误！！！')  # 抛出异常
    if x >= 0:
        return x
    else:
        return -x


my_abs(33)


# x的n次方
def go(x, n=2):  # 默认n=2  注意：1.必选参数在前，默认参数在后  2.默认参数必须指向不变对象！
    i = 1
    while n > 0:
        n = n - 1
        i = i * x
    return i


print('5的3次方=' + str(go(5, 3)))
print('5的3次方=', go(5, 3))


# 可变参数：在参数前面加了一个*号，可以传入任意个参数，包括0个参数，接收的是一个tuple
def calc(nums):
    sum = 0
    for x in nums:
        sum = sum + x
    return sum


print('1-4的和为：' + str(calc([1, 2, 3, 4])))


def calc(*nums):
    sum = 0
    for x in nums:
        sum = sum + x
    return sum


print('1-9的和为：' + str(calc(1, 2, 3, 4, 5, 6, 7, 8, 9)))

list = [2, 3, 4]
print('2-4的和为：' + str(calc(*list)))  # *list表示把list这个list的所有元素作为可变参数传进去


# 关键字参数：**参数名(函数内部自动组装为一个dict---key value组合),可以扩展函数的功能
def student(name, gender, **other):
    print('name:', name, 'gender:', gender, 'other:', other)


student('冯飞龙', 'man', age='25', province='HuBei')


# 命名关键字参数：*，前缀，限定参数名
# def student(name, gender, *, city='武汉', age):
#     print(name, gender, city, age)


student('ffl', 'man', city='深圳', age=25)
student('fl', 'man', age=26)


# 参数组合：
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数


# 递归
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(4))

# 切片Slice，针对list和tuple
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nums[0:4]  # 包左不包右
nums[:4]  # 第一个索引是0，还可以省略
nums[-2:]  # 取倒数两个元素
nums[:5:2]  # 前5个数，每两个取一个
nums[::3]  # 所有数，每三个取一个
nums[::-3]  # 所有数，反转，每三个取一个
nums[:]  # 复制一个list

# 迭代
map = {'name': 'fengfeilong', 'age': 25, 'city': 'ShenZhen', 'gender': 'male'}
for key in map:  # 遍历key，dict默认遍历key
    print(key)
for value in map.values():  # 遍历value
    print(value)

# 判断一个对象是否可迭代
from collections import Iterable

a = isinstance('ffl', Iterable)  # str		true
b = isinstance((1, 2, 3), Iterable)  # tuple		true
c = isinstance(123, Iterable)  # int		false
print(a, b, c)

# 请使用迭代查找一个list中最小和最大值，并返回一个tuple
ages = [12, 32, 22, 54, 123, 34]
max = 0
min = 0
for x in ages:
    if x >= max:
        max = x
        min = max
for y in ages:
    if y <= min:
        min = y
print(max, min)

# 生成[1x1, 2x2, 3x3, ..., 10x10]
list = []
for x in range(1, 11):
    list.append(x * x)
print(list)

# 列表生成式
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 1])  # 加入条件判断
print([x + y + z for x in '冯王李' for y in '飞家哟' for z in '龙蝶哈'])  # 多层循环

# 打印出当前目录下所有的文件和文件夹
import os

# print([x for x in os.listdir('.')])


for key, value in map.items():
    print(key, '=', value)

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])

print('FengFeiLong'.lower())  # 小写
print('FengFeiLong'.upper())  # 大写

# 将下面list中包含小写字母的都转成大写字母
list = [123, 'Fengfeilong', 'HAHA', 'GoGoGo']
for x in list:
    if isinstance(x, str):
        print(x.upper())

# generator
g = (x for x in list)
print(g)
for x in g:  # 遍历generator
    print(x)


# print(next(g))

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


fib(6)


# yield关键字，包含yield关键字的函数就是一个generator
# 变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行

# 高阶函数:函数作为参数传入另一个函数中
def add(x, y, z):
    return z(x) + z(y)


a = add(10, -10, abs)
print('高阶函数test：', a)

# map函数：map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
# print('list所有元素转str',list(map(str,[1,2,3,4,5,6,7,8])))

# reduce函数：
from functools import reduce


def add(x, y):
    return x + y


a = reduce(add, [1, 2, 3, 4, 5])
print('reduce求数组的和：', a)

# str转int
dic = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(x):
    return dic[x]


print(str2int('5'))

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
del (list)  # 将之前自定义的变量delete掉,否则会报TypeError: 'dict' object is not callable错误
del (map)


def str2float(s):
    # 传入'123.456'
    s = s.split('.')

    def f1(x, y):
        return x * 10 + y

    def f2(x, y):
        return x / 10 + y

    def str2num(str):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[str]

    return reduce(f1, map(str2num, s[0])) + reduce(f2, list(map(str2num, s[1]))[::-1]) / 10


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

# filter函数：返回的是一个Iterator
L = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def is_odd(x):
    return x % 2 == 0


# del (list)
a = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(a)


# 利用filter去掉空str
def not_empty(x):
    return x.strip()  # strip()函数去掉字符串首尾空格，相当于trim()


print(list(filter(not_empty, ['a', 'b', ' ', '   ', 'c'])))

# 反转字符串
print('冯飞龙反转---->', '冯飞龙'[::-1])

# 排序
newList = [4, 1, 66, 23, -70, 2, -25]
print(sorted(newList))
print(sorted(newList, key=abs))     #根据绝对值排序
print(sorted(newList, key=abs,reverse=True))     #根据绝对值反向排序


def reverse(x):
    return -x


print(sorted(newList, key=reverse))

def lazy_sum(*numbers):
    def get_sum():
        sum = 0
        for x in numbers:
            sum += x
        return sum
    return get_sum


f = lazy_sum(1, 2, 3, 4, 5)
print('1-5的和为：',f())

#闭包：当一个函数返回了一个函数后，其内部的局部变量还被新函数引用
#注意：返回函数不要引用任何循环变量，或者后续会发生变化的变量

#利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    def f():
        n = 0
        while True:
            n = n+1
            yield n
    x = f()
    def counter():
        return next(x)
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 ...


