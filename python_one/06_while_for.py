#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time : 2020-06-30 
@Author : Yong
@File : 06_while_for.py
@Software: PyCharm
"""

# todo：  While 循环
"""
while True:
    a = int(input('>>'))
    print(a)
    if a > 10:
        # 满足条件退出
        break 

"""

# 确定边界值 分析
"""
flag = 10
while flag:  # 10->1  while 0
    print(flag)
    flag -= 1
"""


# todo : for ...in.. for循环
# range()  当作基数器用  写几就 执行几次
# range()  惰性可迭代对象
"""
for i in range(10):  # range(0,10) 左闭右开  前包后不包  0<= i <10 遍历
    print(i)
    i += 10
    print(i)
"""

for i in range(0, 10, 1):  # range(10) 左闭右开  前包后不包  0<= i <10 遍历
    if i == 5:
        break  # 结束循环
    # print(i)


for i in range(10, 0, -1):  # range[0,10] 左闭右开  前包后不包  0<= i <10 遍历
    if i == 5:
        continue  # 跳过当前循环
    # print(i)


num_a = 12345
w = 10000
for i in range(5):
    # print(num_a//w)  # 12345 /10000 =>1
    num_a = num_a % w  # 12345 % 10000 => num
    w = w // 10  # 1000

num_b = 54321

# for n in range(5):
#     print(num_b % 10)
#     num_b = num_b // 10
#
#


for n in range(5):
    c = num_b//10
    # print(num_b-c * 10)
    num_b = c

w = 10000
num_x = int('01230')
length = 5
flag = False
count = 0

while w:
    t = num_x // w  # 0
    if not flag:  # False
        if t:
            flag = True
        else:
            length -= 1
    if flag:
        # print(t)
        count += 1
    num_x = num_x % w
    w = w // 10
# print(length, '#length')
# print(length, '#count')


# else 子句  for 后面加else  遇到 break 直接跳出 不执行 else
# 循环正常结束 执行 else

for i in range(0):
    print(i)
    if i > 3:
        break
else:
    print('循环结束')