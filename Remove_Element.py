# https://leetcode.com/problems/remove-element/


class Solution:
    def removeElement(self, nums, val):
        i = 0
        j = len(nums)-1
        if len(nums) == 1:
            if nums[i] == val:
                return 0, []
        while i <= j:
            if nums[i]==val and nums[j]!=val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            elif nums[i]==val and nums[j]==val:
                j -= 1
            else:
                i += 1
        return i, nums[:i]

    """
    In the above program, our dilemma was that when we swap and the last nums[j] is also equal to val
    then swapping will not help us. Hence we used an elif to tackle that issue.
    A better approach is we replace nums[i] with nums[j] and then decrease the counter of j.
    This way if nums[j] is not equal to val, then we have captured that in nums[i] now. 
    At the same time, if nums[j] is equal to val, then our decreasing j will now change the last element to be j-1
    eg: [4,1,2,3,4] remove 4
        [4,1,2,3,  4] j point to 3 now
        [3,1,2,4,  4] j points to 2 now, and also 3 is moved ahead. i points to 1 and only once more the loop will run
        and then terminate. 
        returning i+1 will give us [3,1,2] and order does not matter.
    
    This approach has higher code readability
    """
    def betterApproach(self, nums, val):
        i, j = 0, len(nums)-1
        while i <= j:
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
            else:
                i += 1
        return i, nums[:i]


if __name__ == "__main__":
    obj = Solution()
    print(obj.removeElement(nums=[3,2,2,3], val=3))
    print(obj.removeElement(nums=[1], val=1))

    print(obj.betterApproach(nums=[3,2,2,3], val=3))
    print(obj.betterApproach(nums=[1], val=1))