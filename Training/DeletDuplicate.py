#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Double pointer
        l = 0
        r = 0
        while r <= len(nums) - 1:
