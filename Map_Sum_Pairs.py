# https://leetcode.com/problems/map-sum-pairs/

class MapSumNode:
    def __init__(self):
        self.children = {}
        self.weight = 0


class MapSum:

    def __init__(self):
        self.root = MapSumNode()

    def dfs(self, current):
        stack = [current]
        result = 0
        while stack:
            curr = stack.pop()
            result += curr.weight
            for child in curr.children:
                stack.append(curr.children[child])
        return result

    def insert(self, key: str, val: int) -> None:
        current = self.root
        for ch in key:
            if ch not in current.children:
                current.children[ch] = MapSumNode()
            current = current.children[ch]
        current.weight = val

    def getSum(self, prefix: str) -> int:
        current = self.root
        for ch in prefix:
            if ch not in current.children:
                return 0
            current = current.children[ch]
        return self.dfs(current)


if __name__ == "__main__":

    obj = MapSum()
    print(obj.insert("aa", 3))
    print(obj.insert("aa", 2))
    print(obj.getSum(prefix="a"))

