# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/discuss/524865/Clean-Python-3-sorting-and-counting

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        count_dict = {}
        for i, n in enumerate(sorted(nums)):
            if n not in count_dict:
                count_dict[n] = i

        return [count_dict[n] for n in nums]


if __name__ == "__main__":
    obj = Solution()
    print(obj.smallerNumbersThanCurrent(nums=[8,1,2,2,3]))