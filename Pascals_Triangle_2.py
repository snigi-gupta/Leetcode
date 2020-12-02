# https://leetcode.com/problems/pascals-triangle/

class Solution:

    def helper(self, itr, pascal_row):

        new_pascal_row = [1]
        ptr0 = 0
        ptr1 = 1

        while itr > 1:
            sum_ = pascal_row[ptr0] + pascal_row[ptr1]
            new_pascal_row.append(sum_)
            ptr0 += 1
            ptr1 += 1
            itr -= 1

        new_pascal_row.append(1)
        return new_pascal_row

    def generate(self,rowIndex):
        itr = 1
        result = [[1]]
        while itr <= rowIndex:
            result.append(self.helper(itr, result[itr-1]))
            itr += 1
        return result[rowIndex]


if __name__ == "__main__":
    obj = Solution()
    print(obj.generate(rowIndex=5))
