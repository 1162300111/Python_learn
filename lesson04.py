#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: zhengnanyan
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: 872397486@qq.com
@File : lesson04.py
@Time : 2020/2/22 10:15
@Site : 
@Software: PyCharm
'''
# 需要这样输出：
# 请输入一个整数:5
# 1
# 2
# 3
# 4
# 5

num = input("请输入一个整数: ")
num = int(num)
begin = 1
while(begin <= num):
    print(begin)
    begin = begin+1


# 需要打印这样的图案：
# 请输入一个整数:5
#     *****
#    ****
#   ***
#  **
# *

count = input("请输入一个整数: ")
count = int(count)
while count > 0:
    print(" "*(count-1)+"*"*count)
    count = count-1