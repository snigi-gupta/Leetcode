class Solution:
    def findDuplicates(self, arr):
        hashMap = {}
        result = []
        for val in arr:
            if val not in hashMap:
                hashMap[val] = 1
            else:
                hashMap[val] += 1

        for k, v in hashMap.items():
            if v > 1:
                result.append(k)
        return result


if __name__ == "__main__":
    obj = Solution()
    print(obj.findDuplicates(arr = [1,2,4,5,2,1,3,5,]))