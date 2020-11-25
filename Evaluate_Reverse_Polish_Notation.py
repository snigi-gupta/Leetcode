# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens):

        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                num2, num1 = stack.pop(), stack.pop()
                if token == "+":
                    result = num1 + num2
                elif token == "-":
                    result = num1 - num2
                elif token == "*":
                    result = num1 * num2
                else:
                    result = num1 / num2
                stack.append(int(result))
        return stack[-1]


if __name__ == "__main__":
    obj = Solution()
    print(obj.evalRPN(tokens=["2", "1", "+", "3", "*"]))
    print(obj.evalRPN(tokens=["4", "13", "5", "/", "+"]))
    print(obj.evalRPN(tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
