# https://leetcode.com/problems/number-of-good-pairs/
# https://leetcode.com/problems/number-of-good-pairs/discuss/731561/JavaC%2B%2BPython-Count
from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums):
        count = Counter(nums)
        return sum(num*(num-1)//2 for num in count.values())



if __name__ == "__main__":
    obj = Solution()
    print(obj.numIdenticalPairs(nums=[1,2,3,1,1,3]))