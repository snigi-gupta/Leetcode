# https://leetcode.com/problems/single-number/

from collections import defaultdict


class Solution:
    def singleNumber(self, nums):
        hash_map = defaultdict(int)

        for num in nums:
            hash_map[num] += 1

        for key, val in hash_map.items():
            if val < 2:
                return key


if __name__ == "__main__":
    obj = Solution()
    print(obj.singleNumber(nums=[2,2,1]))