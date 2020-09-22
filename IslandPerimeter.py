class Solution:
    def islandPerimeter(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    if i == 0:
                        up = 0
                    else:
                        up = grid[i-1][j]
                    if j == 0:
                        left = 0
                    else:
                        left = grid[i][j-1]
                    if i == rows-1:
                        down = 0
                    else:
                        down = grid[i+1][j]
                    if j == cols-1:
                        right = 0
                    else:
                        right = grid[i][j+1]
                    perimeter += 4-(up+down+left+right)
        return perimeter

    def optimized(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i>0 and grid[i-1][j] == 1:
                        perimeter -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2
        return perimeter

if __name__ == "__main__":
    obj = Solution()
    print(obj.islandPerimeter(grid=[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
    print(obj.optimized(grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))