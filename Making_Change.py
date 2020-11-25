"""
25,10, 5, 1 coins

50 -25
25 -25
0
2 coins
57
57 - 25
32 - 25
7 - 5
2 - 1
1- 1
5 coins

"""

import sys


class Solution:
    """
    This is a greedy approach
    """

    def makeChange(self, money):
        count = 0
        coins = [25, 10, 5, 1]

        for coin in coins:
            while money - coin >= 0:
                money = money - coin
                count += 1
        return count

    def topDown(self, money):
        self.cache = [-1 for _ in range(money + 1)]
        return self._topDown(money)

    def _topDown(self, money):
        if money == 0:
            return 0
        elif self.cache[money] >= 0:
            return self.cache[money]
        coins = [25, 10, 5, 1]
        minCoins = sys.maxsize

        for coin in coins:
            if money - coin >= 0:
                minCoins = min(minCoins, self._topDown(money - coin))

        self.cache[money] = minCoins + 1
        return self.cache[money]

    def botttomUp(self, money):
        coins = [25,10, 5, 1]
        cache = [-1 for _ in range(money+1)]
        cache[0] = 0
        for itr in range(1,money+1):
            minCoins = sys.maxsize
            for coin in coins:

                if itr-coin >= 0:
                    curr_cache = cache[itr-coin] + 1
                    minCoins = min(curr_cache, minCoins)

            cache[itr] = minCoins

        return cache[money]


if __name__ == "__main__":
    obj = Solution()
    print(obj.makeChange(money=57))
    print(obj.topDown(money=100))
    print(obj.botttomUp(money=10))
