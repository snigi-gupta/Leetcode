# https://leetcode.com/problems/design-hashmap/


class Bucket:
    def __init__(self):
        self.bucket = []

    def find(self, key):
        for (k, v) in self.bucket:
            if key == k:
                return v
        return -1

    def update(self, key, value):
        found = False

        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break
        if not found:
            self.bucket.append((key, value))

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 2069
        self.hashMap = [Bucket() for _ in range(self.size)]

    def put(self, key, value):
        """
        value will always be non-negative.
        """
        hashKey = key % self.size
        self.hashMap[hashKey].update(key, value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hashKey = key % self.size
        return self.hashMap[hashKey].find(key)

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hashKey = key % self.size
        self.hashMap[hashKey].remove(key)


if __name__ == "__main__":
    hashMap = MyHashMap()
    print(hashMap.put(1, 1))
    print(hashMap.put(2070, 1))
    print(hashMap.put(2, 2))
    print(hashMap.get(1))
    print(hashMap.get(2070))
    print(hashMap.put(2, 1))
    print(hashMap.get(2))
    print(hashMap.remove(2))
    print(hashMap.get(2))
