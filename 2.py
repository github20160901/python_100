#!/usr/bin/env python
# encoding: utf-8
'''
@version: python3.6
@author: Yasin
@software: PyCharm
@file: 2.py
@time: 2018/4/25 17:46

'''

#企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？

def sum_bonus():
    l1 = 100000 * 0.1
    l2 = 200000 * 0.075
    l3 = 200000 * 0.05
    l4 = 400000 * 0.03
    profit = input('Please input profit for this mounth: ')
    profit = int(profit)
    if profit <= 100000:
        bonus = l1
    elif 100000 < profit <= 200000:
        bonus = l1 + (profit - 100000) * 0.075
    elif 200000 < profit <= 400000:
        bonus = l1 + l2 + (profit - 200000) * 0.05
    elif 400000 < profit <= 600000:
        bonus = l1 + l2 + l3 + (profit - 400000) * 0.03
    print(bonus)
    1

if __name__ == '__main__':
    sum_bonus()

