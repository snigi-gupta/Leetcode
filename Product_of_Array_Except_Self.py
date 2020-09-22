# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums):
        leftArr = []
        rightArr = [0 for _ in nums]
        result = []

        for i, n in enumerate(nums):
            if i == 0:
                leftArr.append(1)
            else:
                leftArr.append(nums[i-1] * leftArr[i-1])
        i = len(nums)-1
        while i >= 0:
            if i == len(nums)-1:
                rightArr[i] = 1
            else:
                rightArr[i] = nums[i+1] * rightArr[i+1]
            i -= 1

        # print(leftArr)
        # print(rightArr)

        for i in range(len(nums)):
            result.append(leftArr[i]*rightArr[i])
        return result

    def saveSpace(self, nums):
        result = [0 for _ in nums]
        result[0] = 1
        for i, n in enumerate(nums):
            if i == 0:
                continue
            else:
                result[i] = result[i-1] * nums[i-1]
        R = 1
        i = len(nums)-1
        while i >= 0:
            result[i] = result[i] * R
            R *= nums[i]
            i -= 1
        return  result

if __name__ == "__main__":
    obj = Solution()
    print(obj.productExceptSelf(nums=[2,3,1,4]))
    print(obj.saveSpace(nums=[2, 3, 1, 4]))