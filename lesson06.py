#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: zhengnanyan
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: 872397486@qq.com
@File : lesson06.py
@Time : 2020/2/22 11:12
@Site : 
@Software: PyCharm
'''
# 请写一个程序打印出 0~100 所有的奇数
# first = 1
# while first < 10:
#     print(first,end=" ")
#     first = first+2


# 爱因斯坦曾出过这样一道有趣的数学题：有一个长阶梯，若每步上2阶，
# 最后剩1阶；若每步上3阶，最后剩2阶；若每步上5阶，最后剩4阶；
# 若每步上6阶，最后剩5阶；只有每步上7阶，最后刚好一阶也不剩

num = 1
list1 = []
while num < 1000:
    if num % 7 == 0:
        if num % 2 == 1 and num % 3 == 2 and num % 5==4 and num%6==5:
            list1.append(num)
    num = num+1
if list1 is not None:
    print(list1)
else:
    print('no num')

#示例
x = 7
i = 1
flag = 0

while i <= 100:
    if (x%2 == 1) and (x%3 == 2) and (x%5 == 4) and (x%6==5):
        flag = 1
    else:
        x = 7 * (i+1) # 根据题意，x一定是7的整数倍，所以每次乘以7
    i += 1

if flag == 1:
    print('阶梯数是：', x)
else:
    print('在程序限定的范围内找不到答案！')