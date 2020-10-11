# https://leetcode.com/problems/maximum-subarray/
# see your notes

class Solution:
    def maxSubArray(self, nums):
        # 1 Divide
        # 2 Conquer
        # 3 Combine

        def helper(arr):
            if len(arr) == 1:
                return arr[0], arr[0], arr[0], arr[0]
            # ans , left, right, array

            left = helper(arr[:len(arr) // 2])
            right = helper(arr[len(arr) // 2:])

            ans = max(left[0], right[0], left[2] + right[1])
            # -2,1,-1 ans = 1

            return ans, max(left[1], left[3] + right[1]), max(right[2], right[3] + left[2]), left[3] + right[3]

        result = helper(nums)
        return result[0]

    def usingDP(self, nums):

        max_sum  = nums[0]
        best_choice = nums[0]

        for i in range(1, len((nums))):

            best_choice = max(best_choice+nums[i], nums[i])

            max_sum = max(max_sum, best_choice)

            """
            The below is an implementation without using max. Just to understand.            
            """
            # if best_choice+nums[i] > nums[i]:
            #     best_choice = best_choice+nums[i]
            # else:
            #     best_choice = nums[i]

            # if max_sum < best_choice:
            #     max_sum = best_choice

        return max_sum



if __name__ == "__main__":
    obj = Solution()
    print(obj.maxSubArray(nums=[-2,1,-3,4,-1,2,1,-5,4]))
    print(obj.usingDP(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))