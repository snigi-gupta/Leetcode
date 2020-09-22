# https://leetcode.com/problems/array-partition-i/
class ArrayPartition:
    def arrayPairSum(self, nums) -> int:
        sorted_nums = sorted(nums)
        result = 0
        for v in range(0, len(sorted_nums), 2):
            result += sorted_nums[v]
        return result

if __name__ == "__main__":
    input = [1, 4, 3, 2] #ans 4
    obj = ArrayPartition()
    print(obj.arrayPairSum(input))
