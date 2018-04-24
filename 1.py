#!/usr/bin/env python
# encoding: utf-8
'''
@version: python2.7
@author: Yasin
@software: PyCharm
@file: 1.py
@time: 2018/4/24 19:56
'''
#有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
l = []
for n in range(1,5):
    b = n * 100
    for n1 in range(1,5):
        if n1 == n:
            pass
        else:
            s = n1 * 10
            for n2 in range(1,5):
                if n2 == n or n2 == n1:
                    pass
                else:
                    g = n2
                    z = b + s + g
                    l.append(z)
print l
print len(l)

