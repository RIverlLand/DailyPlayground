#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        for i in range(len(nums)):
            if i == val:
                nums.pop(i)
                continue
            else:
                i+=1

s = Solution()
s.removeElement([3,2,2,3], 3)