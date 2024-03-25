# -*- coding: utf-8 -*-
from functools import reduce, map

# 利用map和reduce做个浮点数转换比我想象的要复杂

def str2float(s):
    def turn(x):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')