#!/usr/bin/env python
# encoding: utf-8
'''
@version: python2.7
@author: Yasin
@software: PyCharm
@file: 1(2).py
@time: 2018/4/24 21:58
'''


line=[]
for i in range(123,433):
    a=i%10
    b=(i%100)//10
    c=(i%1000)//100
    if a!=b and b!=c and a!=c  and 0<a<5 and 0<b<5 and 0<c<5 :
        print (i)
        line.append(i)
print('the total is :',len(line))