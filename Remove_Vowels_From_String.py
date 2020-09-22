# https://leetcode.com/problems/remove-vowels-from-a-string/
# https://leetcode.com/problems/remove-vowels-from-a-string/discuss/493206/Python3-with-Set-vs-List-performance-with-inline-comments

class Vowels:
    def remove(self, s):
        # result = []
        """
        Instead of list use string, since that is what is to be returned
        """
        result = ""
        # vowels = ['a', 'e', 'i', 'o', 'u']
        """
        Instead of list, use a set. Since vowels are unique.
        """
        vowels = ('a', 'e', 'i', 'o', 'u')
        for c in s:
            if c not in vowels:
                # result.append(c)
                result += c
        # return "".join(result)
        return result


if __name__ == "__main__":
    my_string = "snigdha" # ans sngdh
    obj = Vowels()
    print(obj.remove(my_string))
