# https://leetcode.com/problems/flood-fill/
# https://www.youtube.com/watch?v=TClRuEZ-uDg
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


if __name__ == "__main__":
    obj = Solution()
    print(obj.floodfill(image=[[1,1,1],[1,1,0],[1,0,1]], sr=1, sc=1, newColor=2))