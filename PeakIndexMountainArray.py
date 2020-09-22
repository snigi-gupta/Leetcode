# https://leetcode.com/problems/peak-index-in-a-mountain-array/
class Solution:
    def peakIndexInMountainArray(self, A):
        lo, hi = 0, len(A)-1

        while lo<hi:
            mid = hi+lo // 2
            if A[mid] < A[mid+1]:
                lo = mid+1
            else:
                hi = mid
        return lo

if __name__ == "__main__":
    obj = Solution()
    print(obj.peakIndexInMountainArray(A=[3, 4, 1, 1]))