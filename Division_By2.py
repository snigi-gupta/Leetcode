class Solution:
    def divisionBy2(self, num):
        stack = []
        while num != 0:
            rem = num%2
            num = num//2
            print(rem, num)
            stack.append(str(rem))

        return ''.join(stack)[::-1]


if __name__ == "__main__":
    obj = Solution()
    print(obj.divisionBy2(num=242))