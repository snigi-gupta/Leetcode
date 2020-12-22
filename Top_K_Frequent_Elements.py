# https://leetcode.com/problems/top-k-frequent-elements/
from collections import Counter
from itertools import chain


class Solution:
    def topKFrequent(self, nums, k):

        bucket = [[] for _ in range(len(nums) + 1)]

        count = Counter(nums)

        for f, c in count.items():
            bucket[c].append(f)
        all_elements = list(chain(*bucket))

        return all_elements[::-1][:k]


if __name__ == "__main__":
    obj = Solution()
    print(obj.topKFrequent(nums=[1,1,1,2,2,3], k=2))