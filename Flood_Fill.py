# https://leetcode.com/problems/flood-fill/
# https://www.youtube.com/watch?v=TClRuEZ-uDg
import collections

class Solution:
    def dfs(self, image, i, j, newColor, oldColor):
        if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]) or image[i][j] != oldColor:
            return
        image[i][j] = newColor
        self.dfs(image, i + 1, j, newColor, oldColor)
        self.dfs(image, i - 1, j, newColor, oldColor)
        self.dfs(image, i, j + 1, newColor, oldColor)
        self.dfs(image, i, j - 1, newColor, oldColor)

    def floodfill(self, image, sr, sc, newColor):
        oldColor = image[sr][sc]

        if oldColor == newColor:
            return image
        self.dfs(image, sr, sc, newColor, oldColor)
        return image

    def stack_dfs(self, image, sr, sc, newColor):

        oldColor = image[sr][sc]
        stack = [[sr,sc]]
        seen = set()

        while stack:
            currRow, currCol = stack.pop()
            if (currRow >= 0 and currRow <len(image)) and (currCol >=0 and currCol <len(image[0])) and ((currRow, currCol) not in seen) and (image[currRow][currCol] == oldColor):
                image[currRow][currCol] = newColor
                seen.add((currRow, currCol))
                stack.append([currRow + 1, currCol])
                stack.append([currRow, currCol + 1])
                stack.append([currRow - 1, currCol])
                stack.append([currRow, currCol-1])

        return image

    def queue_bfs(self, image, sr, sc, newColor):
        oldColor = image[sr][sc]
        queue = collections.deque([[sr, sc]])
        seen = set()

        while queue:
            currRow, currCol = queue.popleft()
            if (currRow >= 0 and currRow < len(image)) and (currCol >= 0 and currCol < len(image[0])) and (
                    (currRow, currCol) not in seen) and (image[currRow][currCol] == oldColor):
                image[currRow][currCol] = newColor
                seen.add((currRow, currCol))
                queue.append([currRow + 1, currCol])
                queue.append([currRow, currCol + 1])
                queue.append([currRow - 1, currCol])
                queue.append([currRow, currCol - 1])
        return image


if __name__ == "__main__":
    obj = Solution()
    print(obj.floodfill(image=[[1,1,1],[1,1,0],[1,0,1]], sr=1, sc=1, newColor=2))
    print(obj.stack_dfs(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, newColor=2))
    print(obj.queue_bfs(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, newColor=2))