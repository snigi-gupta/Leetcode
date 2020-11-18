# https://leetcode.com/problems/reverse-linked-list/

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def appendNode(self, val):
        newnode = Node(val)
        if self.head is None:
            self.head = newnode
            return
        current = self.head
        while current.next:
            current = current.next

        current.next = newnode

    def printNode(self):
        current = self.head
        while current:
            print(current.val, end=" ")
            current = current.next

    def reverseNode(self):
        current = self.head
        prev_node = None
        while current:
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node
        self.head = prev_node


class Solution:
    def reverseList(self, head):
        print("")


if __name__ == "__main__":
    ll = LinkedList()
    ll.appendNode(1)
    ll.appendNode(2)
    ll.appendNode(3)
    ll.appendNode(4)
    ll.appendNode(5)
    ll.printNode()
    ll.reverseNode()
    ll.printNode()



