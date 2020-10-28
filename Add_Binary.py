# https://leetcode.com/problems/add-binary/

"""
0+0 = 0 carry 0
0+1 = 1 carry 0
1+1 = 1 carry 1
1+1+1 = 1 carry 1

thesum can be 0,1,,2,3
thesum%2 = 0,1,1,1 (this result can be appended to result)
thesum/2 = 0,0,1,1
"""
class Solution:
    def addBinary(self, a, b):
        thesum = 0
        carry = 0
        result = []
        len_a, len_b = len(a)-1, len(b)-1
        while len_a >= 0 or len_b >= 0:
            thesum = carry
            if len_a >=0:
                thesum += int(a[len_a])
            if len_b >= 0:
                thesum += int(b[len_b])
            quotient, rem = divmod(thesum,2)
            result.append(str(rem))
            carry = quotient
            len_a -= 1
            len_b -= 1
        if carry:
            result = result + [str(carry)]

        return ''.join(result[::-1])


if __name__ == "__main__":
    obj = Solution()
    print(obj.addBinary(a="11", b="1"))