# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def helper(node):

            if node:
                if low <= node.val <= high:
                    self._sum += node.val

                if node.val > low:
                    helper(node.left)
                if node.val < high:
                    helper(node.right)

        self._sum = 0
        helper(root)

        return self._sum


if __name__ == "__main__":
    treenode = TreeNode(10)
    treenode.left = TreeNode(5)
    treenode.right = TreeNode(15)
    treenode.left.left = TreeNode(3)
    treenode.left.right = TreeNode(7)
    treenode.right.right = TreeNode(18)

    obj = Solution()
    ans = obj.rangeSumBST(treenode, 7, 15)
    print(ans)