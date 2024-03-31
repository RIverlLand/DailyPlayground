#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def Permutation(self , strlist: str) -> List[str]:
        # write code here
        re = set()  # 原来 re = []
        string = []
        for i in strlist:
            string.append(i)
        self.recursion(re, string, 0)
        return sorted(re) # 由于set类型不可以直接subscribe，需要sorted转成list

    def recursion(self, re, strlist: set, index):
        if index == len(strlist):
            re.add(''.join(strlist)) # 好好看好好学
        for i in range(index, len(strlist)) :
            if strlist[i] != strlist[index] or i == index:  # So that the loop can keep going!!! otherwise it will stop at a place it shouldn't
                # ! 但是由于 i == index的存在，例如aabb这种有两个重复存在的字符就容易依然有duplicate输出。所以最开始的list可以用set来规避这个问题
                strlist[i], strlist[index] = strlist[index], strlist[i]
                self.recursion(re, strlist, index+1)
                strlist[i], strlist[index] = strlist[index], strlist[i]

s = Solution()
print(s.Permutation('abcbd'))
