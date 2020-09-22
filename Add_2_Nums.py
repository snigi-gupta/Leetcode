class ListNode:
    def __init__(self, value):
        self.value = value
        self.nextNode = None

class LinkedList:

    def __init__(self):
        self.head = None

    def traverse(self):
        currentNode = self.head

        while currentNode:
            print(currentNode.value, "->")
            currentNode = currentNode.nextNode

    def insertAtEnd(self, value):
        NewListNode = ListNode(value)
        if self.head is None:
            self.head = NewListNode
            return
        lastNode = self.head
        while lastNode.nextNode:
            lastNode = lastNode.nextNode
        lastNode.nextNode = NewListNode


class AddTwoNumbers:
    def addTwoNumbers(self, l1: LinkedList, l2: LinkedList):
        r = None
        p = None
        c = 0

        l1 = l1.head
        l2 = l2.head

        nNode = LinkedList()
        while l1 or l2 or c != 0:
            v = (l1.value if l1 else 0) + (l2.value if l2 else 0) + c
            c = v // 10
            # n = ListNode(v % 10)
            # if r is None:
            #     r = n
            # if p is not None:
            #     p.nextNode = n

            nNode.insertAtEnd(v%10)
            # p = n
            l1 = l1.nextNode if l1 else None
            l2 = l2.nextNode if l2 else None

        # nNode.traverse()
        return nNode


if __name__ == "__main__":

    l1 = [2, 4, 3]
    l2 = [5, 6, 4]

    # print("l1")
    l1Node = LinkedList()
    l1Node.head = ListNode(l1[0])

    for v in l1[1:]:
        l1Node.insertAtEnd(v)

    # l1Node.traverse()

    # print("l2")
    l2Node = LinkedList()
    l2Node.head = ListNode(l2[0])

    for v in l2[1:]:
        l2Node.insertAtEnd(v)

    # l2Node.traverse()

    addTwoNumsObj = AddTwoNumbers()
    result = addTwoNumsObj.addTwoNumbers(l1Node, l2Node)
    result.traverse()



    """
    Uncomment below to simple create a linked list
    """
    # node = LinkedList()
    # node.head = ListNode(1)
    # node2 = ListNode(2)
    # node3 = ListNode(3)
    #
    # node.head.nextNode = node2
    # node2.nextNode = node3
    #
    # node.traverse()
    # node.insertAtEnd(4)
    # print("New List")
    # node.traverse()