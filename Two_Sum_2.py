# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


class Solution:

    """
    This solution works for Two_Sun technique because the array is not sorted. So we can solve the question in O(n)
    time using a hash-map.
    """
    def twoSum(self, numbers, target):
        hashMap= {}


        for i, num in enumerate(numbers):
            complement = target - num
            if num in hashMap:
                return [hashMap[num], i+1]
            else:
                hashMap[complement] = i+1

    """
    However, if we have a sorted array we can use the two-pointer technique.
    we add the smallest and the largest element. if we get the sum, we return it.
    if we get a sum lower than target then we increase left ptr. if we get a sum higher than target, then we decrease 
    right ptr.
    """
    def twoSum2(self, numbers, target):
        left, right = 0, len(numbers)-1
        while left<right:
            _sum = numbers[left] + numbers[right]
            if _sum == target:
                return [left+1,right+1]
            elif _sum < target:
                left += 1
            else:
                right -= 1


if __name__ == "__main__":
    obj = Solution()
    print(obj.twoSum(numbers=[2,7,11,15], target=9))
    print(obj.twoSum(numbers=[2,3,4], target=6))
    print(obj.twoSum(numbers=[-1,0], target=-1))
    print("Two-Pointer")
    print(obj.twoSum2(numbers=[2,7,11,15], target=9))
    print(obj.twoSum2(numbers=[2,3,4], target=6))
    print(obj.twoSum2(numbers=[-1,0], target=-1))