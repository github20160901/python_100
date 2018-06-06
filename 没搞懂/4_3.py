#!/usr/bin/env python
# encoding: utf-8
'''
@version: python3.6
@author: Yasin
@software: PyCharm
@file: 4_3.py
@time: 2018/5/20 20:18

'''

#调用sorted()排序
dict = {"a" : "apple", "b" : "grape", "c" : "orange", "d" : "banana"}
print (dict)
#按照key排序
print (sorted(dict.items(), key=lambda d: d[0]))
#按照value排序
print (sorted(dict.items(), key=lambda d: d[1]))

#字典的浅拷贝
dict = {"a" : "apple", "b" : "grape"}
dict2 = {"c" : "orange", "d" : "banana"}
dict2 = dict.copy()           # 拷贝dict并赋给dict2
print (dict2)

#字典的深拷贝
import copy
dict = {"a" : "apple", "b" : {"g" : "grape","o" : "orange"}}
dict2 = copy.deepcopy(dict)         # 深拷贝
dict3 = copy.copy(dict)              # 浅拷贝
dict2["b"]["g"] = "orange"
print (dict)
print (dict2)
print (dict3)
dict3["b"]["g"] = "orange"
print (dict)
