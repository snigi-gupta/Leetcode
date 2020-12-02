# https://leetcode.com/problems/brick-wall/

"""
The idea is to look at the wall and find the positions of the creases.
The you find the max count of the creases
Then you subtract the max creases from the number of brick rows to print the number of brick that will get cut.
"""
from collections import defaultdict

class Solution:
    def leastBrick(self, wall):
        hashMap = defaultdict(int)

        max_count = 0
        for row in wall:
            brick_width = 0
            for idx in range(0,len(row)-1):
                brick_width += row[idx]
                hashMap[brick_width] += 1
                max_count = max(max_count, hashMap[brick_width])
        print(hashMap)

        return len(wall)-max_count


if __name__ == "__main__":
    obj = Solution()
    print(obj.leastBrick(wall= [[1,2,2,1],
                                [3,1,2],
                                [1,3,2],
                                [2,4],
                                [3,1,2],
                                [1,3,1,1]]))

