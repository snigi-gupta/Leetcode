# https://leetcode.com/problems/plus-one/


class Solution:
    def plusOne(self, digits):
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                carry = 1
            else:
                digits[i] += 1
                return digits
        if carry:
            return [carry] + digits


if __name__ == "__main__":
    obj = Solution()
    print(obj.plusOne(digits=[1, 2, 9]))
    print(obj.plusOne(digits=[9, 9, 9]))
    print(obj.plusOne(digits=[1, 8, 8]))
    print(obj.plusOne(digits=[0]))
