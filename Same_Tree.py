# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def printTree(self):
        print(self.val, end="  ")

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
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def check_tree(firstNode, secondNode):
            if firstNode is None and secondNode is None:
                return True
            if firstNode is None or secondNode is None:
                return False
            if firstNode.val != secondNode.val:
                print(f'first: {firstNode.val}, second: {secondNode.val}')
                return False
            else:
                return check_tree(firstNode.left, secondNode.left) and check_tree(firstNode.right, secondNode.right)
        return check_tree(p,q)


root = TreeNode(7)
root.insertLeaf(6)
root.insertLeaf(8)
root.insertLeaf(4)
print("First tree")
root.printTree()

root2 = TreeNode(7)
root2.insertLeaf(6)
root2.insertLeaf(9)
root2.insertLeaf(4)
print("")
print("Second tree")
root2.printTree()

obj = Solution()
print("Ans", obj.isSameTree(root, root2))
