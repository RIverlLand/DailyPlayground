#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for r in range(len(nums)):
            if nums[r] == val:
                pass
            else:
                nums[l] = nums[r]
                l+=1
        return l

s = Solution()
s.removeElement([3], 2)