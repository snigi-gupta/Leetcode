# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        newnode = ListNode(val)

        if self.head is None:
            self.head = newnode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newnode

    def printnode(self):
        current = self.head
        seen = set()    # to not print infinitely if circular
        while current.next:
            if current.val not in seen:
                print(f' {current.val} ->', end=" ")
                seen.add(current.val)
                current = current.next
            else:
                break

        print(f' {current.val}')

    def circular(self, val, pos):
        current = self.head

        count = 0
        while count < pos-1:
            current = current.next
            count += 1

        cir_address = current.next

        while current.val != val:
            current = current.next

        current.next = cir_address

    def hasCycle(self):
        current = self.head
        seen = set()

        while current.next:
            if current not in seen:
                seen.add(current)
                current = current.next
            else:
                return True

        return False


if __name__ == "__main__":
    head = LinkedList()
    head.append(3)
    head.append(2)
    head.append(0)
    head.append(-4)
    print("before circular link")
    head.printnode()
    head.circular(-4, 1)
    print("after circular link")
    head.printnode()

    print(head.hasCycle())