class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0] * (n+1)
        dp[1] = 1
        p=0
        for i in range(1, n+1):
            for j in range(i+delay, min(i+forget,n+1)):
                dp[j] += dp[i]
        for k in range(n-forget+1, n+1):
            p += dp[k]
        return p%(pow(10,9) + 7)
    
s = Solution()

print(s.peopleAwareOfSecret(425,81,118))