# https://leetcode.com/problems/minimum-time-visiting-all-points/
# https://leetcode.com/problems/minimum-time-visiting-all-points/discuss/436250/JavaPython-3-6-liner-and-1-liner-w-brief-explanation-and-analysis.

class MinimumTime:
    def visitPoints(self, points):
        result = 0
        for p in range(1, len(points)):
            result += max(abs(points[p-1][0]-points[p][0]), abs(points[p-1][1]-points[p][1]))
        return result





if __name__ == "__main__":
    N = [[1,1],[3,4],[-1,0]] # ans 7
    obj = MinimumTime()
    print(obj.visitPoints(N))