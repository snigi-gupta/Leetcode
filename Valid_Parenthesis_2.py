class Solution:
    def isValid(self, s):
        brackets = s
        stack = []
        flag = True
        hashMap = {")": "(",
                   "]": "[",
                   "}": "{", }
        i = 0
        while i < len(brackets) and flag:
            if brackets[i] in "([{":
                stack.extend(brackets[i])
            else:
                if len(stack) == 0:
                    flag = False
                else:
                    current = stack.pop()
                    if current != hashMap[brackets[i]]:
                        flag = False
            i += 1

        if stack == [] and flag:
            return True
        else:
            return False


if __name__ == "__main__":
    obj = Solution()
    print(obj.isValid(s="()"))
    print(obj.isValid(s=")"))
