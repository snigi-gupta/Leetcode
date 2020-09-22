# https://leetcode.com/problems/running-sum-of-1d-array/
class Solution:
    def runningSum(self, nums):
        running_sum = [nums[0]]
        for i in range(1, len(nums)):
            temp = running_sum[i-1] + nums[i]
            running_sum.append(temp)
        return running_sum
    def bruteForce(self,nums):
        running_sum = []
        for i in range(len(nums)):
            temp = sum(nums[0:i+1])
            running_sum.append(temp)
        return running_sum

if __name__ == "__main__":
    obj = Solution()
    print(obj.runningSum(nums=[3, 1, 2, 10, 1]))
    print(obj.bruteForce(nums=[3, 1, 2, 10, 1]))