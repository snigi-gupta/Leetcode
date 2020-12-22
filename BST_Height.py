# BST Calculate Tree Height
# https://www.educative.io/edpresso/finding-the-maximum-depth-of-a-binary-tree
"""
This code calculates the height of a tree using both bottom-up and top-down approach.
"""
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insertLeaf(self, leaf):
        if self.val > leaf:
            if self.left is None:
                self.left = TreeNode(leaf)
            else:
                self.left.insertLeaf(leaf)
        elif self.val < leaf:
            if self.right is None:
                self.right = TreeNode(leaf)
            else:
                self.right.insertLeaf(leaf)
        else:
            self.val = leaf

    def preorder(self, node):
        print(node.val, end=" ")
        if node.left:
            self.preorder(node.left)
        if node.right:
            self.preorder(node.right)


class Solution:
    # top-down approach
    def bstHeightTopDown(self, root):
        def helper(node, height):
            nonlocal ans
            if node.left is None and node.right is None:
                ans = max(ans, height)
                return
            if node.left is not None:
                helper(node.left, height+1)
            if node.right is not None:
                helper(node.right, height+1)
            return ans

        ans = 0
        return helper(root, 1)

    def bstHeightBottomUp(self, root):
        def helper(node):
            if node is None:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            return max(left, right) + 1

        return helper(root)


if __name__ == "__main__":
    root = TreeNode(3)
    root.insertLeaf(5)
    root.insertLeaf(1)
    root.insertLeaf(9)
    root.insertLeaf(4)
    root.insertLeaf(8)

    root.preorder(root)
    obj = Solution()
    print("Height: ", obj.bstHeightTopDown(root))
    print("Height: ", obj.bstHeightBottomUp(root))
