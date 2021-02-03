# https://leetcode.com/problems/longest-palindromic-substring/
# https://www.youtube.com/watch?v=y2BD4MJqV20


class Solution:
    def longestPalindrome(self, s):

        if s is "" or len(s) < 1:
            return ""

        start = 0
        end = 0

        for i in range(len(s)):
            len1 = self.expand(s, i, i)
            len2 = self.expand(s, i, i + 1)

            max_len = max(len1, len2)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end+1]

    def expand(self, s, left, right):

        if s is "" or left > right:
            return 0

        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left - 1


if __name__ == "__main__":
    obj = Solution()
    # print(obj.longestPalindrome(s="babad"))
    print(obj.longestPalindrome(s="bracecaraa"))