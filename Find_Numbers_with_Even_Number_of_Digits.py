# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class EvenDigits:
    def findNumbers(self, nums):
        result = 0
        for val in nums:
            if len(str(val)) % 2 == 0:
                result += 1
        return result

    # another approach [CLEVER]
    # https://leetcode.com/problems/find-numbers-with-even-number-of-digits/discuss/459489/JAVA-solution-with-100-better-space-and-Time

    def findNumbers(self, nums):
        result = 0
        for val in nums:
            if (val>=10 and val<100) or (val>=1000 and val<10000) or (val == 100000):
                result += 1
        return result

if __name__ == "__main__":
    N = [12,345,2,6,7896] # ans 2
    obj = EvenDigits()
    print(obj.findNumbers(N))
    print("Clever approach", obj.findNumbers(N))
