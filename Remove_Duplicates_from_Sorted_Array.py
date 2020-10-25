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


    """
    A better approach is to only consider when nums[i] != nums[j]
    and simply perform requried actions
    This approach has higher code readability
    """

    def betterApproach(self, nums):
        i, j = 0, 1
        while j < len(nums):
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i += 1
            j +=1
        return i+1, nums[:i+1]


if __name__ == "__main__":
    obj = Solution()
    print(obj.removeDuplicates(nums=[1,1,1,2,2,3,4]))
    print(obj.betterApproach(nums=[1,1,1,2,2,3,4]))