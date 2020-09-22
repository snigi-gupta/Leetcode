# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/solution/
class Solution:
    def numberOfSteps(self, num):
        count = 0
        while num != 0:

            if num%2 == 0:
                num //= 2
            else:
                num -= 1
            count += 1
        return count

    def optimized(self, num):
        bin_num = bin(num)[2:]
        ones = bin_num.count("1")
        total = len(bin_num)
        return ones+total-1



if __name__ == "__main__":
    obj = Solution()
    print(obj.numberOfSteps(num=14))
    print(obj.optimized(num=14))
