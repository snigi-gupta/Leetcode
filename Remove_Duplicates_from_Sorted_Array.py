# https://leetcode.com/problems/remove-duplicates-from-sorted-array/


class Solution:
    def removeDuplicates(self, nums):
        i = 0
        j = i + 1
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                nums[i+1] = nums[j]
                i += 1
                j += 1

        return i+1, nums[:i+1]


if __name__ == "__main__":
    obj = Solution()
    print(obj.removeDuplicates(nums=[1,1,1,2,2,3,4]))