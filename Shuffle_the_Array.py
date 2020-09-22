# https://leetcode.com/problems/shuffle-the-array/
class Solution:
    def shuffle(self, nums, n):
        i = 0
        j = len(nums)//2

        result = []
        while j < n*2:
            result.append(nums[i])
            result.append(nums[j])
            i += 1
            j += 1
        return result




if __name__ == "__main__":
    obj = Solution()
    print(obj.shuffle(nums=[2,5,1,3,4,7], n=3))
    print(obj.shuffle(nums=[1,2,3,4,4,3,2,1], n=4))