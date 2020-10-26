# https://leetcode.com/problems/search-insert-position/


class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        # mid = 0

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # return mid if nums[mid] > target else mid + 1
        """
        when exiting the loop we are already incrementing left = mid+1 if element<target
        So in the last iteration if we do not find target then target should be at left pos.
        Also, if element > target then we are shifting the right ptr and there will be a time
        when mid is smaller than target and again left is incremented before we leave the last loop.
        Hence returning left is justified in case of element not found.
        """
        return left


if __name__ == "__main__":
    obj = Solution()
    print(obj.searchInsert(nums=[1,3,5,6], target=5))
    print(obj.searchInsert(nums=[1,3,5,6], target=2))
    print(obj.searchInsert(nums=[1,3,4,6], target=5))
    print(obj.searchInsert(nums=[1,3,5,6], target=0))
    print(obj.searchInsert(nums=[1], target=0))
    print(obj.searchInsert(nums=[1, 3, 5, 6], target=7))
    print(obj.searchInsert(nums=[1, 3, 5], target=1))
    print(obj.searchInsert(nums=[1], target=1))
