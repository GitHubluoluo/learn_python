#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020-06-29 
@Author : Yong
@File : str.py
@Software: PyCharm
"""


#  在python 中字符串的处理

"""
1. 使用后 双引号 单引号 或者使用 r前缀 或者 使用 三引号保持原格式
"""

str_a = 'a'
str_b = "b"
str_c = r'hello'
str_d = """
php
python
java
"""
# print(str_d)

"""
2. 转义字符  \n \r 如果要输出反斜杠加 \\ 
"""
str_f = 'a\nc'

# print(str_f)

"""
3. python 语法格式 使用tab 缩进   使用井号# 或者 三引号 注释 
 / 正斜杠强制换行 一行写不下了
"""

# 这是单行注释

"""
这是 多行注释
"""


"""
4. python 标识符 
    数字字母下划线，不可以数字开头，大小写敏感，
    不能使用关键字 def str
    命名要有意义  userName
    python 变量，函数使用小驼峰命名，类使用大驼峰  
    python 中赋值即定义
"""
a = 123
numOne = 234
_a = 789  # 下划线开头 私有变量
A = 456  # 大写常量
# print(A)

"""
5. python 动态语言 强类型 数据类型需要强制转化
   
"""

str_g = 'str'+str(1)

print(str_g)

