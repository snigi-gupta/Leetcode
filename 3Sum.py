# https://leetcode.com/problems/3sum/
# https://leetcode.com/problems/3sum/solution/
# Refer below link for "No-Sort" technique
# https://www.youtube.com/watch?v=yZLMCSxJ-yA


class Solution:
    def twoPointer(self, nums):

        sorted_nums = sorted(nums)
        result = []
        for i, val1 in enumerate(sorted_nums):
            if val1 >0:
                return result
            if val1 != sorted_nums[i-1] or i == 0:
                lo = i + 1
                hi = len(sorted_nums) - 1
                while lo<hi:
                    theSum = sorted_nums[lo]+sorted_nums[hi]
                    if (theSum + val1) == 0:
                        result.append([val1, sorted_nums[lo], sorted_nums[hi]])
                        lo += 1
                        hi -= 1
                        while lo<hi and sorted_nums[lo] == sorted_nums[lo-1]:
                            lo += 1
                    elif theSum < -val1:
                        lo += 1
                    elif theSum > -val1:
                        hi -= 1
        return result

    """
    a+b+c = 0
    a = -b-c
    """
    def hashSet(self, nums):
        sorted_nums = sorted(nums)
        result = []

        for i, val1 in enumerate(sorted_nums):
            if val1 > 0:
                return result
            if val1 != sorted_nums[i-1] or i == 0:
                seen = set()
                j = i + 1
                while j < len(sorted_nums):
                    val2 = sorted_nums[j]
                    val3 = -val1-val2
                    if val3 in seen:
                        result.append([val1, val2, val3])
                        while j+1<len(sorted_nums) and sorted_nums[j] == sorted_nums[j+1]:
                            j += 1
                    seen.add(val2)
                    j += 1

        return result


if __name__ == "__main__":
    obj = Solution()
    # print(obj.twoPointer(nums=[-1,0,1,2,-1,-4]))
    # print(obj.twoPointer(nums=[]))
    # print(obj.twoPointer(nums=[0]))
    # print(obj.twoPointer(nums=[-8,-1,0,2,4,6]))
    # print(obj.twoPointer(nums=[-2,0,0,2,2]))
    print(obj.hashSet(nums=[-2,0,0,2,2]))
