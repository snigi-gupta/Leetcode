import collections
class Solution:
    def check_anagram(self, s1, s2):

        if len(s1) != len(s2):
            return False

        s1_chars = collections.Counter(s1)
        s2_chars = collections.Counter(s2)
        print(s1_chars)
        print(s2_chars)
        for key in s1_chars.keys():
            if s1_chars[key] != s2_chars[key]:
                return False

        return True






if __name__ == "__main__":
    s1 = "dark2"
    s2 = "kard3"
    obj = Solution()
    print(obj.check_anagram(s1, s2))

