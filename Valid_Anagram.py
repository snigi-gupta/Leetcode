# https://leetcode.com/problems/valid-anagram/

from collections import defaultdict

class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t): return False

        hashMap = defaultdict(int)
        for ch in s:
            hashMap[ch] += 1
        print(hashMap)
        for ch in t:
            hashMap[ch] -= 1
        print(hashMap)
        for k, v in hashMap.items():
            if v < 0:
                return False
        return True


if __name__ == "__main__":
    obj = Solution()
    print(obj.isAnagram("anaggap", "anagtga"))