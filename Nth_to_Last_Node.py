# https://www.educative.io/courses/ds-and-algorithms-in-python/mE23Jj5pp93
# INCOMPLETE

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
    def print_nth_to_lastnode(self, ll, nth):
        # calculate length
        current = ll.head
        length = 0
        while current:
            length += 1
            current = current.next
        print("length", length)
        current = ll.head

        while length != nth and current.next:
            current = current.next
            length -= 1
        return current.val


if __name__ == "__main__":
    ll = LinkedList()
    mylist = [1, 4, 1, 2, 2, 3, 4]
    # mylist = ["A", "B", "C", "D"]
    for i in mylist:
        ll.append(i)
    ll.printnode()
    list_len = ll.length(ll.head)
    print(list_len)

    obj = Solution()
    nthnode = obj.print_nth_to_lastnode(ll, nth=2)
    print("nth_node", nthnode)
