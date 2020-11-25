# https://leetcode.com/problems/move-zeroes/submissions/


class Solution:

    def __init__(self, nums):
        self.nums = nums

    def moveZeroes(self):
        """
        Do not return anything, modify nums in-place instead.
        """
        nums = self.nums
        ptr1 = 0
        ptr2 = 0
        while ptr2 < len(nums):
            if nums[ptr2] != 0:
                nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1]
                ptr1 += 1
            ptr2 += 1
        return nums


if __name__ == "__main__":
    obj = Solution(nums=[0,1,0,3,12])
    print(obj.moveZeroes())