import copy
class Solution:
    def flipAndInvertImage(self, img):
        print("array", img)
        flipped_image = copy.deepcopy(img)
        center = int(len(img[0])/2)
        # flipping the image
        for i in range(len(img)):
            for j in range(center):
                flipped_image[i][j] = img[i][(len(img[i])-1)-j]
                flipped_image[i][(len(img[i])-1)-j] = img[i][j]

        for i in range(len(img)):
            for j in range(len(img[0])):
                flipped_image[i][j] = 1 if flipped_image[i][j] == 0 else 0
        return flipped_image

    def optimized(self, img):
        rows = len(img)
        cols = len(img[0])
        flipped_image = img
        for row in range(rows):
            flipped_image[row] = img[row][::-1]
            for col in range(cols):
                flipped_image[row][col] ^= 1
        return flipped_image

if __name__ == "__main__":
    # image = [[1, 1, 0], [0, 1, 0], [0, 0, 0]]
    image = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    # ans [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
    obj = Solution()
    # print(obj.flipAndInvertImage(image))
    print(obj.optimized(image))