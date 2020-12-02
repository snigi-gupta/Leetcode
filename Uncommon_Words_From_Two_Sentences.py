# https://leetcode.com/problems/uncommon-words-from-two-sentences/

from collections import defaultdict


class Solution:
    def uncommonFromSentences(self, A, B):

        words = A.split()
        words.extend(B.split())

        hash_map = defaultdict(int)
        result = []
        for word in words:
            hash_map[word] += 1

        for key, value in hash_map.items():
            if value == 1:
                result.append(key)

        return result


if __name__ == "__main__":
    obj = Solution()
    print(obj.uncommonFromSentences(A="this apple is sweet", B="this apple is sour"))