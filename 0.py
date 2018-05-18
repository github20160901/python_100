#!/usr/bin/env python
# encoding: utf-8
'''
@version: python3.6
@author: Yasin
@software: PyCharm
@file: 0.py
@time: 2018/5/7 19:09

'''

from functools import reduce

def sum(x, y):
    return x + y

print (reduce(sum,range(0,10)))
print (reduce(sum,range(0,10),10))
print (reduce(sum,range(0,0),10))
