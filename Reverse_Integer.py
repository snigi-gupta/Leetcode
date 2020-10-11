# https://leetcode.com/problems/reverse-integer/
# https://www.youtube.com/watch?v=Io9ujnnR4sI&t=1272s

class Solution:
    def reverse(self, x):
        s = (x > 0) - (x < 0)
        r = int(str(x*s)[::-1])
        print(s*r * (r < 2**31))


    """
    1. In python -123/10 will give 12.3
       Using -123//10 will give 13
       But we need -12, so for that we will use def divide()
       
       
    2. In python -123%10 will give 7
       Thus we need to ensure that when a -ve number we take a mod with a -ve number.
       So, -123%-10 will give us -3, which is what we want.
       Thus we created def mod() which will return the mod accordingly. 
       
    """
    def divide(self, num, divisor):
        return int(num*1.0 / divisor)

    def mod(self, num, m):
        if num<0:
            return num % -m
        else:
            return num % m

    def reverse2(self, x):
        MAX_INT = 2**31 -1 # this is a large number which is a constraint int the question. This number ends with 7
        MIN_INT = -2**31 # this is a large number which is a constraint int the question. This number ends with -8
        res = 0

        while x:
            pop = self.mod(x, 10)
            x = self.divide(x, 10)

            if res > self.divide(MAX_INT, 10) or (res == self.divide(MAX_INT, 10) and pop > 7):
                return 0
            if res < self.divide(MIN_INT, 10) or (res == self.divide(MIN_INT, 10) and pop < -8):
                return 0

            res = res*10 + pop

        return res

if __name__ == "__main__":
    obj = Solution()
    obj.reverse(x=123) # ans 321
    print(obj.reverse2(x=- 123)) # ans -321
    print(obj.reverse2(x=-1463847412))
