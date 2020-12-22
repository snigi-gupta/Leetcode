# https://leetcode.com/problems/valid-palindrome/


class Solution:

    def isPalindrome(self, s):
        string = []
        if s == "":
            return True

        for val in s:
            if val.isalnum():
                string.append(val.lower())

        left_ptr, right_ptr = 0, len(string) - 1

        while left_ptr < right_ptr:
            # print(string[left_ptr], string[right_ptr])
            if string[left_ptr] != string[right_ptr]:
                return False
            left_ptr += 1
            right_ptr -= 1

        return True


if __name__ == "__main__":
    obj = Solution()
    print(obj.isPalindrome("A man, a plan, a canal: Panama"))