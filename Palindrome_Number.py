# https://leetcode.com/problems/palindrome-number/

"""
First of all we should take care of some edge cases. All negative numbers are not palindrome,
for example: -123 is not a palindrome since the '-' does not equal to '3'. So we can return false for all
negative numbers.

Now let's think about how to revert the last half of the number. For number 1221, if we do 1221 % 10, we get the last
digit 1, to get the second to the last digit, we need to remove the last digit from 1221, we could do so by dividing it
by 10, 1221 / 10 = 122. Then we can get the last digit again by doing a modulus by 10, 122 % 10 = 2, and if we multiply
the last digit by 10 and add the second last digit, 1 * 10 + 2 = 12, it gives us the reverted number we want.
Continuing this process would give us the reverted number with more digits.

Now the question is, how do we know that we've reached the half of the number?

Since we divided the number by 10, and multiplied the reversed number by 10, when the original number is less than
the reversed number, it means we've processed half of the number digits.
"""


class Solution:
    def isPalindrome(self, x):
        if x <0:
            return False
        newNum = 0
        num = x
        while x!=0:
            digit = x%10
            newNum = newNum*10 + digit
            x = x//10

        if newNum==num:
            return True
        else:
            return False

    def optimized(self, x):

        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        newNum = 0
        while x>newNum:
            digit = x%10
            newNum = newNum*10 + digit
            x = x//10

        if newNum == x or x == newNum//10: # first condition for even no. of digits, second condition for odd
            return True
        else:
            return False


if __name__ == "__main__":
    obj = Solution()
    print(obj.isPalindrome(x=121))
    print(obj.optimized(x=121))
    print(obj.optimized(x=10))
