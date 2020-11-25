# https://leetcode.com/problems/fibonacci-number/
# https://github.com/samgh/DynamicProgrammingEbook/blob/master/python/Fibonacci.py


class Solution:

    """
    This is a recursive approach
    """
    def fib(self, N):
        if N == 0:
            return 0
        if N == 1:
            return 1
        result = self.fib(N-1)+self.fib(N-2)

        return result

    """
    This is a top down approch that uses Dynamic Programming
    """
    def fibTopDown(self, N):
        print(f"We are inside 'fibTopDown({N})' function")
        if N < 2: return N
        cache = [-1 for _ in range(N+1)]
        print(f"cache is {cache}")
        cache[0], cache[1] = 0, 1
        print(f"cache now is {cache}")
        print(f"Now calling '_fibTopDown({N})' function with cache {cache}")
        return self._fibTopDown(N, cache)

    def _fibTopDown(self, N, cache):
        print(f"cache[{N}] is {cache[N]})")
        if cache[N] >= 0: return cache[N]
        print(f"Calling recursively 'fibTopDown({N-1}) and 'fibTopDown({N-2})' functions")
        cache[N] = self._fibTopDown(N-1, cache) + self._fibTopDown(N-2, cache)
        print(f"cache after recursion call is {cache}")
        return cache[N]

    """
    This is a bottom up approach using Dynamic Programming
    """
    def fibBottomUp(self, N):
        if N == 0: return 0
        cache = [0 for _ in range(N+1)]
        cache[1] = 1
        for i in range(2, N+1):
            cache[i] = cache[i-1] + cache[i-2]
        return cache[N]


if __name__ == "__main__":
    obj = Solution()
    print(obj.fib(N=10))
    print(obj.fibTopDown(N=4))
    print(obj.fibBottomUp(N=10))