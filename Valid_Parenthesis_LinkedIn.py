"""
This function determines if the braces ('(' and ')') in a string are properly matched. It ignores non-brace characters.
* Some examples:
1- input: "()()()()" ; output: true
2- input: " ( (45+) *a3)" ; output: true
3- input: "(( (()) ())" ; output: false
4- input: ") )((" ; output: false
"""
class Solution():

    def matched(self, input_string):
        if not input_string:
            return False

        counter = 0

        for ch in input_string:
            if counter < 0:
                return False
            if ch == "(":
                counter += 1
            elif ch == ")":
                counter -= 1

        return counter == 0


if __name__ == "__main__":
    obj = Solution()
    print(obj.matched(input_string=" ( (45+) *a3)"))
