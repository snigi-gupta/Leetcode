# https://leetcode.com/problems/decompress-run-length-encoded-list/

class Decompress:
    def encoded(self, nums):
        result = []
        for i in range(1, len(nums),2):
            result.extend([nums[i]] * nums[i-1])
        return result


if __name__ == "__main__":
    N = [1,2,3,4] # ans [2,4,4,4]
    obj = Decompress()
    print(obj.encoded(N))
