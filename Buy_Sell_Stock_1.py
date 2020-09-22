# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
import sys


class BuySellStock:
    def maxProfit(self, prices) -> int:

        min_price = sys.maxsize
        max_profit = 0
        for i in range(0, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit

    def otherMethod(self, prices):
        min_costprice = sys.maxsize
        max_profit = 0

        for i, p in enumerate(prices):
            if p < min_costprice:
                min_costprice = p
            else:
                max_profit = max(max_profit, p - min_costprice)
        return max_profit

if __name__ == "__main__":
    input = [7,1,5,3,6,4]   #ans 5
    # input = [7,6,4,3,1]   #ans 0
    # input = [7,2,4,1]     #ans 2
    obj = BuySellStock()
    print(obj.maxProfit(input))