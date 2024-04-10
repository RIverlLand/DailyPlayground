# 将问题拆解为子问题，可以用初状态一步步描述过来的（例如斐波那契数列）
# 子问题需要有界，边界条件由题目给定

class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        dp = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):  # 在执行这一步的时候，基本不存在连续两间房间都不抢的情况，因为边界条件是n-1 和 n-2+now的条件，也就决定了即使有小数字+大数字的组合，也不会由于选了小数字略过了大数字
            dp.append(max(dp[i-1], nums[i]+dp[i-2]))
        return dp[-1]
    
s = Solution()
print(s.rob([1,3,6,2,9,10,25,2,36,37,38]))