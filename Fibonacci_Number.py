# https://leetcode.com/problems/fibonacci-number/


class Solution:
    def fib(self, N):
        if N == 0:
            return 0
        if N == 1:
            return 1
        result = self.fib(N-1)+self.fib(N-2)

        return result


if __name__ == "__main__":
    obj = Solution()
    print(obj.fib(N=4))