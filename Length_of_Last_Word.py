# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s):
        words = s.split()
        if not words:
            return 0
        return len(words[-1])


if __name__ == "__main__":
    obj = Solution()
    print(obj.lengthOfLastWord(s="Hello World"))
    print(obj.lengthOfLastWord(s=""))
    print(obj.lengthOfLastWord(s=" "))
    print(obj.lengthOfLastWord(s="    "))