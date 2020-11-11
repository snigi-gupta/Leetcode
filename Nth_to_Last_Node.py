# https://www.educative.io/courses/ds-and-algorithms-in-python/mE23Jj5pp93


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

    def length(self, current):
        if current is None:
            return 0
        return 1 + self.length(current.next)


class Solution:
    def print_nth_to_lastnode(self, ll, list_len, n):
        current = ll.head
        while current:
            if n == 0:
                return current
            current = current.next
            n -= 1



if __name__ == "__main__":
    ll = LinkedList()
    mylist = [1, 4, 1, 2, 2, 3, 4]
    for i in mylist:
        ll.append(i)
    ll.printnode()
    list_len = ll.length(ll.head)

    obj = Solution()
    nthnode = obj.print_nth_to_lastnode(ll=ll, list_len=list_len, n=4)
    nthnode.printnode()
