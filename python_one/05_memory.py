#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020-06-29 
@Author : Yong
@File : 05_memory.py
@Software: PyCharm
"""

import sys


# https://blog.csdn.net/z_feng12489/article/details/89433637

# 无需声明变量类型，不用关心变量存亡，
# 也不关心内存管理，使用引用基数器记录所引用数
# 采用GC垃圾回收机制
# 引用基数器+1 执行完毕后引用销毁，减少一个引用  计数为0 统一回收

# todo: 对象的引用计数+1的情况
"""

1. 对象被创建
>>> import sys
>>> a = 23
>>> sys.getrefcount(a)

这里23这个对象并没有在内存中新建，
因为在Python启动解释器的时候会创建一个小整数池，-5~256之间的这些对象会被自动创建加载到内存中等待调用；
a = 23是为23这个整数对象增加了一个引用。

>>> class MyName():
...     pass
...
>>> sys.getrefcount(MyName())

结果为1，是因为sys.getrefcount(MyName())函数也算一个引用。

2. 对象被引用
>>> a = 3.1415926
>>> b = a
>>> c = b
>>> sys.getrefcount(a)
4
>>> sys.getrefcount(b)
4
>>> sys.getrefcount(c)

每一次赋值都会增加数据操作的引用次数，要记住引用的是变量a,b,c等指向的数据 3.1415926 ，而不是变量本身。

3. 对象被作为参数，传入到一个函数中
>>> a = 3.1415926   # 增加一个引用  count = 1
>>> b = a   # 增加一个引用  count = 2
>>> c = b   # 增加一个引用  count = 3
>>> sys.getrefcount(b)   # 增加一个引用  count = 4   执行完毕后引用销毁，减少一个引用   count = 3
4
>>> sys.getrefcount(c)   # 增加一个引用  count = 4   执行完毕后引用销毁，减少一个引用   count = 3

函数 sys.getrefcount() 调用时 会增加一个引用，调用完又销毁一个引用。 实际上就是实参传给形参的问题。

4. 对象作为一个元素，存储在容器中
>>> a = 3.1415926   # 增加一个引用  count = 1
>>> sys.getrefcount(a)
2
>>> b = a   # 增加一个引用  count = 2
>>> sys.getrefcount(a)
3
>>> list_ = [a, b]   # 增加两个引用  count = 4
>>> sys.getrefcount(a)
5 
"""


# todo : 对象的引用计数-1的情况：

"""

1. 对象的别名被赋予新的对象
>>> a = 3.1415926   # 增加一个引用  count = 1
>>> b = a   # 增加一个引用  count = 2
>>> sys.getrefcount(a)
3
>>> b = -3.1415926   # 原对象减少一个引用  count = 1
>>> sys.getrefcount(a)
2

2. 对象的别名被显式销毁
>>> a = 3.1415926   # 增加一个引用  count = 1
>>> b = a   # 增加一个引用  count = 2
>>> sys.getrefcount(a)
3
>>> del b   # 减少一个引用  count = 1
>>> sys.getrefcount(a)
2

3. 一个对象离开它的作用域
>>> a = 3.1415926   # 增加一个引用  count = 1 
>>> sys.getrefcount(a)   # 增加一个引用  count = 1  ==>   打印 2  ==>  减少一个引用  count = 1
2

a 作为参数传递到 sys.getrefcount(a) 函数中，只在函数中起作用，一旦执行完毕就会销毁。

4. 对象所在的容器被销毁，或从容器中删除对象
>>> a = 3.1415926
>>> sys.getrefcount(a)
2
>>> list_ = [a,1,2,3]
>>> sys.getrefcount(a)
3
>>> del list_
>>> sys.getrefcount(a)
2

"""
# Python启动解释器的时候会创建一个小整数池，-5~256之间的这些对象会被自动创建加载到内存中等待调用；
# 字面常量 常驻内存 引用次数很多
num_1 = 'he54545'

# print(sys.getrefcount(num_1))

num_2 = []

# print(sys.getrefcount(num_2))

# todo: 顺序 分支 循环
"""
顺序  依次进行
分支  if...:else:... 只能进一个分支

"""

score = 50
if score >= 100:
    print("分数不能大与100")
elif score >= 80:
    print("优秀")
elif score >= 70:
    print('良好')
elif score >= 60:
    print('及格')
elif 60 >= score > 0:
    print('不及格')
else:
    print('分数不能小于0')

# 输入数据  阻塞 input 里面的提示符
# 比较大小
"""
a = int(input(">>"))
b = int(input(">>"))
if a > b:
    print('a>b')
else:
    print('a<b')
"""


# 判断数字长度是否大与5位数，并输出位数
c = int(input(">>"))
if c >= 10000:
    print('>=5位')
elif c >= 1000:
    print("4位")
elif c >= 100:
    print("3位")
elif c >= 10:
    print("2位")
else:
    print("1位")

# 条件折半 加快速度
d = int(input(">>"))
if d >= 1000:
    if d >= 10000:
        print('>=5位')
    else:
        print('4位')
else:  # b<1000
    if d >= 100:
        print('3位')
    elif d >= 10:
        print('2位')
    else:
        print('1位')
