# https://leetcode.com/problems/max-area-of-island/
# https://www.youtube.com/watch?v=W8VuDt0eb5c
class Solution:
    def dfs(self, grid, i, j):

        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return 0
        grid[i][j] = 0
        count = 1
        count += self.dfs(grid, i+1, j)
        count += self.dfs(grid, i-1, j)
        count += self.dfs(grid, i, j +1)
        count += self.dfs(grid, i, j-1)

        return count

    def maxAreOfIsland(self, grid):
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.dfs(grid, i, j))

        return max_area



if __name__ == "__main__":
    obj = Solution()
    print(obj.maxAreOfIsland(grid=[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))