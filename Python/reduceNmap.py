# -*- coding: utf-8 -*-
# from functools import reduce, map


# 利用map和reduce做个浮点数转换比我想象的要复杂

def str2float(s):
    def turn(x):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

# 定义一个素数生成函数
    
def _odd_iter(): # 生成一个质数的生成器
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n): # 筛选函数，在序列中删除n的倍数用的
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()  # 创建质数序列（偶数不用创建了）
    while True:
        n = next(it) # iterate through the init list
        yield n
        it = filter(_not_divisible(n), it) # 在it中的数字会在filter的过程中被排掉，例如不能被2，3整除的5就会留在序列中，而4不在，不断迭代得到最终的生成器

# 回文序列：
def is_palindrome(n):
    return str(n)==str(n)[::-1]

output = filter(is_palindrome, range(1, 1000)) # 返回1，1000之间数字的回文序列


# sorted 函数的reverse应该就是个可选参数，默认为True?
# sorted 函数的定义式：
# @overload
# def sorted(
#     __iterable: Iterable[SupportsRichComparisonT], *, key: None = None, reverse: bool = False
# ) -> list[SupportsRichComparisonT]: ...