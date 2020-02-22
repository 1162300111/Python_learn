#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: zhengnanyan
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: 872397486@qq.com
@File : lesson05.py
@Time : 2020/2/22 10:39
@Site : 
@Software: PyCharm
'''

#int()取整是暴力截断的
# 要实现四舍五入的办法：在数字后面加0.5
print("5.4: %d" % int(5.4+0.5))
print("5.6: %d" % int(5.6+0.5))

#要判断两个类型是否相同推荐使用 isinstance()。
print(isinstance(23,str))

# 写一个程序，判断给定年份是否为闰年。（注意：请使用已学过的 BIF 进行灵活运用）
year = input("请输入一个年份：")
if(year.count('.')):# while not temp.isdigit():
    print("输入错误")
    year = input("其输入正确年份（整数）：")
year = int(year)
if((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):# if (year/4 == int(year/4)) and (year/100 != int(year/100))
    print("yes")
else:
    print('no')