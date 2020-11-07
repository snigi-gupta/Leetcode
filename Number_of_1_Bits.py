# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            if n & 1:
                result += 1
            n >>= 1

        return result


if __name__ == "__main__":
    obj = Solution()
    print(obj.hammingWeight(n=0o0000000000000000000000000001011))