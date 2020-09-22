# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

"""
It will be O(logN), since the loop will run the number of times equal to number of digits.
"""
class Solution:
    def subtractProductAndSum(self, n):
        thesum = 0
        theprod = 1
        while n > 0:
            digit = n%10
            thesum += digit
            theprod *= digit
            n = n//10
        return theprod-thesum

if __name__ == "__main__":
    obj = Solution()
    print(obj.subtractProductAndSum(n=234))