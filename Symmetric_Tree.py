# https://leetcode.com/problems/symmetric-tree/
# https://www.youtube.com/watch?v=K7LyJTWr2yA
# https://www.youtube.com/watch?v=XV7Sg2hJO3Q


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    # In-order traversal
    def printTree(self, lev=0):
        if self.left:
            self.left.printTree(lev+1)
        print(' ' * 4 * lev + '->', self.val)
        if self.right:
            self.right.printTree(lev+1)


class Solution:
    def check(self, left, right):
        if left is None and right is None:
            return True
        elif left is not None and right is not None:
            return left.val == right.val and self.check(left.left, right.right) and self.check(left.right, right.left)
        return False

    def isSymmetric(self, root):
        return root is None or self.check(root.left, root.right)


if __name__ == "__main__":
    root = TreeNode(7)
    root.left = TreeNode(8)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(6)
    root.right = TreeNode(None)
    root.right.right = TreeNode(6)
    root.right.left = TreeNode(6)
    print("Tree")
    root.printTree()

    obj = Solution()
    print(obj.isSymmetric(root))