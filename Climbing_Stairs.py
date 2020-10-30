# https://leetcode.com/problems/climbing-stairs/

"""
This solution works but raises TLE at n=38.
To solve TLE, we can use DP approach
"""
class Solution:
    def climbStairs(self, n):
        total_ways = 0
        if n == 0 or n == 1 or n == 2:
            return n
        total_ways += self.climbStairs(n-1) + self.climbStairs(n-2)

        return total_ways

    def betterApproach(self, n):
        if n == 1:
            return 1
        dp = [1, 2]
        for i in range(2, n):
            dp.append(dp[i-1]+dp[i-2])
        return dp[n-1]


if __name__ == "__main__":
    obj = Solution()
    # print(obj.climbStairs(n=4))
    # print(obj.climbStairs(n=38))
    print(obj.betterApproach(n=38))