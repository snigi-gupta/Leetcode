# https://leetcode.com/problems/maximum-product-subarray/
# https://www.youtube.com/watch?v=hJ_Uy2DzE08

class Solution:
    def maxProduct(self, nums):
        max_prod = nums[0]
        max_choice = nums[0]
        min_choice = nums[0]

        for i in range(1, len(nums)):
            temp = max_choice
            max_choice = max(nums[i], nums[i]*temp, nums[i]*min_choice)
            min_choice = min(nums[i], nums[i]*temp, nums[i]*min_choice)

            max_prod = max(max_choice, max_prod)

        return max_prod


if __name__ == "__main__":
    obj = Solution()
    print(obj.maxProduct(nums=[-2,3,-4]))
