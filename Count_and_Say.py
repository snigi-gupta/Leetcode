# https://leetcode.com/problems/count-and-say/
# https://www.youtube.com/watch?v=JQOGiecrsaQ


class Solution:
    def countAndSay(self, n):
        res = "1"

        while (n-1):
            new_string = ""
            i = 0
            while (i<len(res)):
                count = 1
                while(i+1 <len(res) and res[i] == res[i+1]):
                    i += 1
                    count += 1
                new_string += str(count) + res[i]
                i += 1
            n -= 1
            res = new_string
        return res


if __name__ == "__main__":
    obj = Solution()
    print(obj.countAndSay(n=3))
    print(obj.countAndSay(n=2))
    print(obj.countAndSay(n=1))