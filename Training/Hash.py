class Solution:
    def MoreThanHalfNum_Solution(self , numbers) -> int:
        # write code here
        dic = {}
        i = 0
        while i <= len(numbers) -1:
            if numbers[i] in dic:
                dic[numbers[i]] += 1
            else:
                dic[numbers[i]] = 1
            if dic[numbers[i]] > int(len(numbers)/2):
                return numbers[i]
            i +=1
            
s = Solution()
a = s.MoreThanHalfNum_Solution([1])
pass

# Ditch 牛客 after this