class Solution:
    def isPalindrome(self, s: str) -> bool:
        input = [i.lower() for i in s if i.isalpha()]
        l = 0
        r = len(input) - 1
        while l <= r:
            if input[l] != input[r]:
                return False
            l +=1
            r -=1
        return True
    
s = Solution()
s.isPalindrome("A man, a plan, a canal: Panama")