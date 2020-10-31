# https://leetcode.com/problems/merge-sorted-array/


class Solution:
    def merge(self, nums1, m, nums2, n):
        p1, p2 = m-1, n-1
        p = m+n-1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] =nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                nums1[p1] = nums2[p2]
                p1 -= 1
            p -= 1
        if p2 >= 0:
            nums1[:p2+1] = nums2[:p2+1]
        return nums1


if __name__ == "__main__":
    obj = Solution()
    print(obj.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))
    print(obj.merge(nums1=[4, 5, 6, 0, 0, 0], m=3, nums2=[1, 2, 3], n=3))
    print(obj.merge(nums1=[0], m=0, nums2=[1], n=1))
