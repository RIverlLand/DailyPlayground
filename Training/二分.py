# 描述
# 给定一个长度为n的数组nums，请你找到峰值并返回其索引。数组可能包含多个峰值，在这种情况下，返回任何一个所在位置即可。
# 1.峰值元素是指其值严格大于左右相邻值的元素。严格大于即不能有等于
# 2.假设 nums[-1] = nums[n] = 
# −
# ∞
# −∞
# 3.对于所有有效的 i 都有 nums[i] != nums[i + 1]
# 4.你可以使用O(logN)的时间复杂度实现此问题吗？

# 空间复杂度？
# 时间复杂度似乎就是循环的计算次数？for i in range(n) 就是O(n)，O(logN)几乎就是用作二分法的复杂度，因为每次查找，对象都变为n/2, n/2/2, n/2/2/2.... 最终复杂度为n/2^k，此时复杂度为log2N，省略2变为logN


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @return int整型
#
class Solution:
    def findPeakElement(self , nums: List[int]) -> int:
        # write code here
        left = 0
        right = len(nums) - 1
        while left<right:
            mid = int((left+right)/2)
            if nums[mid] - nums[mid+1] > 0:
                right = mid
            else:
                left = mid + 1
        return right