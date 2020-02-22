#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: zhengnanyan
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: 872397486@qq.com
@File : calc.py
@Time : 2020/2/22 9:44
@Site : 
@Software: PyCharm
'''
#编写程序：calc.py 要求用户输入数字并判断，
# 输入符合要求打印“yes”，不符合要求则打印“no”

num = input("请输入一个数字: ")
if(num.isdigit()):
    print('yes')
else:
    print('no')