# https://leetcode.com/problems/reorder-data-in-log-files/

class Solution:
    def reorderLogFiles(self, logs):

        def custom_sort(logs):
            identifier, log = logs.split(" ", maxsplit=1)
            if log[0].isalpha():
                return (0, log, identifier)
            else:
                return (1, )
        return sorted(logs, key=custom_sort)


if __name__ == "__main__":
    obj = Solution()
    print(obj.reorderLogFiles(logs=["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))