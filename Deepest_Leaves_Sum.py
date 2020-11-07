# https://leetcode.com/problems/deepest-leaves-sum/

from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root):
        if root is None:
            return 0
        answer = 0
        firstqueue = deque([root])
        secondqueue = deque()
        while firstqueue:
            secondqueue = firstqueue
            firstqueue = deque()
            for node in secondqueue:
                if node.left:
                    firstqueue.append(node.left)
                if node.right:
                    firstqueue.append(node.right)

        for leaf in secondqueue:
            answer += leaf.val
        return answer


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
    print(obj.deepestLeavesSum(root))