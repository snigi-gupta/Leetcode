# https://leetcode.com/problems/merge-two-sorted-lists/
# https://www.geeksforgeeks.org/merge-two-sorted-linked-lists/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, val):
        newnode = ListNode(val)
        if self.head is None:
            self.head = newnode
            return
        lastnode = self.head
        while lastnode.next:
            lastnode = lastnode.next
        lastnode.next = newnode

    def printnode(self):
        current = self.head
        while current.next:
            print(f'{current.val}  ->', end=" ")
            current = current.next
        print(f'{current.val}')

class Solution:
    """
    If l1 and l2 have type list
    """
    def mergeTwoLists(self, l1, l2):
        i,j = 0,0
        result = []
        while i <len(l1) and j<len(l2):
            if l1[i] < l2[j]:
                result.append(l1[i])
                i += 1
            elif l2[j] < l1[i]:
                result.append(l2[j])
                j += 1
            else:
                result.extend([l1[i], l2[j]])
                i += 1
                j += 1

        if i != len(l1)-1:
            result.extend(l1[i:])
        if j != len(l2)-1:
            result.extend(l2[j:])

        return result

    """
    If l1 and l2 are of type ListNode
    This is an iterative solution
    """
    def mergeTwoLists2(self, l1, l2):
        result = LinkedList()
        l1current = l1.head
        l2current = l2.head
        while l1current and l2current:
            if l1current.val < l2current.val:
                result.append(l1current.val)
                l1current = l1current.next
            elif l2current.val < l1current.val:
                result.append(l2current.val)
                l2current = l2current.next
            else:
                result.append(l1current.val)
                result.append(l2current.val)
                l1current = l1current.next
                l2current = l2current.next

        while l1current:
            result.append(l1current.val)
            l1current = l1current.next

        while l2current:
            result.append(l2current.val)
            l2current = l2current.next

        return result

    """
    Recursive solution
    """
    def recursive(self, l1current, l2current):
        tempNode = None
        if l1current is None:
            return l2current
        elif l2current is None:
            return l1current
        elif l1current.val <= l2current.val:
            tempNode = l1current
            tempNode.next = self.recursive(l1current.next, l2current)
            return tempNode
        elif l2current.val < l1current.val:
            tempNode = l2current
            tempNode.next = self.recursive(l1current, l2current.next)
            return tempNode


if __name__ == "__main__":
    obj = Solution()
    print(obj.mergeTwoLists(l1=[1,2,4,8,8,9], l2=[1,3,4,5,6]))

    l1 = LinkedList()
    l2 = LinkedList()

    list1 = [1,2,4]
    list2 = [1,3,4]

    for val in list1:
        l1.append(val)
    print("l1:")
    l1.printnode()

    print(" ")
    for val in list2:
        l2.append(val)
    print("l2:")
    l2.printnode()

    print("result")
    result = obj.mergeTwoLists2(l1=l1, l2=l2)
    result.printnode()

    print("result")
    result = LinkedList()
    result.head = obj.recursive(l1.head, l2.head)
    result.printnode()