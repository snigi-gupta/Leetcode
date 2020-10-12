# https://leetcode.com/problems/search-in-rotated-sorted-array/


class Solution:
    def getSmallestIdx(self, nums):
        left, right = 0, len(nums) - 1

        if nums[right] > nums[0]:
            return 0

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[mid + 1]:
                return mid + 1
            elif nums[mid - 1] > nums[mid]:
                return mid

            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1

    def findVal(self, arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == target:
                return arr[mid]
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def search(self, nums, target):

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        idx = self.getSmallestIdx(nums)

        if idx==0:
            val = self.findVal(nums, target)
            return nums.index(val) if val != -1 else -1
        elif target >= nums[0]:
            val = self.findVal(nums[:idx], target)
            return nums.index(val) if val != -1 else -1
        else:
            val = self.findVal(nums[idx:], target)
            return nums.index(val) if val != -1 else -1


if __name__ == "__main__":
    obj = Solution()
    print(obj.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
    print(obj.search(nums=[4,5,6,7,0,1,2], target = 3))
    print(obj.search(nums=[1], target = 0))
    print(obj.search(nums=[1,3], target = 1))
    print(obj.search(nums=[1,3], target = 3))
    print(obj.search(nums=[3,1], target = 3))
