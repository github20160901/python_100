#!/usr/bin/env python
# encoding: utf-8
'''
@version: python2.7
@author: Yasin
@software: PyCharm
@file: 1(1).py
@time: 2018/4/24 21:30
'''
#http://www.wklken.me/posts/2013/08/20/python-extra-itertools.html  itertools用法
import itertools

DataIn = list('1234')
TmpList = []
for x in list(itertools.combinations(DataIn,3)):
    TmpList = TmpList + list(itertools.permutations(x,3))
for i in TmpList:
    print(''.join(i))
