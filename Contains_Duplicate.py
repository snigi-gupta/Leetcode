# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums):
        counter = {}
        for n in nums:
            if n not in counter:
                counter[n] = 1
            else:
                counter[n] += 1


        for k, v in counter.items():
            print(k,v)
            if v>=2:
                return True

        return False


if __name__ == "__main__":
    obj = Solution()
    print(obj.containsDuplicate(nums=[1, 2, 3, 1]))
    print(obj.containsDuplicate(nums=[3, 1]))
