# Island

# 和面试时思考的思路相近，遍历过的格子需要有个标记，但思路差距的地方在于：
# 1. 没有具体到两方向搜索要怎么做，没想到切实可行的递归方案去遍历
# 2. 岛屿沉没不能标记为0，会有风险在于无法区分已遍历的岛屿和未经过的海洋
# 3. 一维的时候是打错了

from typing import List

class Solution:
    def numIslands(self, island: List[List[str]]) -> int:
        output = 0
        for h in range(len(island)):
            for v in range(len(island[0])):
                if island[h][v] == "1":
                    self.recursionIsland(island, h, v)
                    output += 1
        return output

    def recursionIsland(self, island:list, h:int, v:int):
        if h >= len(island) or v >= len(island[0]) or h <= -1 or v <= -1:
            return
    
        if island[h][v] != "1":
            return
        
        island[h][v] = "2"
        self.recursionIsland(island, h, v+1)
        self.recursionIsland(island, h, v-1)
        self.recursionIsland(island, h+1, v)
        self.recursionIsland(island, h-1, v)

s = Solution()
dfs = s.numIslands

print(dfs([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
print(dfs([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
print(dfs([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
print(dfs([["1","0","1","1","0","1","1"], ["1","0","1","1","0","1","0"]]))
print(dfs([["1","0","1","1","0","1","1"]]))