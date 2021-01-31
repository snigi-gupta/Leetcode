# https://leetcode.com/problems/longest-substring-without-repeating-characters/

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s):

        if not s:
            return 0

        counter = 0
        start, end = 0, 0
        max_len = float('-inf')

        hash_map = defaultdict(int)

        while end < len(s):
            end_char = s[end]
            if hash_map[end_char] > 0:
                counter += 1
            hash_map[end_char] += 1
            end += 1

            while counter > 0:
                start_char = s[start]

                if hash_map[start_char] > 1:
                    counter -= 1
                hash_map[start_char] -= 1
                start += 1
            max_len = max(max_len, end-start)
        return max_len


if __name__ == "__main__":
    obj = Solution()

    print(obj.lengthOfLongestSubstring(s="abbajkhipndaabcd"))