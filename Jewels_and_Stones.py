# https://leetcode.com/problems/jewels-and-stones/
# https://leetcode.com/problems/jewels-and-stones/discuss/113553/C%2B%2BJavaPython-Set-Solution-O(J-%2B-S)

from collections import defaultdict
class Solution:
    def numJewelsInStones(self, J, S):
        stone_count = defaultdict(int)
        count = 0
        for stone in S:
            stone_count[stone] += 1
        for key, value in stone_count.items():
            if key in J:
                count += value
        return count
    def optimized(self, J, S):
        setJ = set(J)
        return sum(stone in setJ for stone in S)


if __name__ == "__main__":
    obj = Solution()
    print(obj.numJewelsInStones(J="aA", S="aAAbbbb"))
    print(obj.numJewelsInStones(J="z", S="ZZ"))

    print(obj.optimized(J="aA", S="aAAbbbb"))
    print(obj.optimized(J="z", S="ZZ"))