# https://leetcode.com/problems/backspace-string-compare/


class Solution:
    def backspaceCompareStack(self, S, T):
        def back(S):
            stack = []

            for c in S:
                if c != "#":
                    stack.append(c)
                elif stack:
                    stack.pop()
            return "".join(stack)

        return back(S) == back(T)

    def backspaceCompareTwoPointer(self, S, T):
        len_S, len_T = len(S)-1, len(T)-1
        skip_ptr_S, skip_ptr_T = 0, 0
        while True:
            while len_S >= 0 and (skip_ptr_S or S[len_S] == '#'):
                if S[len_S] == '#':
                    skip_ptr_S += 1
                else:
                    skip_ptr_S += -1
                len_S -= 1
            while len_T >= 0 and (skip_ptr_T or T[len_T] == '#'):
                if T[len_T] == '#':
                    skip_ptr_T += 1
                else:
                    skip_ptr_T += -1
                len_T -= 1
            if not (len_S >= 0 and len_T >=0 and S[len_S] == T[len_T]):
                return len_S == len_T == -1
            len_S -= 1
            len_T -= 1


if __name__ == "__main__":
    obj = Solution()
    print(obj.backspaceCompareStack("ba##c", "a#c"))
    print(obj.backspaceCompareTwoPointer("ba##c", "a#c"))






