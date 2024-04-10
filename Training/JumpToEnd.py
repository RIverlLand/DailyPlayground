from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # for i in range(len(nums) - 1):
        #     if nums[i] == 0:
        #         if nums[i-1] == 1 or i == 0:
        #             return False
        #     elif nums[i] >= len(nums) - 1 - i:
        #         return True
        # return True
        far = 0
        for i in range(len(nums) -1):
            temp = i + nums[i]
            if temp > far:
                far = temp
            if nums[i] == 0 and temp == far:
                return False
        return True
    

s = Solution()
print(s.canJump([5,9,3,2,1,0,2,3,3,1,0,0]))