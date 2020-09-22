# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
# https://www.youtube.com/watch?v=Z49SHHLzq4w

from collections import Counter

class OddMatrix:
    """
    TC: O(L+n*m)
    SC: O(n*m)
    """
    def findOddValues(self, n, m, indices):
        M = [[0 for _ in range(m)] for _ in range(n)]
        # M_ = [[0] * m ] * n
        # https://stackoverflow.com/questions/55320040/difference-between-2-ways-of-list-comprehensions-in-python

        for r,c in indices:
            for j in range(m):
                M[r][j] += 1
            for i in range(n):
                M[i][c] += 1
        return sum(M[i][j] % 2 for i in range(n) for j in range(m))

    """
    TC: O(L+n*m)
    SC: O(n*m)
    """
    def findOddValues2(self, n, m, indices):
        M = [[0 for _ in range(m)] for _ in range(n)]

        """
        XOR True -> Odd
            False -> Even
        """
        # M_ = [[0] * m ] * n
        # https://stackoverflow.com/questions/55320040/difference-between-2-ways-of-list-comprehensions-in-python

        for r,c in indices:
            for j in range(m):
                M[r][j] ^= 1
            for i in range(n):
                M[i][c] ^= 1
        return sum(M[i][j] for i in range(n) for j in range(m))

    """
    TC: O(L+n*m)
    SC: O(L)
    """
    def findOddValues3(self, n, m, indices):
        row, col = Counter(r for r,_ in indices), Counter(c for _, c in indices)
        return sum(row[i]+col[j] % 2 for i in range(n) for j in range(m))

    """
    TC: O(L+n*m)
    SC: O(L)
    """


if __name__ == "__main__":
    indices = [[0,1],[1,1]] # ans 6
    n=2
    m=3
    obj = OddMatrix()
    print("findOddValues", obj.findOddValues(n, m, indices))
    print("findOddValues2", obj.findOddValues2(n, m, indices))
    print("findOddValues3", obj.findOddValues3(n, m, indices))