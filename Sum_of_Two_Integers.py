# https://leetcode.com/problems/sum-of-two-integers/
# https://www.youtube.com/watch?v=qq64FrA2UXQ&feature=emb_title

"""
^ (XOR) is for simulating addition
& (AND) calculates the carry
<< (LEFT SHIFT) shifts the carry to the left (since we use the carry for the next left bit, we use <<.)

"""
class Solution:
    def getSum(self, a, b):
        x, y = abs(a), abs(b)

        if x < y:
            return self.getSum(b, a)

        sign = 1 if a >= 0 else -1

        if a * b >= 0:
            while y:
                answer = x ^ y
                carry = (x & y) << 1
                x, y = answer, carry
        else:
            while y:
                answer = x ^ y
                borrow = ((~x) & y) << 1
                x, y = answer, borrow

        return x * sign


if __name__ == "__main__":
    obj = Solution()
    # print(obj.getSum(a=1, b=2))
    print(obj.getSum(a=-3, b=-4))