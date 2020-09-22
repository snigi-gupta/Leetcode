# https://www.educative.io/courses/ds-and-algorithms-in-python/g7Zp75M7LNk
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, ele):
        self.stack.append(ele)
        return "Done"

    def pop(self):
        if self.stack:
            return self.stack.pop()

    def peek(self):
        if self.stack is not None:
            return self.stack[-1]

    def get_stack(self):
        return self.stack

class Solution:
    def validate(self, brackets):
        isMatch = {")": "(", "]": "[", "}": "{"}
        obj = Stack()
        flag = True
        idx = 0
        while idx < len(brackets) and flag:
            if brackets[idx] in "([{":
                obj.push(brackets[idx])
            else:
                if obj.stack is None:
                    flag = False
                else:
                    top = obj.pop()
                    if top != isMatch[brackets[idx]]:
                        flag = False
            idx += 1
        if obj.stack == [] and flag:
            return  True
        else:
            return False


if __name__ == "__main__":
    newObj = Solution()
    print(newObj.validate(brackets="[{}"))
