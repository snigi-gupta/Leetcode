# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        left, right = 2, x//2

        while left <= right:
            mid = left + (right-left)//2
            num = mid * mid
            if num > x:
                right = mid - 1
            else:
                left = mid + 1

        return right


if __name__ == "__main__":
    obj = Solution()
    print(obj.mySqrt(x=8))