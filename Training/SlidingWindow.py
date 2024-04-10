#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 给定一个含有 n 个正整数的数组和一个正整数 target 。

# 找出该数组中满足其总和大于等于 target 的长度最小的 连续
# 子数组
#  [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        re = []
        for l in range(len(nums) - 1):
            r = l
            flag = True
            sum = nums[r]
            while sum < target:
                r += 1
                if r >= len(nums):
                    flag = False
                    break
                sum += nums[r]
            if flag:
                re.append(r-l+1)
        if re == []:
            re.append(0)
        re.sort()
        return re[0]
    

s = Solution()
s.minSubArrayLen(11, [1,1,1,1,1,1,1,1])
            