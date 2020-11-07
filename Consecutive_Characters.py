# https://leetcode.com/problems/consecutive-characters/

class Solution:
    def maxPower(self, s):

        count, max_count = 1,1
        previous = s[0]
        for i in range(1, len(s)):
            if s[i]==previous:
                count += 1
                max_count = max(max_count, count)
            else:
                previous = s[i]
                count = 1
        return max_count


if __name__ == "__main__":
    obj = Solution()
    print(obj.maxPower(s="leetcode"))

