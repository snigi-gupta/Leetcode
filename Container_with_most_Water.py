# https://leetcode.com/problems/container-with-most-water/


"""
So the idea is to use two pointers to control the movement over the vertical lines
The area of a retangle = longest side  X shortest side
Keeping the base/distance b/w left and right pointers and considering it as length,
we move our pointer to the next pointer for the shorter vertical lines.
This ensures that even if we are reducing the length, we are keeping the larger vertical line
still in the picture.
We update max_area only when temp_area > max_area.
"""


class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            shortestLine = min(height[left], height[right])
            temp_area = (right - left) * shortestLine
            if temp_area > max_area:
                max_area = temp_area
                # print(f'max-area: {max_area}')
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area


if __name__ == "__main__":
    obj = Solution()
    print(obj.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
    # print(obj.maxArea(height=[1, 1]))
    # print(obj.maxArea(height=[1, 2, 1]))
    # print(obj.maxArea(height=[4, 3, 2, 1, 4]))
    # print(obj.maxArea(height=[1, 8, 5, 3, 7, 8]))
    # print(obj.maxArea(height=[1, 3, 2, 5, 25, 24, 5]))
