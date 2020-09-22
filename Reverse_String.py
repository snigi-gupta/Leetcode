# https://www.educative.io/courses/ds-and-algorithms-in-python/gkgwQvGVBY3
class Solution:
    def reverse(self, string):
        result = ""
        stack = [s for s in string]
        while stack != []:
            result += stack.pop()
        return result


if __name__ == "__main__":
    obj = Solution()
    print(obj.reverse(string="Hello"))