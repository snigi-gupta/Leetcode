# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution:
    def reverseParentheses(self, s):
        stack = []
        itr = 0
        while itr<len(s):
            if s[itr] != ')':
                stack.append(s[itr])
            else:
                temp_string = ""
                while stack[-1] != "(":
                    temp_string += stack.pop()
                stack = stack[:len(stack)-1] + list(temp_string)
            itr += 1
        return ''.join(stack)


if __name__ == "__main__":
    obj = Solution()
    print(obj.reverseParentheses(s="(u(love)i)"))
    print(obj.reverseParentheses(s="(ed(et(oc))el)"))
    print(obj.reverseParentheses(s="a(bcdefghijkl(mno)p)q"))