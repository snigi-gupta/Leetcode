# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


class Solution:

    """
    This approach is brute force.
    We are traversing through the entire list to look for a digit
    less than the previous digit, basically finding the dip. The use of sorted is wrong here.
    Hence we need to use a different strategy.
    """
    def findMin(self, nums):
        if len(nums) == 1:
            return nums[0]

        if sorted(nums) == nums:
            return nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                continue
            else:
                return nums[i]

    def binarySearch(self, nums):

        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums)-1

        # No rotation
        if nums[right]>nums[0]:
            return nums[0]

        while left < right:
            # mid = left+right//2
            """
            To find the mid always use the below formula, for right precision. 
            """
            mid = left + (right - left) // 2

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[0]:
                left = mid+1
            else:
                right = mid-1


if __name__ == "__main__":
    obj = Solution()
    # print(obj.findMin(nums=[3, 4, 5, 1, 2]))
    # print(obj.findMin(nums=[3, 7, 8, 20, 50, 0]))
    # print(obj.findMin(nums=[4, 5, 6, 7, 0, 1, 2]))
    # print(obj.findMin(nums=[1, 2]))
    print(obj.binarySearch(nums=[3, 4, 5, 1, 2]))
    print(obj.binarySearch(nums=[3, 7, 8, 20, 50, 0]))
    print(obj.binarySearch(nums=[4, 5, 6, 7, 0, 1, 2]))
    print(obj.binarySearch(nums=[1, 2]))
