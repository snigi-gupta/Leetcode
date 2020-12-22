# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

import sys


class Solution:
    def maxProfit(self, prices):
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit


if __name__ == "__main__":
    input = [7,1,5,3,6,4]   #ans 7
    obj = Solution()
    print(obj.maxProfit(input))