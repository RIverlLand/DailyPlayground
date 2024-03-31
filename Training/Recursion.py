from typing import List
class Solution:
    def permute(self , num: List[int]) -> List[List[int]]:
        # write code here
        result = []
        self.recursion(result, num, 0)
        return result

    def recursion(self, result, num, index):
        if index == len(num):
            result.append(num.copy())
        for i in range(index, len(num)):
            num[i], num[index] = num[index], num[i]
            self.recursion(result, num, index + 1)
            num[i], num[index] = num[index], num[i]

solution = Solution()
print(solution.permute([1, 2, 3]))

# from typing import List

# class Solution:
#     def permute(self, num: List[int]) -> List[List[int]]:
#         result = []
#         self.recursion(result, num, 0)
#         return result

#     def recursion(self, result, num, index):
#         if index == len(num):
#             result.append(num.copy())  # Append a copy of num
#         for i in range(index, len(num)):
#             num[index], num[i] = num[i], num[index]  # Swap elements
#             self.recursion(result, num, index + 1)
#             num[i], num[index] = num[index], num[i]  # Backtrack

# Testing the code