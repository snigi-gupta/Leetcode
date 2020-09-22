# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        result = [False for _ in range(len(candies))]
        greatest = max(candies)
        for i, candy in enumerate(candies):
            if candy + extraCandies >= greatest:
                result[i] = True
        return result





if __name__ == "__main__":
    obj = Solution()
    print(obj.kidsWithCandies(candies=[4,2,1,1,2], extraCandies=1))
    print(obj.kidsWithCandies(candies=[2,3,5,1,3], extraCandies=3))
    print(obj.kidsWithCandies(candies=[12,1,12], extraCandies=10))
    print(obj.kidsWithCandies(candies=[2, 8, 7], extraCandies=1))