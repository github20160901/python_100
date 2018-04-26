#!/usr/bin/env python
# encoding: utf-8
'''
@version: python3.6
@author: Yasin
@software: PyCharm
@file: 3.py
@time: 2018/4/26 14:22

'''

#一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
#重点在于得出一个范围，否则从负无穷到正无穷，无法穷举

#设该数为x：x + 100 = n^2, n^2 + 168 = m^2。
#设m=n+k（不妨设m,n,k均为自然数）：带入m^2-n^2-168，得k^2+2nk=168。
#解得n=84/k - k/2；由于n,k均为自然数，则nk>=1，故1<=k^2<168，故1<=k<=12。

for x in range(1, 13):
    a = 84/x -x/2
    if int(a) == a:
        n = a ** 2 - 100
        print(n)

# 数学问题没看懂



