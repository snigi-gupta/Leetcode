# https://leetcode.com/problems/shortest-word-distance/
import collections


class Solution:
    def shortestDistance(self, words, word1, word2):
        hash_map = collections.defaultdict(list)

        for index, word in enumerate(words):
            hash_map[word].append(index)

        distance_1 = hash_map.get(word1)
        distance_2 = hash_map.get(word2)

        return abs(distance_2 - distance_1)


if __name__ == "__main__":
    obj = Solution()
    print(obj.shortestDistance(words=["practice", "makes", "perfect", "coding", "makes"], word1="coding",
                               word2="practice"))
    print(obj.shortestDistance(words=["a", "a", "b", "b"], word1="a", word2="b"))
