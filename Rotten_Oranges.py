# https://leetcode.com/problems/rotting-oranges/
class Solution:
    def orangesRotting(self, grid):
        fresh = set()
        rotten = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh.add((i, j))
                elif grid[i][j] == 2:
                    rotten.add((i, j))
        minutes = 0
        direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        while len(fresh) > 0:
            infected = set()
            for rot in rotten:
                i = rot[0]
                j = rot[1]
                for d in direction:
                    nexti = i + d[0]
                    nextj = j + d[1]
                    if (nexti, nextj) in fresh:
                        fresh.remove((nexti, nextj))
                        infected.add((nexti, nextj))

            if len(infected) == 0:
                return -1
            rotten = infected
            minutes += 1
        return minutes






if __name__ == "__main__":
    obj = Solution()
    print(obj.orangesRotting(grid=[[2,1,1],[1,1,0],[0,1,1]]))
    print(obj.orangesRotting(grid=[[0,1]]))
    print(obj.orangesRotting(grid=[[0, 2]]))