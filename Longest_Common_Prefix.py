# https://leetcode.com/problems/longest-common-prefix/


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()

            current = current.children[ch]
        current.isEnd = True

    """
    If you have to search a prefix, this function can be used.
    It will only return if the given prefix is present or not.
    However, the question demands for the longest prefix.
    """
    # def searhPrefix(self, prefix):
    #     current = self.root
    #
    #     for ch in prefix:
    #         if ch not in current.children:
    #             return False
    #         current = current.children[ch]
    #     return True

    """
    Intuition: We want to see if the current node has only 1 child and that isEnd is False.
    When isEnd of next current node is True, it means that a word is already completed and the first isEnd True is
    the shortest word. Therefore, we cannot have a prefix larger than the shortest word in the trie.
    """
    def getLongestPrefix(self, words):
        longestPrefix = ""
        current = self.root

        while len(current.children) == 1 and not current.isEnd:
            # print(current.children.keys(), current.isEnd)
            ch = list(current.children.keys())[0]
            longestPrefix += ch
            current = current.children[ch]
        return longestPrefix


class Solution:

    def longestCommonPrefix(self, strs):

        obj = Trie()
        for s in strs:
            obj.insert(s)
        return obj.getLongestPrefix(strs)


if __name__ == "__main__":
    obj = Solution()
    print(obj.longestCommonPrefix(strs=["flower","flow","flight"]))
    print(obj.longestCommonPrefix(strs=["flower", "flow"]))
    print(obj.longestCommonPrefix(strs=["flow", "flow"]))