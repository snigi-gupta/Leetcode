# https://leetcode.com/problems/lru-cache/solution/

"""
Goal : To create a least recently used cache

put(key, value)
- insert the value in the cache, if the key does not exist
- update the value in the cache for that key, if the key exists
- check if the capacity of the cache has exceeded and then evict the least recently used value.
> check is the value is not in the hashmap? > yes: add after the head, no: update the node's data and add it right after the head
> check is the capacity has exceeded?> no: do nothing, yes: remove the element right before the tail.
hashmap:
1: node1
2: update node val
4: node4


head<->value8<->value4<->value1<->tail

get(key)
- return the value for the given key.
- if key does not exists return -1
>hashmap: store the keys: node to the element in the double linked list.
> double linked list:  values as head<->e1<->e12<->...<->tail

cache: will have a limited capacity (which is given)

"""


class DLinkedNode:
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRUCache:
    def addNode(self, node):
        current = self.head
        node.prev = current
        node.next = current.next

        current.next.prev = node
        current.next = node

    def removeNode(self, node):
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def moveToHead(self, node):

        self.removeNode(node)
        self.addNode(node)

    def popFromTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node

    def __init__(self, capacity):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()

        self.head.next = self.tail
        self.head.tail = self.head

    def get(self, key):
        node = self.cache.get(key, None)

        if not node:
            return -1

        self.moveToHead(node)
        return node.value

    def put(self, key, value):
        node = self.cache.get(key)

        if not node:
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
            self.addNode(newNode)

            self.size += 1

            if self.size > self.capacity:
                tail = self.popFromTail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.value = value
            self.moveToHead(node)


if __name__ == "__main__":
    lRUCache = LRUCache(2)
    print(lRUCache.put(1, 1))  # cache is {1 = 1}
    print(lRUCache.put(2, 2))  # cache is {1 = 1, 2 = 2}
    print(lRUCache.get(1))  # return 1
    print(lRUCache.put(3, 3))  # LRU key was 2, evicts key 2, cache is {1 = 1, 3 = 3}
    print(lRUCache.get(2))  # returns - 1(not found)
    print(lRUCache.put(4, 4))  # LRU key was 1, evicts key 1, cache is {4 = 4, 3 = 3}
    print(lRUCache.get(1))  # return -1(not found)
    print(lRUCache.get(3))  # return 3
    print(lRUCache.get(4))  # return 4
