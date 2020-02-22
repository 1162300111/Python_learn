#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: zhengnanyan
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: 872397486@qq.com
@File : lesson01.py
@Time : 2020/2/22 9:15
@Site : 
@Software: PyCharm
'''

#重复打印字符串，用字符串乘法
print("a "*5)

#在一个字符串中嵌入一个双引号
print("我说：\"这是双引号\"")

#在 Python 或 IDLE 中，输入 dir(____builtins____)
# 可以看到 Python 提供的内置方法列表（注意，builtins 前后是两个下划线哦）

# 字符串可以拼接
print("I" + " am "+"zny")

#键盘输入
# name = input('输入你的名字：')
# print("你的名字是："+name)
# print("----------------------")

#在字符串前加r,就可以打印字符串中的反斜杠
s = r'C:\11\2223'+'\\'
print(s)#输出：C:/11/2223//\'

#help(print) # 查看print函数的功能

#and or
print(1 and 3)