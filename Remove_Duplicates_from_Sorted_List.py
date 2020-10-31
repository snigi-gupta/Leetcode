# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = LinkedList()

    def append(self, val):
        newnode = ListNode(val=val)
        if self.head is None:
            self.head = newnode
        lastnode = self.head
        while lastnode.next:
            lastnode = lastnode.next
        lastnode.next = newnode

    def printnode(self):
        current = self.head
        while current.next:
            print(f'{current.val} -> ', end=" ")
            current = current.next
        print(f'{current.val}')


class Solution:
    def deleteDuplicates(self, ll):
        current = ll.head
        while current is not None and current.next is not None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return ll


if __name__ == "__main__":
    ll = LinkedList()
    mylist = [1,1,1,2,2,3,4]
    for i in mylist:
        ll.append(i)
    ll.printnode()

    obj = Solution()
    result = obj.deleteDuplicates(ll=ll)
    result.printnode()
