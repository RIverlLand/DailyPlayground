# # 题目：
# # 在第 1 天，有一个人发现了一个秘密。

# # 给你一个整数 delay ，表示每个人会在发现秘密后的 delay 天之后，每天 给一个新的人 分享 秘密。同时给你一个整数 forget ，表示每个人在发现秘密 forget 天之后会 忘记 这个秘密。一个人 不能 在忘记秘密那一天及之后的日子里分享秘密。

# # 给你一个整数 n ，请你返回在第 n 天结束时，知道秘密的人数。

# 2 <= n <= 100
# 1 <= delay < forget <= n

# 示例1：
# 输入：n = 6, delay = 2, forget = 4  1, 1, 2, 2, 4, 
# 输出：5

# 示例2：
# 输入：n = 4, delay = 1, forget = 3  1, 2, 4, 6
# 输出：6

# 示例3：
# 输入：n = 10, delay = 1, forget = 5
# 输出：416


def secret(n, delay, forget):
    ans = [1]
    temp = []
    day = 1
    while day <= n:
        if (day-1) % forget == 0 and day -1 != 0:
            ans[-1] = ans[-1] - temp[0]
            temp.pop(0)
        if day > delay+1:
            p = ans[-1]*2
            temp.append(p - ans[-1])
            ans.append(p)
        day += 1
    return ans[-1]

    # dp = [1,1]

    # for k in range(n-1):
    #     dp.append(0)
    
    # for i in range(1, n+1):
    #     end = min( i+forget,  n+1)
    #     for j in range(i+delay, end):
    #         dp[j] += dp[i]
    
    # re = 0
    # for o in range(n-forget+1, n+1):
    #     re += dp[o]
    # return re


print(secret(4,1,3))
print(secret(10,1,5))
print(secret(6,2,4))