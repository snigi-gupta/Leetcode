# BST Preorder Traversal


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


class Solution:
    def preorder(self, node, result):
        # print(node.val, end=" ")
        result.append(node.val)
        if node.left:
            self.preorder(node.left, result)
        if node.right:
            self.preorder(node.right, result)
        return result

    def inorder(self, node, result):
        if node.left:
            self.inorder(node.left, result)
        result.append(node.val)
        if node.right:
            self.inorder(node.right, result)
        return result

    def postorder(self, node, result):
        if node.left:
            self.postorder(node.left, result)
        if node.right:
            self.postorder(node.right, result)
        result.append(node.val)
        return result


if __name__ == "__main__":
    root = TreeNode(3)
    root.insertLeaf(5)
    root.insertLeaf(1)
    root.insertLeaf(9)
    root.insertLeaf(4)
    root.insertLeaf(8)


    obj = Solution()
    print("Pre-Order: ", obj.preorder(root, []))
    print("In-Order: ", obj.inorder(root, []))
    print("Post-Order: ", obj.postorder(root, []))
