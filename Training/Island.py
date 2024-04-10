# Island

# 和面试时思考的思路相近，遍历过的格子需要有个标记，但思路差距的地方在于：
# 1. 没有具体到两方向搜索要怎么做，没想到切实可行的递归方案去遍历
# 2. 岛屿沉没不能标记为0，会有风险在于无法区分已遍历的岛屿和未经过的海洋
# 3. 一维的时候是打错了

from typing import List

class Solution:  # DFS算法，深度优先的主要特征在于回溯，退回和避免走重复的路径，
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


class Solution2: # BFS DFS的深度指的是一直走到最后一个子节点，而BFS的方式是维护一个节点列表，需要遍历的时候在列表中加入接下来要遍历的节点值
    def numIslands(self, grid: [[str]]) -> int:
        def bfs(grid, i, j):
            queue = [[i, j]]
            while queue:
                [i, j] = queue.pop(0)
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                    grid[i][j] = '0'
                    queue += [[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]]  # 最大的区别在于边界条件的处理，BFS会先遍历所有的相邻节点，而DFS会先朝着某个方向前进，直到回溯才会回到其他节点
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0': continue
                bfs(grid, i, j)
                count += 1
        return count
