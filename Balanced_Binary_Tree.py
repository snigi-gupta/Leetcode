# https://leetcode.com/problems/balanced-binary-tree/
from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root):
        self.root = TreeNode(root)


    def insertLeaf(self, leaf, current):
        node = TreeNode(leaf)

        if current.val > leaf:
            if current.left is None:
                current.left = node
            else:
                self.insertLeaf(leaf, current.left)
        elif current.val < leaf:
            if current.right is None:
                current.right = node
            else:
                self.insertLeaf(leaf, current.right)
        else:
            current.val = leaf


    def printnode(self):
        node = self.root
        # print(node.val)
        theQueue = deque([node])
        while theQueue:
            temp_node = theQueue.popleft()
            print(temp_node.val, end=" ")
            if temp_node.left:
                theQueue.append(temp_node.left)
            if temp_node.right:
                theQueue.append(temp_node.right)


class Solution:
    def isBalanced(self, root):
        def getHeight(node):
            if node is None:
                return 0, True
            left, l_flag = getHeight(node.left)
            right, r_flag = getHeight(node.right)
            sub_tree_diff = abs(left-right)
            if sub_tree_diff > 1 or not l_flag or not r_flag:
                return -1, False
            return max(left, right) + 1, True

        height, result =  getHeight(root)
        return result



if __name__ == "__main__":
    """
    This creates a BST
        20
    9       35
3        31
    """
    tree = Tree(20)
    tree.insertLeaf(9, tree.root)
    tree.insertLeaf(3, tree.root)
    tree.insertLeaf(35, tree.root)
    tree.insertLeaf(31, tree.root)
    tree.insertLeaf(30, tree.root)
    tree.insertLeaf(29, tree.root)

    tree.printnode()

    obj = Solution()
    print(obj.isBalanced(tree.root))

    """
    This creates a Binary Tree
        3
    9       20
        15      7
    """
    binaryTree = TreeNode(3)
    binaryTree.left = TreeNode(9)
    binaryTree.right = TreeNode(20)
    binaryTree.right.left = TreeNode(15)
    binaryTree.right.right =TreeNode(7)
    print("Binary Tree balanced?", obj.isBalanced(binaryTree))

    """
            1
        2       2
    3       3
4       4
    """
    binaryTree2 = TreeNode(1)
    binaryTree2.left = TreeNode(2)
    binaryTree2.right = TreeNode(2)
    binaryTree2.left.left = TreeNode(3)
    binaryTree2.left.right =TreeNode(3)
    binaryTree2.left.left.left =TreeNode(4)
    binaryTree2.left.left.right =TreeNode(4)
    print("Binary Tree balanced?", obj.isBalanced(binaryTree2))

