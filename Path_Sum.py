class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def printTree(self):
        print(self.val)
        if self.left:
            self.left.printTree()

        if self.right:
            self.right.printTree()

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


class Solution:

    def hasPathSum(self, root: 'TreeNode', sum: 'int') -> 'bool':
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        sum -= root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


if __name__ == "__main__":
    obj = Solution()
    root = TreeNode(7)
    root.insertLeaf(6)
    root.insertLeaf(8)
    root.insertLeaf(4)
    root.printTree()

    print(obj.hasPathSum(root, 17))