# https://leetcode.com/problems/create-target-array-in-the-given-order/
# https://leetcode.com/problems/create-target-array-in-the-given-order/discuss/553334/Python-Using-insert()-and-without-insert()
class Solution:
    def createTargetArray(self, nums, index):
        target = [-1 for _ in range(len(nums))]
        for i in range(len(nums)):
            if target[index[i]] == -1:
                target[index[i]] = nums[i]
            else:
                j = index[i]
                temp = nums[i]
                while target[j] != -1:
                    target[j], temp = temp, target[j]
                    j += 1
                target[j] = temp
        return target


if __name__ == "__main__":
    obj = Solution()
    print(obj.createTargetArray(nums=[0,1,2,3,4], index=[0,1,2,2,1]))
