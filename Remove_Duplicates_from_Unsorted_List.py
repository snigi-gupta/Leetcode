# https://www.educative.io/courses/ds-and-algorithms-in-python/g7nEp50EkBk


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        newnode = ListNode(val=val)
        if self.head is None:
            self.head = newnode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newnode

    def printnode(self):
        current = self.head
        while current.next:
            print(f'{current.val} -> ', end=" ")
            current = current.next
        print(f'{current.val}')


class Solution:
    def deleteDuplicates(self, ll):
        current = ll.head
        seen = {}
        prevnode = None
        while current:
            if current.val not in seen:
                seen[current.val] = 1
                prevnode = current
            else:
                prevnode.next = current.next
                current = None
            current = prevnode.next


if __name__ == "__main__":
    ll = LinkedList()
    mylist = [1, 4, 1, 2, 2, 3, 4]
    for i in mylist:
        ll.append(i)
    ll.printnode()

    obj = Solution()
    obj.deleteDuplicates(ll=ll)
    ll.printnode()
