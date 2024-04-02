#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List

# 双指针：使用两个相同方向（快慢指针）或者相反方向（对撞指针）的指针进行扫描
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # p1, p2 = m-1, n-1
        # tail = m+n-1
        # while p1 >= 0 or p2 >=0:
        #     if p1 == -1 and p2 == -1:
        #         return
        #     if p2 == -1:
        #         nums1[tail] = nums1[p1]
        #         tail-=1
        #         p1-=1
        #         continue
        #     if nums1[p1] > nums2[p2]:
        #         nums1[tail] = nums1[p1]
        #         tail -=1
        #         p1 -=1
        #     if nums1[p1] <= nums2[p2]:
        #         nums1[tail] = nums2[p2]
        #         tail -=1
        #         p2 -=1
        # return
        p1, p2 = m-1, n-1
        tail = m+n-1
        while p1 >= 0 or p2 >=0:
            if p1 == -1:
                nums1[tail] = nums2[p2]
                p2-=1

            elif p2 == -1:
                nums1[tail] = nums1[p1]

                p1-=1

            elif nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]

                p1 -=1
            else:
                nums1[tail] = nums2[p2]
                p2 -=1
            tail -=1

# 偷鸡
# def merge(...)
#         nums1[m:] = nums2
#         nums1.sort()
                
# 最大的问题是if 的逻辑，如果前面的if已经迭代过了不应该再进去后面的if，这就是为什么上面一定要有个continue
# 再仔细想，tail指针其实是完全没有必要的，只要p2和p1相对位置是正确的，可以省掉一整个指针? 
            




s = Solution()

s.merge([2,0], 1, [2], 1)