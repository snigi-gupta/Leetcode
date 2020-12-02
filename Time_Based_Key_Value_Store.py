"""
Goal: Design a class TimeMap
- set(key, value, timestamp)
    Store the tuple in a hashmap.
- get(key, timestamp)
    Return the prev_timestamp <= timestamp
    if min(prev_timestamps) > timestamp, return ""

Data structure: Hashmap
Solution: Binary Search
"""
# https://leetcode.com/problems/time-based-key-value-store/
from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key, value, timestamp):
        self.hashmap[key].append([timestamp, value])

    def get(self, key, timestamp):

        if key not in self.hashmap or timestamp < self.hashmap[key][0][0]:
            return ""

        if timestamp > self.hashmap[key][-1][0]:
            return self.hashmap[key][-1][1]
        left = 0
        right = len(self.hashmap[key])
        while left < right:

            mid = left + (right - left) // 2

            if self.hashmap[key][mid][0] == timestamp:
                return self.hashmap[key][mid][1]
            elif self.hashmap[key][mid][0] > timestamp:
                right = mid - 1
            else:
                left = mid
        return self.hashmap[key][left][1]


if __name__ == "__main__":
    obj = TimeMap()
    print(obj.set("foo", "bar", 1))
    print(obj.get("foo", 1))
    print(obj.get("foo", 3))
    print(obj.set("foo", "bar2", 4))
    print(obj.get("foo", 4))
    print(obj.get("foo", 5))
    print(obj.set("love", "high", 10))
    print(obj.set("love", "low", 20))
    print(obj.get("love", 5))
    print(obj.get("love", 10))
    print(obj.get("love", 15))
    print(obj.get("love", 20))
    print(obj.get("love", 25))
