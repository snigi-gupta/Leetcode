# https://leetcode.com/problems/binary-tree-right-side-view/

from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root):

        if root is None:
            return []
        order = []
        firstqueue = deque([root])
        node = TreeNode(None)
        while firstqueue:
            secondqueue = firstqueue
            firstqueue = deque()
            while secondqueue:
                node = secondqueue.popleft()
                if node.left:
                    firstqueue.append(node.left)
                if node.right:
                    firstqueue.append(node.right)
            order.append(node.val)

        return order


if __name__ == "__main__":
    """
                1
            2       3
        null 5   null  4
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)

    obj = Solution()
    print(obj.rightSideView(root))
