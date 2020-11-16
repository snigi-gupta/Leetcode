# https://leetcode.com/problems/minimum-depth-of-binary-tree/
import sys


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root):
        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)

            if None in [node.left, node.right]:
                return max(left, right) + 1
            else:
                return min(left, right) + 1

        return helper(root)


if __name__ == "__main__":
    """
            1
        2       2
    3       3
4       4
    """
    binaryTree = TreeNode(1)
    binaryTree.left = TreeNode(2)
    binaryTree.right = TreeNode(2)
    binaryTree.left.left = TreeNode(3)
    binaryTree.left.right = TreeNode(3)
    binaryTree.left.left.left = TreeNode(4)
    binaryTree.left.left.right = TreeNode(4)

    obj = Solution()
    print(obj.minDepth(binaryTree))

    """
        2
            3
                4
                    5
                        6
    """
    binaryTree = TreeNode(2)
    binaryTree.right = TreeNode(3)
    binaryTree.right.right = TreeNode(4)
    binaryTree.right.right.right = TreeNode(5)
    binaryTree.right.right.right.right = TreeNode(6)

    print(obj.minDepth(binaryTree))
