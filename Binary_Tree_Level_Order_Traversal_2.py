# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root):
        if root is None:
            return []
        order = []
        firstqueue = deque([root])

        while firstqueue:
            secondqueue = firstqueue
            firstqueue = deque()
            order.append([])
            while secondqueue:
                node = secondqueue.popleft()
                order[-1].append(node.val)
                if node.left:
                    firstqueue.append(node.left)
                if node.right:
                    firstqueue.append(node.right)
        return order[::-1]


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    obj = Solution()
    print(obj.levelOrderBottom(root))